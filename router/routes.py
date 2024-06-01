from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from models import Student as DBStudent

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class OurBaseModel(BaseModel):
    class Config:
        from_attributes = True

class Student(OurBaseModel):
    id: int
    name: str
    city: str

class StudentCreate(OurBaseModel):
    name: str
    city: str

class StudentUpdate(OurBaseModel):
    name: str
    city: str

@app.get("/", response_model=List[Student], status_code=status.HTTP_200_OK)
def read_students(db: Session = Depends(get_db)):
    students = db.query(DBStudent).all()
    return students

@app.post("/create_student/", response_model=Student, status_code=status.HTTP_201_CREATED)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    new_student = DBStudent(name=student.name, city=student.city)
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student

@app.put("/update_student/{student_id}", response_model=Student, status_code=status.HTTP_200_OK)
def update_student(student_id: int, student_update: StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")

    student.name = student_update.name
    student.city = student_update.city
    db.commit()
    db.refresh(student)
    return student

@app.delete("/delete_student/{student_id}", status_code=status.HTTP_200_OK)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(DBStudent).filter(DBStudent.id == student_id).first()
    if student is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
    db.delete(student)
    db.commit()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"detail": "Student Deleted!"})