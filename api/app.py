<<<<<<< HEAD
from fastapi import FastAPI, File, UploadFile
import shutil
import os
import sys

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inference.predict import DRPredictor

app = FastAPI(title="Diabetic Retinopathy Detection API")

# Initialize model once
try:
    predictor = DRPredictor()
except Exception as e:
    print(f"Warning: Model could not be loaded: {e}")
    predictor = None

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if predictor is None:
        return {"error": "Model not loaded. Train the model first."}

    # Save temp file
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        stage, probability = predictor.predict(temp_file)
        result = {
            "filename": file.filename,
            "stage": stage,
            "probability": probability
        }
    finally:
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
    return result
=======
from fastapi import FastAPI, File, UploadFile
import shutil
import os
import sys

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from inference.predict import DRPredictor

app = FastAPI(title="Diabetic Retinopathy Detection API")

# Initialize model once
try:
    predictor = DRPredictor()
except Exception as e:
    print(f"Warning: Model could not be loaded: {e}")
    predictor = None

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if predictor is None:
        return {"error": "Model not loaded. Train the model first."}

    # Save temp file
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        stage, probability = predictor.predict(temp_file)
        result = {
            "filename": file.filename,
            "stage": stage,
            "probability": probability
        }
    finally:
        # Cleanup
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
    return result
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
