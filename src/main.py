from sklearn.model_selection import train_test_split
import joblib
import os
os.makedirs("model", exist_ok=True)

from preprocess import load_and_preprocess_data
from model import get_model
from evaluate import evaluate_model


def main():
    print("Starting training pipeline...")

    # 1. Load data
    X, y = load_and_preprocess_data()

    # 2. Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # 3. Model
    model = get_model()

    # 4. Train
    model.fit(X_train, y_train)

    # 5. Predict
    y_pred = model.predict(X_test)

    # 6. Evaluate
    acc = evaluate_model(y_test, y_pred)
    print(f"Model Accuracy: {acc}")

    # 7. Save
    joblib.dump(model, "model/model.joblib")
    print("Model saved!")

    print("Pipeline finished!")


if __name__ == "__main__":
    main()