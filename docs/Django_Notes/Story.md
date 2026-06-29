Test Case
Title: Modify Session Cookie
Steps
Login.
Open Developer Tools.
Modify session cookie.
Refresh the page.
Expected Result
Django should detect that the cookie has been modified.
Session should become invalid.
User should be redirected to the login page or receive an unauthorized response.