from enum import Enum
from fastapi import FastAPI, HTTPException  
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class Gender(Enum):
    male = "male"
    female = "female"

class Student(BaseModel):
    id: int
    name: str 
    age: int 
    gender: Gender 


students = [
    Student(id=1,name='haroon',age=20,gender=Gender.male),
    Student(id=2,name='ali',age=18,gender=Gender.male),
    Student(id=3,name='baker',age=29,gender=Gender.male),
    Student(id=4,name='user',age=27,gender=Gender.female),
    Student(id=5,name='ladu',age=25,gender=Gender.male),
    Student(id=6,name='ali',age=26,gender=Gender.male),
    Student(id=7,name='tayyab',age=22,gender=Gender.male),
    Student(id=8,name='bilal',age=23,gender=Gender.male),
    Student(id=9,name='user',age=24,gender=Gender.female),
    Student(id=10,name='ajy',age=90,gender=Gender.male),
]


@app.get("/")
def get():
    print("Fast Api ")
    return "Fast APi "


@app.get("/studant")
def get():
    print(students)
    return students


@app.get("/student/{student_id}")
def get(student_id: int):
    for student in students:
        if student.id == student_id:
            return student
    return {"error": "Student not found"}

@app.post("/student/")
async def create_student(student: Student ):
    students.append(student)
    return student

@app.delete("/student/{student_id}")
async def delete_student(student_id: int ):
     for student in students:
        if student.id == student_id:
            students.remove(delete_student)
        return {"Student Delete SucessFully"}


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student ):
    for student_to_update in students:
        if student_to_update.id == student_id:
            student_to_update.name = student.name
            student_to_update.age = student.age
            student_to_update.gender = student.gender
            return student_to_update

def start():
    uvicorn.run("tests.main:app", host="127.0.0.1", reload=True)
