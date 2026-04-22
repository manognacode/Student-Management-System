from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Connect to SQLite (creates file automatically)
conn = sqlite3.connect("students.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT,
  age INTEGER,
  course TEXT
)
""")
conn.commit()

# CREATE
@app.route("/add", methods=["POST"])
def add_student():
    data = request.json
    cursor.execute(
        "INSERT INTO students(name, age, course) VALUES(?,?,?)",
        (data["name"], data["age"], data["course"])
    )
    conn.commit()
    return jsonify({"message": "Student added"})

# READ
@app.route("/students", methods=["GET"])
def get_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    result = []
    for r in rows:
        result.append({"id": r[0], "name": r[1], "age": r[2], "course": r[3]})
    return jsonify(result)

# DELETE
@app.route("/delete/<int:id>", methods=["DELETE"])
def delete_student(id):
    cursor.execute("DELETE FROM students WHERE id=?", (id,))
    conn.commit()
    return jsonify({"message": "Deleted"})

app.run(debug=True)
