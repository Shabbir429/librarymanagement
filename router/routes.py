from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from sqlalchemy.orm import Session
from typing import List
from database import SessionLocal
from models import Student as DBStudent

app = FastAPI()

# Dependency to get the database session


