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

