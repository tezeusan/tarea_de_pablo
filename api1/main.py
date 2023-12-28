from fastapi import FastAPI

app = FastAPI()


@app.get("/add/{x}/{y}")
def add(x: int, y: int):
    return {"result": x + y}


@app.get("/subtract/{x}/{y}")
def subtract(x: int, y: int):
    return {"result": x - y}


@app.get("/multiply/{x}/{y}")
def multiply(x: int, y: int):
    return {"result": x * y}


@app.get("/divide/{x}/{y}")
def divide(x: int, y: int):
    if y == 0:
        return {"error": "Cannot divide by zero"}
    return {"result": x / y}
