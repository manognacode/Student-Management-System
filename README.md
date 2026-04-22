#  Student Management System

##  Project Overview

This is a simple full-stack web application that allows users to manage student records. The system supports basic CRUD operations (Create, Read, Update, Delete) using a Python Flask backend, SQLite database, and a frontend built with HTML and JavaScript.

---

##  Features

* Add new student details
* View all students
* Delete student records
* Real-time data update using API calls

---

##  Tech Stack

* **Frontend:** HTML, JavaScript
* **Backend:** Python (Flask)
* **Database:** SQLite

---

##  API Endpoints

* `GET /students` → Fetch all students
* `POST /add` → Add a new student
* `DELETE /delete/<id>` → Delete a student

---

##  How It Works

1. User enters student details in the frontend
2. JavaScript sends a request to the Flask backend
3. Backend processes the request and interacts with the database
4. Data is stored/retrieved from SQLite
5. Frontend updates dynamically based on API response

---

##  How to Run the Project

1. Install dependencies:

   ```
   pip install flask flask-cors
   ```
2. Run the backend:

   ```
   python app.py
   ```
3. Open `index.html` in your browser

---

##  What I Learned

* Building REST APIs using Flask
* Performing CRUD operations with a database
* Connecting frontend and backend using JavaScript fetch API
* Handling JSON data and dynamic UI updates

---

##  Future Improvements

* Add update functionality
* Add form validation
* Improve UI with CSS
* Add authentication system

---

##  Author
Mooli Sai Manogna

