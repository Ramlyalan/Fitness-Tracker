import mysql.connector
from config import DB_CONFIG
from werkzeug.security import generate_password_hash, check_password_hash
from google.oauth2 import id_token
from google.auth.transport import requests

def get_db():
    return mysql.connector.connect(**DB_CONFIG)

def register_user(form):
    db = get_db()
    cursor = db.cursor()
    try:
        hashed = generate_password_hash(form['password'])
        cursor.execute("INSERT INTO users (name, email, password, age, weight, height) VALUES (%s, %s, %s, %s, %s, %s)",
                       (form['name'], form['email'], hashed, form['age'], form['weight'], form['height']))
        db.commit()
        return {'success': True}
    except mysql.connector.Error as err:
        return {'success': False, 'message': str(err)}

def login_user(form):
    db = get_db()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email=%s", (form['email'],))
    user = cursor.fetchone()
    if user and check_password_hash(user['password'], form['password']):
        return {'success': True, 'user_id': user['id']}
    return {'success': False, 'message': 'Invalid credentials'}

def verify_google_token(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), DB_CONFIG['GOOGLE_CLIENT_ID'])
        return {'email': idinfo['email'], 'name': idinfo.get('name', 'Unknown')}
    except Exception:
        return None