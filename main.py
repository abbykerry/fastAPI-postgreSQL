from fastapi import FastAPI
from pydantic import BaseModel, Field
from database import engine, Base
import models

Base.metadata.create_all(bind=engine)

app = FastAPI()

# This is Pydantic (our "gatekeeper")
class Farmer(BaseModel):
    full_name: str = Field(..., min_length=3) # The "..." means this field is required
    phone_number: str = Field(..., min_length=10, max_length=13)
    cluster: str | None = None # Optional field, can be None


@app.get("/")
def read_root():
    return {"message": "Hello farmers!"}


@app.post("/farmers")
def create_farmer(farmer: Farmer):
    return {
        "message": "Farmer created successfully",
        "data": farmer
    }