import streamlit as st 
import joblib
from fastapi import FastAPI, HTTPException

# Load the model
diabetes_clf = joblib.load(open('./models/diabetes_detector_model.pkl','rb'))

# Initialize an instance of FastAPI
app = FastAPI()

# Define the default route 
@app.get("/")
def root():
    return {"message": "Welcome to Diabetes Classification FastAPI"}

# Define the route to the sentiment predictor
# inputs = [pregnancy,glucose,blood,skin,insulin,float(bmi), float(pedigree),age]
@app.post("/predict_diabetes")
def predict_diabetes(inputs:list): #given format : [[6,148,72,35,0,33.6,0.627,50]] 

    polarity = ""

    if(not(inputs)):
        raise HTTPException(status_code=400, 
                            detail = "Please Provide a valid inputs")

    prediction = diabetes_clf.predict(inputs)

    if(prediction[0] == 0):
        polarity = 'You don\'t have diabetes!'

    elif(prediction[0] == 1):
        polarity =  'Unfortunately you have diabetes!'
        
    return {
            "text_message": inputs, 
            "diabetes_polarity": polarity
           }
