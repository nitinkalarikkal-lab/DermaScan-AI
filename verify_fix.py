import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

model = tf.keras.models.load_model(r'C:\Users\NITIN\Downloads\demo\project\app\skin_cnn_mobilenetv2.h5')

def predict(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    preds = model.predict(x)[0]
    idx = np.argmax(preds)
    return float(preds[idx])

user_image = r'c:\Users\NITIN\OneDrive\Desktop\derma\Dermascan AI\project\media\uploads\WhatsApp Image 2026-02-21 at 13.04.00.jpeg'
THRESHOLD = 0.85

if os.path.exists(user_image):
    confidence = predict(user_image)
    print(f"\nUser Image Confidence: {confidence * 100:.2f}%")
    if confidence < THRESHOLD:
        print(f"[PASS] Correctly flagged as 'Uncertain' (below {THRESHOLD*100}% threshold)")
    else:
        print(f"[FAIL] Still flagged as disease! Confidence {confidence*100}% is above {THRESHOLD*100}%")
else:
    print(f"File not found: {user_image}")
