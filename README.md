# Movie Management System

## 📌 Project Overview

The **Movie Management System** is a Django-based web application designed to manage a collection of movies. Users can add, edit, delete, and view movie details along with images, making it easy to organize and showcase movie information.

---

## 🚀 Features

* **User Authentication:** Secure login for users to manage movie entries.
* **Add Movies:** Add new movies with title, description, director, and image.
* **Edit/Delete Movies:** Easily update or remove existing movie entries.
* **Movie List:** View a paginated list of all movies with images and details.
* **Dropdown Selection:** Use dropdown menus for fields like director during movie addition.
* **Image Upload:** Upload and display movie poster images.

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

## 📅 Development Timeline

| Week   | Tasks Completed                                              |
| ------ | ------------------------------------------------------------ |
| Week 1 | Setup Django project, create Movie model, migrations         |
| Week 2 | Build CRUD views and templates (list, add, edit, delete)     |
| Week 3 | Implement image upload and display functionality             |
| Week 4 | Add dropdown fields (e.g., director), testing, and debugging |

---

## 🌐 Deployed Link

*(Add your live deployed link here when available)*

---

## 📌 Contribution

Want to contribute?

1. Fork the repository
2. Create a new branch (`feature-xyz`)
3. Commit your changes
4. Push the branch and create a Pull Request

---

## 📞 Support

For questions or suggestions, please reach out. ✨

