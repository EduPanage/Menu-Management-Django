# MenuHub

A simple restaurant and menu management project developed with **Django**.

## About the Project

MenuHub is a learning project created to review programming concepts and explore specific features and details of the **Django framework**.

The project focuses on understanding Django's structure, models, database relationships, and administrative interface.

## Features

- Restaurant registration and management.
- Menu item registration.
- Association between menu items and restaurants.
- Database management using Django ORM.
- Model administration through Django Admin.

## Technologies

- Python
- Django
- SQLite
- HTML

## Project Structure

```text
MenuHub/
│
├── menuhub/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── menus/
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
│
├── db.sqlite3
└── manage.py
```

## Getting Started

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd MenuHub
```

Install Django:

```bash
pip install django
```

Run database migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Access the application at:

```text
http://127.0.0.1:8000/
```

## Learning Objectives

This project was developed for study and practice, with the goal of reviewing and improving knowledge of:

- Django project and application structure.
- Models and database relationships.
- Django ORM.
- Django Admin.
- SQLite database integration.

## Author

**EduPanage**
