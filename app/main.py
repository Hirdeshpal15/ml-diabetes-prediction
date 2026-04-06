from fastapi import FastAPI
from pydantic import BaseModel
import joblib

from src.preprocess import load_and_preprocess_data, preprocess_input

app = FastAPI()


# Define input schema
class InputData(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: str
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int


# Load model
model = joblib.load("model/model.joblib")

# Reference columns
X, _ = load_and_preprocess_data()
reference_columns = X.columns


@app.get("/")
def home():
    return {"message": "CI/CD Updated API"}


@app.post("/predict")
def predict(data: InputData):
    """
    What it does:
    Takes validated input and returns prediction

    Why:
    Prevents bad input from breaking system
    """

    # Convert to dict
    input_dict = data.dict()

    # Preprocess
    processed_input = preprocess_input(input_dict, reference_columns)

    # Predict
    prediction = model.predict(processed_input)

    return {
        "prediction": int(prediction[0]),
        "diabetes": "YES" if prediction[0] == 1 else "NO"
    }