#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

model = joblib.load("lab1/best_model.pkl")

app = FastAPI()

class ModelInput(BaseModel):
    feature1: float
    feature2: float
   

@app.get("/")
def home():
    logger.info("Home endpoint hit")
    return {"message": "Welcome to the model API!"}

@app.get("/health")
def health():
    logger.info("Health check endpoint hit")
    return {"status": "OK"}

@app.post("/predict")
def predict(data: ModelInput):
    logger.info(f"Prediction request: {data}")
    features = [[data.feature1, data.feature2]]  
    prediction = model.predict(features)
    logger.info(f"Prediction result: {prediction}")
    return {"prediction": prediction[0]}

