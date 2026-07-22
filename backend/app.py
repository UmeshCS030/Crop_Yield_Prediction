from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from pathlib import Path

# Create FastAPI application
app = FastAPI()

# Path to the trained model
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "crop_yield_model.pkl"

# Load the trained model
model = joblib.load(MODEL_PATH)

#Create the input Model
class CropInput(BaseModel):
    Area: str
    Item: str
    Year: int
    average_rain_fall_mm_per_year: float
    pesticides_tonnes: float
    avg_temp: float

@app.get("/")
def home():
    return {
        "message": "Crop Yield Prediction API is running successfully!"
    }

@app.get("/model-info")
def model_info():
    return {
        "message": "Model loaded successfully!",
        "model_type": str(type(model))
    }


@app.post("/predict")
def predict(data: CropInput):

    #Convert the Input into a Pandas DataFrame
    input_df = pd.DataFrame([data.model_dump()])

    #Call model.predict()
    prediction = model.predict(input_df)

    
    #Return the Prediction as JSON
    return {
        "predicted_yield": float(prediction[0])
    }

