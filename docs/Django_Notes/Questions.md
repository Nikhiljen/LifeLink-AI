# Why is settings.py separated?

To keep application configuration independent of business logic.

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


Q: What is the purpose of SECRET_KEY in Django?
Answer: SECRET_KEY is used by Django for cryptographic signing. 
It helps protect sessions, CSRF tokens, password reset tokens, and other security-sensitive data. 
It should remain secret and be stored securely, typically in environment variables rather than directly in the source code

Question: Why should every Django project have a unique SECRET_KEY?
Answer: Every Django project should use a unique SECRET_KEY because it is used for cryptographic signing 
of security-sensitive data such as sessions, CSRF tokens, and password reset tokens. Reusing a
key across projects increases security risk if the key is exposed. 
Each project should generate and protect its own secret key.

User Login ---> Session Created ---> Session Signed(Used Secret Key) ---> Browser Store Cookies ---> Browser Send Cookies
---> Django Verify Signed ---> Valid ----> Allow Or Reject

Q: Why must every Django app be added to INSTALLED_APPS?
A good answer: Every Django app must be registered in INSTALLED_APPS so that Django loads its models, 
admin configuration, migrations, signals, and other components during application startup. 
If the app is not registered, Django will not treat it as part of the project.

Q: What is the purpose of the request parameter in a Django view?
Answer: The request object represents the incoming HTTP request.
It contains information such as the HTTP method, headers, cookies, session data, authenticated user, 
query parameters, form data, JSON body, and uploaded files. 
Django automatically passes it to every view function so the application can process the client's request.

Q: Why do we use JsonResponse in Django?
Answer: JsonResponse converts Python dictionaries into JSON and creates a proper HTTP response with the correct 
Content-Type (application/json) and status code. 
It is commonly used for REST APIs because frontend applications can easily consume JSON data.

A Django view is a Python function (or class) that receives an HTTP request, 
executes the application's business logic, and returns an HTTP response.

Why do we use Models instead of writing SQL directly?
A strong answer would be:"Django models use the ORM, which allows developers to interact with the 
database using Python objects instead of writing raw SQL. This improves code readability, 
reduces the risk of SQL injection, makes the application database-independent, and simplifies maintenance."