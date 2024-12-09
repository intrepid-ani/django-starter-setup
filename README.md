# **Django Starter Template**

The **Django Starter Template** is a pre-configured Django project designed to streamline the setup process for developers. It includes essential configurations and files to help you start your project quickly and efficiently.

---

## **Features**
- ✅ A pre-configured `core` app for basic functionality.
- 🖼️ A minimal `base.html` template for customization.
- 🎨 Includes a `static` folder with placeholder CSS and JS files.
- 📜 Dependency management through `requirements.txt`.
- 📁 Clean and beginner-friendly project structure.

---

## **Setup Instructions**

### **Step 1: Clone the Repository**
Clone this repository to your local machine:
```bash
git clone https://github.com/yourusername/django-starter-setup.git
cd django-starter-template
```

---

### **Step 2: Set Up a Virtual Environment**
Create and activate a virtual environment:

#### For Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### **Step 3: Install Dependencies**
Install the required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

---

### **Step 4: Apply Database Migrations**
Run the following command to set up the database:
```bash
python manage.py migrate
```

---

### **Step 5: Run the Development Server**
Start the server and view your project in the browser:
```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** to see your Django project running.
_(I know this link is of local host)_

---

## **Project Overview**

Here’s the structure of the project:

```
django-starter-template/
├── core/                  # Main application folder
│   ├── views.py           # Basic views for the app
│   ├── urls.py            # URL routing for the app
│   ├── templates/         # Folder for app-specific templates
├── templates/             # Global templates folder
│   └── base.html          # Minimal base template for the project
├── static/                # Static files folder
│   ├── css/               # Placeholder CSS files
│   └── js/                # Placeholder JavaScript files
├── manage.py              # Django project management file
├── requirements.txt       # List of dependencies
└── settings.py            # Django settings file
```

---

## **base.html Overview**
The `base.html` template is a minimal starter file that you can extend and customize as needed. Here's what it includes by default:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Django Project{% endblock %}</title>
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    <header>
        <h1>Welcome to My Django Project</h1>
    </header>
    <script src="{% static 'js/main.js' %}"></script>
</body>
</html>
```

You can extend this template in your app-specific HTML files:
```html
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
    <p>Welcome to the home page!</p>
{% endblock %}
```

---

## **Changing the Project Name**
If you'd like to rename the project to something other than "MyProject," follow these steps:

### **Step 1: Rename the Project Directory**
Rename the project folder:
```bash
mv MyProject NewProjectName
```

### **Step 2: Update the References in `manage.py`**
Edit `manage.py` and update the project name:
```python
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewProjectName.settings')
```

### **Step 3: Update the References in `settings.py`**
In the new project directory, edit `settings.py` and ensure the references to `MyProject` are updated to `NewProjectName`.

### **Step 4: Update the `ASGI` and `WSGI` Files**
If you’re using `ASGI` or `WSGI`, update the imports in these files:
```python
application = get_asgi_application()
```
Change `MyProject.asgi` to `NewProjectName.asgi`.

---

## **Contributing**
We welcome contributions!  
If you have suggestions or want to add new features, feel free to fork this repository and create a pull request.

---

## **License**
This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

---

Let me know if there’s anything else you’d like to adjust or clarify! 😊
