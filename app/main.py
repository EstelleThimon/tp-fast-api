from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, CI world!"}


@app.get("/square/{number}")
def square(number: int):
    return {"number": number, "square": number * number}