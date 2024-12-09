from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def fast_first():
    return "First try fastAPI"