import pandas as pd

# Load dataset
df = pd.read_csv("data/diabetes_prediction_dataset.csv")

# Show first rows
print("First 5 rows:")
print(df.head())

# Basic info
print("\nDataset Info:")
print(df.info())

# Check missing values
print("\nMissing values:")
print(df.isnull().sum())