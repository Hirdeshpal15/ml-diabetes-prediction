import joblib
from preprocess import load_and_preprocess_data, preprocess_input

# 1. Load model
model = joblib.load("model/model.joblib")

# 2. Get training columns
X, _ = load_and_preprocess_data()
reference_columns = X.columns

# 3. Raw user input
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

# 4. Preprocess input
processed_input = preprocess_input(input_data, reference_columns)

# 5. Predict
prediction = model.predict(processed_input)

print("Prediction:", prediction)

if prediction[0] == 1:
    print("Diabetes: YES")
else:
    print("Diabetes: NO")