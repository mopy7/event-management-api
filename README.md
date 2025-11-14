# Event Management API (Django REST Framework)

A clean, versioned, production-style Event Management API built with Django REST Framework.  
This project demonstrates authentication, permissions, CRUD operations, custom user access rules, and a professional API structure.

---

## 🚀 Features

### 🔐 Authentication
- Token Authentication
- Register API
- Login API

### 👥 User Management
- Secure password hashing
- Unique username & email
- Token generation on login

### 📦 Event Management
- Create, Read, Update, Delete (CRUD)
- Each event is owned by the user who created it
- Automatic owner assignment
- Timestamp tracking (`created_at`, `updated_at`)

### 🔒 Permissions
- Public access for GET requests
- Authenticated access for create/update/delete
- Custom permission: Only owner can modify or delete their events (`IsOwner`)

### 🧩 Tech Stack
- Python 3.12.3
- Django 5.2
- Django REST Framework
- DRF Token Authentication

---

## 📁 Project Structure
```bash
core/
│
├── manage.py
│
├── core/                          # Project settings
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── events/                        # App containing Event model
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── models.py
│   ├── tests.py
│   └── views.py   (empty/not used)
│
└── api/
    └── v1/
        └── events/
            ├── __init__.py
            ├── serializers.py
            ├── views.py
            ├── urls.py
            └── permissions.py
```


---

## 📌 API Endpoints

### 🔐 Authentication
| Method | Endpoint                     | Description          |
|--------|------------------------------|----------------------|
| POST   | /api/v1/events/register/     | Register new user    |
| POST   | /api/v1/events/login/        | Login & get token    |

### 📦 Event CRUD
| Method | Endpoint                | Auth | Description               |
|--------|--------------------------|------|---------------------------|
| GET    | /api/v1/events/          | ❌   | List all events           |
| POST   | /api/v1/events/          | ✔️   | Create event (owner auto) |
| GET    | /api/v1/events/<id>/     | ❌   | Retrieve event            |
| PUT    | /api/v1/events/<id>/     | ✔️   | Update event (owner only) |
| PATCH  | /api/v1/events/<id>/     | ✔️   | Partial update            |
| DELETE | /api/v1/events/<id>/     | ✔️   | Delete (owner only)       |

---

## 🛠️ Installation

```bash
git clone <your-repo-url>
pip install -r requirements.txt
cd src/core
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
