# 🩺 Diabetes Prediction ML System

## 🚀 Project Overview

This project is an end-to-end Machine Learning system that predicts whether a person has diabetes based on health metrics.

It includes:

- Machine Learning model (scikit-learn)
- FastAPI backend deployed on Azure
- Streamlit frontend deployed on cloud
- CI/CD pipeline using GitHub Actions
- Docker for containerization

---

## 🌐 Live Demo

- 🔗 Frontend: https://ml-diabetes-prediction-qvp5zrpzmtwj5mf6gavlm3.streamlit.app
- 🔗 API: https://ml-diabetes-api-hirdesh-d8gdc3f0e0a8hza4.germanywestcentral-01.azurewebsites.net

---

## 🧠 Features

- Predict diabetes using health data
- Input validation using Pydantic
- Error handling and logging
- Real-time predictions via API
- Fully automated CI/CD pipeline

---

## 🏗️ Architecture

User → Streamlit UI → FastAPI (Azure) → ML Model

---

## ⚙️ Tech Stack

- Python
- scikit-learn
- FastAPI
- Streamlit
- Docker
- GitHub Actions (CI/CD)
- Microsoft Azure

---

## 📦 How to Run Locally

```bash
# Clone repo
git clone <your-repo-url>

# Install dependencies
pip install -r requirements.txt

# Train model
python src/train_pipeline.py

# Run API
uvicorn app.main:app --reload

# Run frontend
streamlit run frontend.py
```

---

## 🐳 Docker

```bash
docker build -t ml-api .
docker run -p 8000:8000 ml-api
```

---

## 🔄 CI/CD

- Automatically runs tests
- Builds Docker image
- Pushes to Docker Hub
- Updates deployment

---

## 📊 Future Improvements

- Model versioning
- Monitoring dashboards
- UI improvements

---

## 👨‍💻 Author

Hirdesh Pal
