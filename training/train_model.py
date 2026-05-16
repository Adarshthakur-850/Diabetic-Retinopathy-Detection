<<<<<<< HEAD
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
import os
import cv2

# Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 8
EPOCHS = 5
NUM_CLASSES = 5
MODEL_PATH = "models/dr_model.h5"

def build_model():
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(NUM_CLASSES, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Freeze lower layers
    for layer in base_model.layers:
        layer.trainable = False
        
    model.compile(optimizer=Adam(learning_rate=0.0001), 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

def generate_dummy_data(samples=100):
    """
    Generates dummy random images for testing the training logic 
    without the full Kaggle dataset.
    """
    print("Generating dummy data...")
    X = np.random.rand(samples, 224, 224, 3).astype(np.float32)
    y = np.random.randint(0, NUM_CLASSES, samples)
    return X, y

def train():
    if not os.path.exists("models"):
        os.makedirs("models")
        
    model = build_model()
    model.summary()
    
    # Use dummy data for demonstration if no real data loader is present
    X_train, y_train = generate_dummy_data(samples=50)
    X_val, y_val = generate_dummy_data(samples=10)
    
    print("Starting Training (Demo Mode)...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
=======
import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.optimizers import Adam
import numpy as np
import os
import cv2

# Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 8
EPOCHS = 5
NUM_CLASSES = 5
MODEL_PATH = "models/dr_model.h5"

def build_model():
    base_model = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    x = Dropout(0.5)(x)
    predictions = Dense(NUM_CLASSES, activation='softmax')(x)
    
    model = Model(inputs=base_model.input, outputs=predictions)
    
    # Freeze lower layers
    for layer in base_model.layers:
        layer.trainable = False
        
    model.compile(optimizer=Adam(learning_rate=0.0001), 
                  loss='sparse_categorical_crossentropy', 
                  metrics=['accuracy'])
    return model

def generate_dummy_data(samples=100):
    """
    Generates dummy random images for testing the training logic 
    without the full Kaggle dataset.
    """
    print("Generating dummy data...")
    X = np.random.rand(samples, 224, 224, 3).astype(np.float32)
    y = np.random.randint(0, NUM_CLASSES, samples)
    return X, y

def train():
    if not os.path.exists("models"):
        os.makedirs("models")
        
    model = build_model()
    model.summary()
    
    # Use dummy data for demonstration if no real data loader is present
    X_train, y_train = generate_dummy_data(samples=50)
    X_val, y_val = generate_dummy_data(samples=10)
    
    print("Starting Training (Demo Mode)...")
    history = model.fit(
        X_train, y_train,
        validation_data=(X_val, y_val),
        epochs=EPOCHS,
        batch_size=BATCH_SIZE
    )
    
    model.save(MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    train()
>>>>>>> bfc7beb115d588c39eae3b48e183112d5fff549a
