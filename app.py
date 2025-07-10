from flask import Flask, render_template, request, redirect, session, url_for, jsonify
import mysql.connector
import datetime
from config import DB_CONFIG, GOOGLE_CLIENT_ID
from utils.auth import register_user, login_user, verify_google_token
from utils.health import calculate_bmi, recommend_exercise, calculate_water, calculate_calories

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        result = register_user(request.form)
        if result['success']:
            return redirect('/')
        return result['message']
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    result = login_user(request.form)
    if result['success']:
        session['user_id'] = result['user_id']
        return redirect('/dashboard')
    return result['message']

@app.route('/google-login', methods=['POST'])
def google_login():
    token = request.json.get('token')
    user_info = verify_google_token(token)
    if not user_info:
        return jsonify({'error': 'Invalid Google token'}), 401

    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (user_info['email'],))
    user = cursor.fetchone()

    if not user:
        cursor.execute("INSERT INTO users (name, email, weight, height) VALUES (%s, %s, 0, 0)",
                       (user_info['name'], user_info['email']))
        db.commit()
        user_id = cursor.lastrowid
    else:
        user_id = user['id']

    session['user_id'] = user_id
    return jsonify({'success': True}), 200

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/')
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id=%s", (session['user_id'],))
    user = cursor.fetchone()

    bmi = calculate_bmi(user['weight'], user['height'])
    water = calculate_water(user['weight'])
    calories = calculate_calories(user['weight'], user['age'])
    exercises = recommend_exercise(user['age'])

    return render_template('dashboard.html', user=user, bmi=bmi,
                           water=water, calories=calories, exercises=exercises)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)