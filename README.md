# Task-Management-web-App - Khadeim Rahman
This is the framework for my web application which was made for task management.
This guide will help you set it up locally.

---

## 1. Clone the repository

git clone <your-repo-url>
cd TaskPlusFinal 

2. Create a Python virtual environment

Recommended Python version: 3.11

# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt

4. Set up the database
python manage.py makemigrations
python manage.py migrate

If you get migration conflicts:

python manage.py makemigrations --merge

For a fresh start (development only):

Delete db.sqlite3

Delete all files in tasks_app/migrations/ except __init__.py

Run migrations again:

python manage.py makemigrations
python manage.py migrate

5. Create a superuser (optional)
python manage.py createsuperuser

Follow the prompts to set a username, email, and password.

6. Run the development server
# Default port
python manage.py runserver

# Or a custom port if another server is running
python manage.py runserver 8001

Open your browser at http://127.0.0.1:8000
 (or your custom port).

7. Additional Notes

To remove the default AutoField warnings, add this to settings.py:

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

## Features
- update page content without refresh using AJAX.
- Beautiful front-end ReactJs.
- providing API with Django Rest framework.

