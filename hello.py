'''
Date: 2026-03-12 20:22:55
'''
import os
import fastapi
app = fastapi.FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/")
def create_item(item: fastapi.HTTPException):
    return {"item": item}
