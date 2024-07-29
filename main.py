# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 15:57:37 2024

@author: dhana
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

class Model_Input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
diabetes_model = pickle.load(open('Diabetes_model.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_params : Model_Input):
    
    inp_data = input_params.json()
    inp_dict = json.loads(inp_data)
    
    preg = inp_dict['Pregnancies']
    glu = inp_dict['Glucose']
    bp = inp_dict['BloodPressure']
    st = inp_dict['SkinThickness']
    ins = inp_dict['Insulin']
    bmi = inp_dict['BMI']
    dpf = inp_dict['DiabetesPedigreeFunction']
    age = inp_dict['Age']
    
    inp_list = [preg, glu, bp, st, ins, bmi, dpf, age]
    
    prediction = diabetes_model.predict([inp_list])
    
    if prediction[0]==0:
        return 'The person is not Diabetic'
    else:
        return 'The Person is Diabetic'
    
    
    
    
    
    
    