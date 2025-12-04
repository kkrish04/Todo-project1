from fastapi import FastAPI

app = FastAPI()

todos = []

@app.post("/add")
def add(item: str):
    todos.append(item)
    return {"message": "Added"}