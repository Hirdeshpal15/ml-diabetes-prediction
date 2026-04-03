from preprocess import load_and_preprocess_data

X, y = load_and_preprocess_data()

print("X shape:", X.shape)
print("y shape:", y.shape)
print("Columns:", X.columns)