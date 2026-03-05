import tensorflow as tf
try:
    model = tf.keras.models.load_model(r'C:\Users\NITIN\Downloads\demo\project\app\skin_cnn_mobilenetv2.h5')
    print(f"Model input shape: {model.input_shape}")
    print(f"Model output shape: {model.output_shape}")
except Exception as e:
    print(f"Error: {e}")
