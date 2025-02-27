# Inventory Management System

A simple Django-based inventory management system that allows you to track items and their suppliers.

## Setup

1. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Apply database migrations:
```bash
cd inventory
python manage.py makemigrations
python manage.py migrate
```

4. Create a superuser:
```bash
python manage.py createsuperuser
```

5. Run the development server:
```bash
python manage.py runserver
```

## Usage

- Access the admin interface at: http://localhost:8000/admin/
- View inventory list at: http://localhost:8000/inventory/
- API endpoints:
  - List inventory: http://localhost:8000/api/inventory/
  - Search by name: http://localhost:8000/api/inventory/?search=query

## Testing
```bash
python manage.py test inventory
```
The following endpoints should return 200 OK status:
- /inventory/
- /api/inventory/
- /inventory/<id>/ `