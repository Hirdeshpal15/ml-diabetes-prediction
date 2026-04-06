from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import logging

from src.preprocess import load_and_preprocess_data, preprocess_input

# -------------------------------
# Logging setup
# -------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()


# -------------------------------
# Input Schema
# -------------------------------
class InputData(BaseModel):
    gender: str
    age: float
    hypertension: int
    heart_disease: int
    smoking_history: str
    bmi: float
    HbA1c_level: float
    blood_glucose_level: int


# -------------------------------
# Load model safely
# -------------------------------
try:
    model = joblib.load("model/model.joblib")
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None


# -------------------------------
# Load reference columns
# -------------------------------
try:
    X, _ = load_and_preprocess_data()
    reference_columns = X.columns
    logger.info("Reference data loaded")
except Exception as e:
    logger.error(f"Error loading reference data: {e}")
    reference_columns = None


# -------------------------------
# Routes
# -------------------------------
@app.get("/")
def home():
    return {"message": "CI/CD Updated API 🚀"}


@app.post("/predict")
def predict(data: InputData):
    try:
        logger.info(f"Received input: {data}")

        if model is None:
            raise HTTPException(status_code=500, detail="Model not loaded")

        if reference_columns is None:
            raise HTTPException(status_code=500, detail="Reference data not loaded")

        # Convert input
        input_dict = data.dict()

        # Preprocess
        processed_input = preprocess_input(input_dict, reference_columns)

        # Predict
        prediction = model.predict(processed_input)[0]

        logger.info(f"Prediction result: {prediction}")

        return {
            "prediction": int(prediction),
            "diabetes": "YES" if prediction == 1 else "NO"
        }

    except HTTPException as e:
        raise e

    except Exception as e:
        logger.error(f"Prediction error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")