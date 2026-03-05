import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# 1️⃣ Load your trained model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, 'skin_cnn_mobilenetv2.h5')
model = tf.keras.models.load_model(model_path)
# print("Model loaded: skin_cnn_model.h5")

# 2️⃣ Define the classes in the same order used during training
class_names = ['BA-cellulitis', 'BA-impetigo', 'FU-athlete-foot', 'FU-nail-fungus']

def load_and_preprocess(img_path, size=(224, 224)):
    if not os.path.isfile(img_path):
        raise FileNotFoundError(f"Image not found: {img_path}")
    img = image.load_img(img_path, target_size=size)
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)  
    x = x / 255.0                  
    return x

def predict(img_tensor):
    preds = model.predict(img_tensor)[0]
    idx = np.argmax(preds)
    return class_names[idx], float(preds[idx])

if __name__ == '__main__':
    img_path = input("Enter path to the image file: ").strip()
    try:
        img_tensor = load_and_preprocess(img_path)
        label, confidence = predict(img_tensor)
        print(f"\n🔍 Prediction: **{label}** — {confidence * 100:.2f}% confidence")
    except Exception as e:
        print("❌ Error:", e)
