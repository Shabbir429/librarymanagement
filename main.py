from fastapi import FastAPI
from router import routes

app = FastAPI()

app.include_router(routes.app)