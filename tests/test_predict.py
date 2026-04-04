import joblib

from src.preprocess import load_and_preprocess_data, preprocess_input


def test_prediction():
    # Load model
    model = joblib.load("model/model.joblib")

    # Get reference columns
    X, _ = load_and_preprocess_data()
    reference_columns = X.columns

    # Sample input
    input_data = {
        "gender": "Male",
        "age": 50,
        "hypertension": 0,
        "heart_disease": 0,
        "smoking_history": "never",
        "bmi": 25.0,
        "HbA1c_level": 5.5,
        "blood_glucose_level": 120
    }

    # Preprocess
    processed_input = preprocess_input(input_data, reference_columns)

    # Predict
    prediction = model.predict(processed_input)

    # Assert
    assert prediction[0] in [0, 1]