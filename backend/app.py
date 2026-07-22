from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import gdown
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

# Create FastAPI application
app = FastAPI()

#Add CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to the trained model
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "crop_yield_model.pkl"

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

