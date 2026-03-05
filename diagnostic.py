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

test_images = [
    r'c:\Users\NITIN\OneDrive\Desktop\derma\Dermascan AI\project\test_set\BA- cellulitis (104).jpg',
    r'c:\Users\NITIN\OneDrive\Desktop\derma\Dermascan AI\project\test_set\10_BA-impetigo (89).jpg',
    r'c:\Users\NITIN\OneDrive\Desktop\derma\Dermascan AI\project\test_set\FU-athlete-foot (1).jpg'
]

for img_path in test_images:
    if os.path.exists(img_path):
        preds = predict_full(img_path)
        print(f"\nImage: {os.path.basename(img_path)}")
        print(f"Probabilities: {preds}")
        print(f"Argmax index: {np.argmax(preds)}")
    else:
        print(f"File not found: {img_path}")
