# Secure-File-Sharing-System
Overview
This project implements a secure file-sharing system using Django, a high-level Python web framework, and the Django REST framework for building RESTful APIs. The system facilitates file sharing between two types of users: Operations Users (Ops Users) and Client Users. Ops Users are responsible for tasks such as uploading files, while Client Users can sign up, verify their email, log in, download files, and view a list of uploaded files.

Key Features
User Authentication: The system supports user authentication for Ops Users and Client Users.
File Upload: Ops Users can securely upload files, with restrictions on file types (limited to pptx, docx, and xlsx).
Email Verification: Client Users undergo email verification upon signing up to enhance security.
File Download: Client Users can securely download files using encrypted URLs generated by the system.
File Listing: Client Users can view a list of uploaded files.

Technologies Used
Django: A high-level Python web framework.
Django REST framework: A powerful and flexible toolkit for building Web APIs in Django.
SQLite: A lightweight and easy-to-use relational database.

Project Structure
File Sharing App: Contains models, views, serializers, and permissions for user profiles and file management.
User Authentication: Utilizes Django's built-in authentication system.
API Endpoints: Implements RESTful APIs for user actions and file operations.

Usage
Ops User Actions:

Login to access privileged actions.
Upload files with restricted formats.
Client User Actions:

Sign up to create an account.
Verify email for added security.
Log in to access user-specific features.
Download files using secure, encrypted URLs.
View a list of uploaded files.

How to Run
Clone the repository.
Install the required dependencies: pip install -r requirements.txt.
Run migrations: python manage.py migrate.
Start the development server: python manage.py runserver.
Access the application at http://127.0.0.1:8000/ in your web browser.
