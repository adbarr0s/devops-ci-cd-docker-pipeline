
from fastapi import FastAPI

app = FastAPI(
    title="DevOps CI/CD Demo",
    version="1.0.0",
    description="Simple FastAPI app to demonstrate CI/CD with Docker and GitHub Actions.",
)
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello Adrix!"}

@app.get("/health")
def health():
    return {"status": "ok"}
