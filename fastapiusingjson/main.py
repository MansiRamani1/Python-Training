from fastapi import FastAPI


app=FastAPI()


@app.get("/first")
def index():
    return "hello world"