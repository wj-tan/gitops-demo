from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the GitOps Backend API"}

@app.get("/hello")
def say_hello(name: str = "World"):
    return {"message": f"Hello, {name}!"}
