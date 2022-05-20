from fastapi import FastAPI
# use uvicorn main:app --reload in order to run

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World from Berkay"}

@app.get("/persons/me") # order is important to get without integer
async def read_user_me():
    return {"user_id": "the current user"}

@app.get("/persons/{person_id}")
async def read_person_id(person_id : int): # Data Conversion
    return {"person_id": person_id}

@app.get("/persons/name/{person_name}")
async def read_person_name(person_name):
    return {"person_name": person_name}