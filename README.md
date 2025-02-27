# Inventory Management System

A simple Django-based inventory management system that allows you to track items and their suppliers.

## Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/Harismur98/KiraTech_Assignment.git
cd KiraTech_Assignment
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv .venv
.venv\Scripts\activate

# On macOS/Linux
python -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Navigate to the project directory:
```bash
cd inventory
```

5. Apply database migrations:
```bash
python manage.py migrate
```

6. Create a superuser (admin account):
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Accessing the Application

- Admin Interface: http://localhost:8000/admin/
  - Login with your superuser credentials
  - Manage inventory items and suppliers
- Inventory List: http://localhost:8000/inventory/
- API Endpoints:
  - List all items: http://localhost:8000/api/inventory/
  - Search items: http://localhost:8000/api/inventory/?search=query

## Running Tests

To run the test suite:
```bash
python manage.py test inventory
```