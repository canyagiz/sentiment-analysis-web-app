
```markdown
# 🧠 Real-Time Sentiment Analysis with MLOps

This project demonstrates a full end-to-end MLOps pipeline for real-time sentiment analysis. It takes a text input (like a tweet) and classifies its sentiment as **positive** or **negative** using a machine learning model deployed in the cloud.

The backend is built with **FastAPI**, containerized using **Docker**, deployed to **Google Kubernetes Engine (GKE)**, and served to users via a **Streamlit** web interface.

![image](https://github.com/user-attachments/assets/0d2ea312-2588-49a1-abd2-6683a92b7030)

---

## 🚀 Key Features

- Preprocessing and cleaning of real-world text data
- Training with TF-IDF and Logistic Regression
- Model served via a FastAPI REST API
- Containerization with Docker
- Deployment on GKE with Kubernetes
- Interactive web UI built with Streamlit
- Optional CI/CD integration via GitHub Actions

---

## 🗂️ Project Structure

```
sentiment-mlops/
│
├── data/                  # Dataset & preprocessing scripts
│   └── prepare_data.py
│
├── training/              # Model training & evaluation
│   ├── train.py
│   └── evaluate.py
│
├── models/                # Trained model & vectorizer (pkl files)
│
├── app/                   # FastAPI backend
│   ├── main.py
│   ├── model.py
│   └── utils.py
│
├── frontend/              # Streamlit frontend
│   ├── app_ui.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── notebooks/             # Exploratory data analysis
│   └── EDA.ipynb
│
├── Dockerfile             # Backend Dockerfile
├── build.yaml             # Kubernetes deployment manifest (backend)
├── k8s-frontend.yaml      # Kubernetes deployment manifest (frontend)
├── requirements.txt       # Backend dependencies
└── README.md              # Project documentation
```

---

## 📊 Dataset

- **Source**: [Sentiment140 Dataset](https://www.kaggle.com/kazanova/sentiment140)
- **Classes**:
  - `0`: Negative
  - `4`: Positive
- **Cleaning Steps**:
  - Remove neutral labels
  - Clean URLs, mentions, emojis, punctuation
  - Lowercase conversion

---

## 🧠 Model

- **Vectorizer**: TF-IDF
- **Classifier**: Logistic Regression
- **Saved Artifacts**:
  - `sentiment_model.pkl`
  - `tfidf_vectorizer.pkl`

---

## 🌐 Backend API (FastAPI)

| Endpoint   | Method | Description                 |
|------------|--------|-----------------------------|
| `/predict` | POST   | Returns predicted sentiment |
| `/health`  | GET    | Health check endpoint       |

Example request:
```json
POST /predict
{
  "text": "I love this!"
}
```

Response:
```json
{
  "sentiment": "positive"
}
```

---

## 🖥️ Frontend (Streamlit)

A clean web interface where users can:

- Enter custom text
- Click "Predict"
- See the real-time sentiment result

To run locally:

```bash
streamlit run frontend/app_ui.py
```

---

## 🐳 Docker Usage

### Backend:

```bash
docker build -t sentiment-api .
docker run -p 8000:8000 sentiment-api
```

### Frontend:

```bash
cd frontend
docker build -t sentiment-frontend .
docker run -p 8501:8501 sentiment-frontend
```

---

## ☸️ Deployment on Google Kubernetes Engine (GKE)

1. **Push Docker images** to Google Container Registry (GCR):
```bash
docker tag sentiment-api gcr.io/<project-id>/sentiment-api
docker push gcr.io/<project-id>/sentiment-api
```

2. **Deploy with Kubernetes:**
```bash
kubectl apply -f build.yaml           # Backend
kubectl apply -f k8s-frontend.yaml    # Frontend
```

3. **Access the services** via the external IPs from:
```bash
kubectl get services
```

---

## 📈 Optional Enhancements

- Monitoring with Prometheus & Grafana
- Logging with Google Cloud Logging
- CI/CD with GitHub Actions

---

## ✅ What You'll Learn

| Area             | Skills Gained                          |
|------------------|----------------------------------------|
| Machine Learning | Preprocessing, modeling, evaluation    |
| API Development  | FastAPI + RESTful endpoints            |
| Cloud Deployment | Docker, Kubernetes, GKE, GCR           |
| MLOps Practices  | Modularity, reproducibility, CI/CD     |
| Frontend         | Streamlit web interface                |

---

## 👨‍💻 Author

**Ali Yağız Canigüroğlu**  
[LinkedIn](https://linkedin.com/in/your-profile) | [GitHub](https://github.com/your-username)

---

## 📄 License

This project is licensed under the MIT License.
```

---

Let me know if you want a PDF version or you'd like to publish this to GitHub and need help writing a clean `commit`/`push` process for it!
