from fastapi import FastAPI
from app.database import engine, Base
import app.Models
from app.Routers import enrollment

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Course Registration System",
    version="1.0.0"
)

app.include_router(enrollment.router)

@app.get("/")
def root():
    return {"status": "healthy"}