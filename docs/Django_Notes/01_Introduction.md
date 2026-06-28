# Django Notes - Chapter 1

# Introduction to Django

## What is Django?

Django is a high-level Python web framework used to build secure, scalable, and maintainable web applications quickly.

It follows the **MVT (Model-View-Template)** architecture and provides many built-in features such as authentication, database ORM, admin panel, security, and URL routing.

---

## Why Django?

Instead of building everything from scratch, Django provides ready-made components for common web development tasks.

Examples:

* Authentication
* Admin Panel
* ORM (Database)
* URL Routing
* Middleware
* Session Management
* Security
* Form Handling

This allows developers to focus on solving business problems instead of writing boilerplate code.

---

## Why are we using Django for LifeLink AI?

LifeLink AI requires:

* User Registration
* Login
* Doctor Management
* Hospital Management
* Appointment Booking
* Reviews
* REST APIs
* AI Integration
* Emergency SOS

Django is well suited because it provides a strong backend foundation for all these features.

---

## Django Request Flow

Browser

↓

URL

↓

View

↓

Model

↓

Database

↓

Response

↓

Browser

Every request in Django follows this lifecycle.

---

## Project Goal

We are not learning Django to create demo applications.

We are learning Django while building an AI-powered Healthcare & Emergency Response Platform called **LifeLink AI**.

---

## Interview Questions

### What is Django?

Django is a high-level Python web framework that helps developers build secure, scalable, and maintainable web applications quickly.

---

### What are the advantages of Django?

* Fast development
* Built-in authentication
* ORM support
* Admin Panel
* Secure by default
* Scalable
* Large community support

---

### What architecture does Django follow?

Django follows the **MVT (Model-View-Template)** architecture.

---

## My Questions

### Why are we learning Django instead of Flask?

Answer:

LifeLink AI is a large application containing authentication, database integration, admin panel, REST APIs, AI modules, and future scalability requirements. Django provides many built-in features that reduce development effort and help maintain a structured architecture.
