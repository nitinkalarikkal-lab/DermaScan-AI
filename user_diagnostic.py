import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'app', 'skin_cnn_mobilenetv2.h5')
model = tf.keras.models.load_model(model_path)

def predict_full(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    preds = model.predict(x)[0]
    return preds

user_image = os.path.join(BASE_DIR, 'media', 'uploads', 'WhatsApp Image 2026-02-21 at 13.04.00.jpeg')

if os.path.exists(user_image):
    preds = predict_full(user_image)
    print(f"\nUser Image: {os.path.basename(user_image)}")
    print(f"Probabilities: {preds}")
    idx = np.argmax(preds)
    print(f"Argmax index: {idx}")
    print(f"Confidence: {preds[idx] * 100:.2f}%")
else:
    print(f"File not found: {user_image}")
