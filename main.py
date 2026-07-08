from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import uvicorn

app = FastAPI(title="Student Grade Tracker")

# Allow frontend to talk to the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# This is our "database" for now (just a dictionary in memory)
students = {}
next_id = 1

# This defines what a student looks like
class Student(BaseModel):
    name: str
    subject: str
    grades: List[float]

def calculate_gpa(grades: List[float]) -> float:
    if not grades:
        return 0.0
    average = sum(grades) / len(grades)
    return round(average, 2)

# GET all students
@app.get("/students")
def get_all_students():
    return list(students.values())

# POST - add a new student
@app.post("/students")
def add_student(student: Student):
    global next_id
    gpa = calculate_gpa(student.grades)
    student_data = {
        "id": next_id,
        "name": student.name,
        "subject": student.subject,
        "grades": student.grades,
        "gpa": gpa
    }
    students[next_id] = student_data
    next_id += 1
    return student_data

# GET one student by ID
@app.get("/students/{student_id}")
def get_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    return students[student_id]

# DELETE a student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="Student not found")
    deleted = students.pop(student_id)
    return {"message": f"Student {deleted['name']} deleted successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)