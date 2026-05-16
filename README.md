<<<<<<< HEAD
# Diabetic Retinopathy Detection System

A Deep Learning system to classify retinal fundus images into 5 stages of Diabetic Retinopathy (DR) using Transfer Learning (ResNet50).

## Features
- **Deep Learning Model**: ResNet50 pre-trained on ImageNet, fine-tuned for 5-class DR classification.
- **Preprocessing**: Automatic circular cropping to remove black borders, resizing, and normalization.
- **API**: FastAPI backend for model inference.
- **UI**: Streamlit web interface for easy image upload and analysis.

## Project Structure
```
Diabetic Retinopathy Detection/
│
├── data/                 # Data directory
├── preprocessing/        # Image processing logic
│   └── preprocess.py
├── training/             # Model training scripts
│   └── train_model.py
├── models/               # Saved models
│   └── dr_model.h5
├── inference/            # Prediction logic
│   └── predict.py
├── api/                  # FastAPI backend
│   └── app.py
├── ui/                   # Streamlit Frontend
│   └── streamlit_app.py
└── requirements.txt
```

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Train Model** (Demo Mode):
    ```bash
    python training/train_model.py
    ```
    *Note: This runs on dummy data for demonstration. For real results, integrate the Kaggle APTOS dataset.*

## Running the Application

### Option 1: Streamlit UI
Interactive web app.
```bash
streamlit run ui/streamlit_app.py
```

### Option 2: FastAPI Backend
REST API.
```bash
uvicorn api.app:app --reload
```
API Documentation available at `http://localhost:8000/docs`.
=======
# Diabetic Retinopathy Detection System

A Deep Learning system to classify retinal fundus images into 5 stages of Diabetic Retinopathy (DR) using Transfer Learning (ResNet50).

## Features
- **Deep Learning Model**: ResNet50 pre-trained on ImageNet, fine-tuned for 5-class DR classification.
- **Preprocessing**: Automatic circular cropping to remove black borders, resizing, and normalization.
- **API**: FastAPI backend for model inference.
- **UI**: Streamlit web interface for easy image upload and analysis.

## Project Structure
```
Diabetic Retinopathy Detection/
│
├── data/                 # Data directory
├── preprocessing/        # Image processing logic
│   └── preprocess.py
├── training/             # Model training scripts
│   └── train_model.py
├── models/               # Saved models
│   └── dr_model.h5
├── inference/            # Prediction logic
│   └── predict.py
├── api/                  # FastAPI backend
│   └── app.py
├── ui/                   # Streamlit Frontend
│   └── streamlit_app.py
└── requirements.txt
```

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Train Model** (Demo Mode):
    ```bash
    python training/train_model.py
    ```
    *Note: This runs on dummy data for demonstration. For real results, integrate the Kaggle APTOS dataset.*

## Running the Application

### Option 1: Streamlit UI
Interactive web app.
```bash
streamlit run ui/streamlit_app.py
```

### Option 2: FastAPI Backend
REST API.
```bash
uvicorn api.app:app --reload
```
API Documentation available at `http://localhost:8000/docs`.
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
