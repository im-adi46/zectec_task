# Movie Management System

## 📌 Project Overview

The **Movie Management System** is a Django-based web application designed to manage a collection of movies. Users can add, edit, delete, and view movie details, making it easy to organize and showcase movie information.

---

## 🚀 Features


* **Add Movies:** Add new movies with title, description, director, and image.
* **Edit/Delete Movies:** Easily update or remove existing movie entries.
* **Movie List:** View a paginated list of all movies with images and details.
* **Dropdown Selection:** Use dropdown menus for fields like director during movie addition.


---

## 🛠️ Installation Steps

### Prerequisites

Make sure you have the following installed:

* Python 3.8+
* Django
* SQLite (default database) or any preferred database

### Steps to Run the Project

```bash
git clone <repository-url>
cd movie-management-system

# Create virtual environment
python -m venv env

# Activate environment
# macOS/Linux:
source env/bin/activate  
# Windows:
env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser for admin access
python manage.py createsuperuser

# Start server
python manage.py runserver
```

Access the application at:
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Project Structure

```
movie-management-system/
├── movieapp/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── forms.py
├── movie_management_system/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── media/
│   ├── movie_images/
├── static/
├── templates/
│   ├── movies_list.html
│   ├── add_movie.html
│   ├── edit_movie.html
│   ├── base.html
├── db.sqlite3
├── manage.py
├── requirements.txt
├── README.md
```

---


## 📞 Support

For questions or suggestions, please reach out. ✨

