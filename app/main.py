
from fastapi import FastAPI

app = FastAPI(
    title="DevOps CI/CD Demo",
    version="1.0.0",
    description="Simple FastAPI app to demonstrate CI/CD with Docker and GitHub Actions.",
)


@app.get("/")
def home():
    return {"message": "Hello from DevOps CI/CD Pipeline!"}


@app.get("/health")
def health():
    return {"status": "ok"}
