#Fitness Tracking Web Application
This is a complete Flask-based Fitness Tracking Web Application with user registration, login (including Google Sign-In), personalized exercise recommendations based on BMI and goals, diet suggestions, and water intake tracking with graphical progress visualization.

✨ Features
🔑 User Authentication

Register with name, email, password, age, height, weight

Login via email/password

Google Sign-In integration

🏃 Dashboard

Calculates BMI dynamically

Provides personalized exercise plans based on BMI category and goal (Fat Loss, Maintenance, Muscle Gain)

Displays recommended diet plans

Shows water intake recommendations with progress graphs

📊 Database Integration

Uses MySQL with SQLAlchemy for storing users, exercises, and food suggestions

🎨 Clean Frontend

HTML templates with responsive CSS styling

Bootstrap-enhanced user interface for professional look

🌐 Technologies Used

Python (Flask)

MySQL with SQLAlchemy

Authlib for Google OAuth

HTML, CSS, Bootstrap

⚙️ Setup Instructions
Clone or download this repository.

Install requirements:

bash
Copy
Edit
pip install -r requirements.txt
Import the provided fitness_app.sql into your MySQL server.

Update database credentials in app.py if needed.

Run the app:

bash
Copy
Edit
python app.py
Access on http://localhost:5000.
