import pandas as pd

CATEGORICAL_COLUMNS = ["gender", "smoking_history"]


def load_data():
    return pd.read_csv("data/diabetes_prediction_dataset.csv")


def preprocess_data(df):
    df = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS)
    return df


def get_feature_target(df):
    X = df.drop("diabetes", axis=1)
    y = df["diabetes"]
    return X, y


# THIS FUNCTION MUST EXIST
def load_and_preprocess_data():
    df = load_data()
    df = preprocess_data(df)
    return get_feature_target(df)


# NEW FUNCTION (for prediction)
def preprocess_input(input_dict, reference_columns):
    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df, columns=CATEGORICAL_COLUMNS)

    for col in reference_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[reference_columns]

    return df