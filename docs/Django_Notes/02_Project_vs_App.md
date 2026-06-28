# Django Notes - Chapter 2

# Django Project vs Django App

## What is a Django Project?

A Django Project is the complete web application.

Example:

LifeLink AI

The project contains:

* Settings
* URLs
* Apps
* Database Configuration
* Middleware
* Authentication Configuration

Think of it as the entire hospital.

---

## What is a Django App?

A Django App is a module responsible for one specific functionality.

Examples in LifeLink AI:

accounts

patients

doctors

hospitals

appointments

reviews

emergency

Each app has its own:

* Models
* Views
* URLs
* Admin
* Tests

---

## Hospital Analogy

Hospital

↓

Departments

Cardiology

Orthopedics

Emergency

Similarly

LifeLink AI Project

↓

Apps

Accounts

Patients

Doctors

Hospitals

Appointments

---

## Why create multiple apps?

Advantages:

* Easy maintenance
* Reusable code
* Better project organization
* Team collaboration
* Easier testing

---

## Interview Questions

### Difference between Project and App?

Project:

Entire web application.

App:

One functional module inside the project.

---

### Can one project contain multiple apps?

Yes.

A Django project can contain multiple apps, and each app handles one business functionality.

---

## My Questions

### Why shouldn't we put everything inside one app?

Answer:

Because as the application grows, a single app becomes difficult to maintain.

Separating features into different apps follows the **Single Responsibility Principle (SRP)** and improves scalability and code organization.
