<<<<<<< HEAD
import cv2
import numpy as np
import os
import sys

# Add root
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from inference.predict import DRPredictor

def create_dummy_image():
    # Create a random image (simulate fundus)
    dummy_img = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)
    # Draw a circle (fundus-like)
    cv2.circle(dummy_img, (250, 250), 200, (100, 50, 50), -1)
    cv2.imwrite("test_dummy.jpg", dummy_img)
    return "test_dummy.jpg"

def test_inference():
    print("Testing DR Inference...")
    
    img_path = create_dummy_image()
    
    try:
        predictor = DRPredictor()
        stage, prob = predictor.predict(img_path)
        
        print(f"Prediction: {stage}")
        print(f"Confidence: {prob:.4f}")
        
        if stage in ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]:
            print("SUCCESS: Valid Stage Predicted.")
        else:
            print(f"FAILED: Invalid Stage '{stage}'")
            
    except Exception as e:
        print(f"FAILED with Error: {e}")
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

if __name__ == "__main__":
    test_inference()
=======
import cv2
import numpy as np
import os
import sys

# Add root
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from inference.predict import DRPredictor

def create_dummy_image():
    # Create a random image (simulate fundus)
    dummy_img = np.random.randint(0, 255, (500, 500, 3), dtype=np.uint8)
    # Draw a circle (fundus-like)
    cv2.circle(dummy_img, (250, 250), 200, (100, 50, 50), -1)
    cv2.imwrite("test_dummy.jpg", dummy_img)
    return "test_dummy.jpg"

def test_inference():
    print("Testing DR Inference...")
    
    img_path = create_dummy_image()
    
    try:
        predictor = DRPredictor()
        stage, prob = predictor.predict(img_path)
        
        print(f"Prediction: {stage}")
        print(f"Confidence: {prob:.4f}")
        
        if stage in ["No DR", "Mild", "Moderate", "Severe", "Proliferative DR"]:
            print("SUCCESS: Valid Stage Predicted.")
        else:
            print(f"FAILED: Invalid Stage '{stage}'")
            
    except Exception as e:
        print(f"FAILED with Error: {e}")
    finally:
        if os.path.exists(img_path):
            os.remove(img_path)

if __name__ == "__main__":
    test_inference()
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
