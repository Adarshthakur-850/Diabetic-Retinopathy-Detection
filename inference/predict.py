<<<<<<< HEAD
import tensorflow as tf
import numpy as np
import cv2
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing.preprocess import preprocess_image

MODEL_PATH = "models/dr_model.h5"
CLASSES = {
    0: "No DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferative DR"
}

class DRPredictor:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run training first.")
        print("Loading Validated Model...")
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def predict(self, image_path):
        processed_img = preprocess_image(image_path)
        if processed_img is None:
            return None, None

        # Add batch dimension
        img_batch = np.expand_dims(processed_img, axis=0)
        
        preds = self.model.predict(img_batch)
        class_idx = np.argmax(preds[0])
        confidence = float(preds[0][class_idx])
        
        return CLASSES[class_idx], confidence

if __name__ == "__main__":
    # Test
    predictor = DRPredictor()
    # Dummy file test if exists
    if os.path.exists("test_image.jpg"):
        stage, prob = predictor.predict("test_image.jpg")
        print(f"Prediction: {stage} ({prob:.2f})")
=======
import tensorflow as tf
import numpy as np
import cv2
import os
import sys

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from preprocessing.preprocess import preprocess_image

MODEL_PATH = "models/dr_model.h5"
CLASSES = {
    0: "No DR",
    1: "Mild",
    2: "Moderate",
    3: "Severe",
    4: "Proliferative DR"
}

class DRPredictor:
    def __init__(self):
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Run training first.")
        print("Loading Validated Model...")
        self.model = tf.keras.models.load_model(MODEL_PATH)

    def predict(self, image_path):
        processed_img = preprocess_image(image_path)
        if processed_img is None:
            return None, None

        # Add batch dimension
        img_batch = np.expand_dims(processed_img, axis=0)
        
        preds = self.model.predict(img_batch)
        class_idx = np.argmax(preds[0])
        confidence = float(preds[0][class_idx])
        
        return CLASSES[class_idx], confidence

if __name__ == "__main__":
    # Test
    predictor = DRPredictor()
    # Dummy file test if exists
    if os.path.exists("test_image.jpg"):
        stage, prob = predictor.predict("test_image.jpg")
        print(f"Prediction: {stage} ({prob:.2f})")
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
