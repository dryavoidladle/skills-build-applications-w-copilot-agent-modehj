# Octofit Tracker

## Overview
Octofit Tracker is a Django-based application designed to help manage and track fitness activities for high school students. This project serves as a backend for the Octofit Tracker app, providing the necessary APIs and database management.

## Project Structure
The project is organized as follows:

```
octofit-tracker
└── backend
    ├── octofit_tracker
    │   ├── __init__.py
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── manage.py
    ├── apps
    │   └── tracker
    │       ├── __init__.py
    │       ├── admin.py
    │       ├── apps.py
    │       ├── migrations
    │       │   └── __init__.py
    │       ├── models.py
    │       ├── tests.py
    │       └── views.py
    └── README.md
```

## Setup Instructions

1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd octofit-tracker/backend
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```
   pip install django
   ```

4. **Run Migrations**
   ```
   python manage.py migrate
   ```

5. **Start the Development Server**
   ```
   python manage.py runserver
   ```

## Usage
Once the server is running, you can access the application at `http://127.0.0.1:8000/`. You can create, read, update, and delete fitness tracking records through the provided API endpoints.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.