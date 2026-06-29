# Security Design Notes – User Authentication & Authorization

## 1. Secure Authentication

The application should use secure authentication mechanisms.

Possible implementations:

* JWT (JSON Web Token)
* OAuth 2.0 (Future integration with Google, Microsoft, etc.)

Authentication tokens should:

* Have an expiration time.
* Be signed securely.
* Be transmitted only over HTTPS.
* Be invalidated on logout where applicable.

---

## 2. Role-Based Access Control (RBAC)

Every authenticated user should have a predefined role.

Examples:

* Patient
* Doctor
* Hospital Admin
* Ambulance Staff
* System Administrator

Each role should only have access to authorized resources.

Examples:

Patient

* View own profile
* Book appointments
* View prescriptions

Doctor

* View assigned patients
* Update consultation records
* Manage availability

Admin

* Manage users
* Verify doctors
* Verify hospitals
* View analytics

Patients must never have access to administrator functionality.

---

## 3. Strong Password Policy

Passwords should meet minimum security requirements.

Recommended rules:

* Minimum length: 12 characters
* At least one uppercase letter
* At least one lowercase letter
* At least one number
* At least one special character

Passwords should not contain:

* User's name
* Email address
* Date of birth
* Phone number
* Common dictionary words

Passwords should always be stored as hashes using Django's built-in password hashing.

---

## 4. Authorization Checks

Every protected API should verify:

* User authentication
* User role
* Resource ownership

Example:

A patient should only access their own medical records.

A doctor should only access patients assigned to them (or according to the application's authorization rules).

---

## 5. Future Security Enhancements

* Multi-Factor Authentication (MFA)
* Login attempt rate limiting
* Account lockout after repeated failed logins
* Session timeout
* Device recognition
* Audit logging
* Security monitoring


JWT: Used to authenticate users inside your own application.
OAuth: Used when users log in using another service.
Example:Login with Google, Login with Microsoft or Login with Apple

Many applications use OAuth to log in and JWT to communicate with their own backend after login.