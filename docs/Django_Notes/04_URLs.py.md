# Django Notes - Chapter 4

# urls.py

## What is urls.py?

`urls.py` is responsible for routing incoming HTTP requests to the correct view.

Think of it as the application's receptionist.

---

## Request Flow

Browser

↓

URL

↓

urls.py

↓

View

↓

Response

---

## Example

```python
urlpatterns = [
    path("admin/", admin.site.urls),
]
```

When the user visits:

/admin/

Django opens the Admin Dashboard.

---

## Why use urls.py?

Instead of writing all application logic in one place, Django first determines **where** a request should go.

Examples:

/login

↓

Login View

/register

↓

Registration View

/doctors

↓

Doctor View

---

## Benefits

* Clean routing
* Easy maintenance
* Modular architecture
* Easy API versioning

---

## Interview Questions

### What is URL Routing?

URL Routing is the process of mapping a URL to the appropriate Django view.

---

### What is urlpatterns?

`urlpatterns` is a list containing URL patterns that Django checks when processing incoming requests.

---

## My Questions

### Why doesn't Django directly call views?

Answer:

Django first checks `urls.py` to determine which view should handle the request. This makes routing centralized and allows different URLs to point to different parts of the application.
