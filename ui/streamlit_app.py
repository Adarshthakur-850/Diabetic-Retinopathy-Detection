<<<<<<< HEAD
import streamlit as st
import requests
import io
import os
import sys

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import predictor directly for easier standalone running (skip API dependency for demo)
from inference.predict import DRPredictor

st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon="👁️")

st.title("👁️ Diabetic Retinopathy AI")
st.write("Upload a Retinal Fundus Image to detect the stage of Diabetic Retinopathy.")

# Initializing Predictor Cache
@st.cache_resource
def load_predictor():
    return DRPredictor()

try:
    predictor = load_predictor()
    model_loaded = True
except Exception as e:
    st.error(f"Model not found. Please run `training/train_model.py` first.")
    model_loaded = False

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None and model_loaded:
    # Display Image
    st.image(uploaded_file, caption="Uploaded Fundus Image", use_column_width=True)
    
    if st.button("Analyze Image"):
        with st.spinner("Analyzing..."):
            # Save to temp
            with open("temp_upload.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            stage, confidence = predictor.predict("temp_upload.jpg")
            
            # Cleanup
            if os.path.exists("temp_upload.jpg"):
                os.remove("temp_upload.jpg")
            
            # Display Results
            st.success("Analysis Complete")
            st.metric(label="Predicted Stage", value=stage)
            st.metric(label="Confidence", value=f"{confidence:.2%}")
            
            # Progress bar for severity
            severity_map = {
                "No DR": 0,
                "Mild": 25,
                "Moderate": 50,
                "Severe": 75,
                "Proliferative DR": 100
            }
            score = severity_map.get(stage, 0)
            
            st.write("Severity Level:")
            st.progress(score)
            
            if score > 0:
                st.warning("⚠️ Medical attention recommended.")
            else:
                st.balloons()
=======
import streamlit as st
import requests
import io
import os
import sys

# Add project root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import predictor directly for easier standalone running (skip API dependency for demo)
from inference.predict import DRPredictor

st.set_page_config(page_title="Diabetic Retinopathy Detection", page_icon="👁️")

st.title("👁️ Diabetic Retinopathy AI")
st.write("Upload a Retinal Fundus Image to detect the stage of Diabetic Retinopathy.")

# Initializing Predictor Cache
@st.cache_resource
def load_predictor():
    return DRPredictor()

try:
    predictor = load_predictor()
    model_loaded = True
except Exception as e:
    st.error(f"Model not found. Please run `training/train_model.py` first.")
    model_loaded = False

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None and model_loaded:
    # Display Image
    st.image(uploaded_file, caption="Uploaded Fundus Image", use_column_width=True)
    
    if st.button("Analyze Image"):
        with st.spinner("Analyzing..."):
            # Save to temp
            with open("temp_upload.jpg", "wb") as f:
                f.write(uploaded_file.getbuffer())
            
            stage, confidence = predictor.predict("temp_upload.jpg")
            
            # Cleanup
            if os.path.exists("temp_upload.jpg"):
                os.remove("temp_upload.jpg")
            
            # Display Results
            st.success("Analysis Complete")
            st.metric(label="Predicted Stage", value=stage)
            st.metric(label="Confidence", value=f"{confidence:.2%}")
            
            # Progress bar for severity
            severity_map = {
                "No DR": 0,
                "Mild": 25,
                "Moderate": 50,
                "Severe": 75,
                "Proliferative DR": 100
            }
            score = severity_map.get(stage, 0)
            
            st.write("Severity Level:")
            st.progress(score)
            
            if score > 0:
                st.warning("⚠️ Medical attention recommended.")
            else:
                st.balloons()
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
