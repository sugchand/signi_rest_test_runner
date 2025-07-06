# sample_api/main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def hello():
    return {"message": "Hello from API"}

@app.get("/status")
def status():
    return {"status": "API is healthy"}
