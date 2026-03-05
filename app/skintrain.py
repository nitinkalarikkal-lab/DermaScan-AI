import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, models
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint

# Paths
train_dir = r'D:\Github\ClearDerm\skin\skin-disease-datasaet3\skin-disease-datasaet3\train_set'
val_dir   = r'D:\Github\ClearDerm\skin\skin-disease-datasaet3\skin-disease-datasaet3\test_set'

# Settings
img_size = (224, 224)
batch_size = 32
num_classes = 8
model_path = 'skin_cnn_mobilenetv2.h5'

# Augmentation
train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20, width_shift_range=0.1, height_shift_range=0.1,
    shear_range=0.1, zoom_range=0.1, horizontal_flip=True,
    validation_split=0.2
)

train_data = train_gen.flow_from_directory(
    train_dir, target_size=img_size, batch_size=batch_size,
    subset='training', class_mode='categorical'
)
val_data = train_gen.flow_from_directory(
    train_dir, target_size=img_size, batch_size=batch_size,
    subset='validation', class_mode='categorical'
)

# Model with transfer learning
base = tf.keras.applications.MobileNetV2(
    input_shape=img_size + (3,), include_top=False, weights='imagenet'
)
base.trainable = False

model = models.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dropout(0.3),
    layers.Dense(256, activation='relu'),
    layers.BatchNormalization(),
    layers.Dropout(0.3),
    layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Callbacks
callbacks = [
    ModelCheckpoint(model_path, save_best_only=True),
    EarlyStopping(patience=5, restore_best_weights=True),
    ReduceLROnPlateau(patience=3, factor=0.5)
]

history = model.fit(
    train_data, validation_data=val_data,
    epochs=30, callbacks=callbacks
)

print("✅ Training complete. Best model saved at", model_path)
