# Django Notes - Chapter 3

# settings.py

## What is settings.py?

`settings.py` is the central configuration file for the Django project.

It defines how the application behaves.

Examples:

* Database
* Installed Apps
* Security
* Middleware
* Templates
* Static Files
* Time Zone
* Language
* Authentication

---

## Important Settings

### SECRET_KEY

Used for cryptographic signing.

Never expose it publicly.

Store it inside a `.env` file in production.

---

### DEBUG

Development:

DEBUG = True

Production:

DEBUG = False

When DEBUG=True:

* Detailed error pages are displayed.
* Helpful for development.

When DEBUG=False:

* Sensitive information is hidden.
* Required for production.

---

### ALLOWED_HOSTS

Defines which hosts are allowed to access the application.

Development:

[]

Production:

["lifelinkai.com"]

---

### INSTALLED_APPS

List of Django and custom applications.

Example:

* django.contrib.admin
* django.contrib.auth
* accounts
* doctors

---

### DATABASES

Defines the database configuration.

Currently:

SQLite

Later:

MySQL

---

## Why is settings.py separated?

To keep application configuration independent from business logic.

This follows the **Separation of Concerns (SoC)** principle.

---

## Interview Questions

### What is DEBUG?

DEBUG determines whether Django runs in development mode or production mode.

---

### Why should DEBUG be False in production?

Because detailed error pages can expose sensitive application information.

---

### What is settings.py?

The central configuration file of a Django project.

---

## My Questions

### Why does Django separate settings.py and urls.py?

Answer:

`settings.py` stores project configuration such as database settings, installed apps, middleware, and security settings.

`urls.py` handles URL routing by mapping incoming requests to the appropriate views.

Separating them follows the **Separation of Concerns (SoC)** principle, making the project easier to maintain and scale.
