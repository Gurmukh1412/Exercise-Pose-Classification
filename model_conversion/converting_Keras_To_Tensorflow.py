import tensorflow as tf

# Load the trained Keras model
model = tf.keras.models.load_model("exercise_classifier_keras.h5")

# Convert to TensorFlow Lite format
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

# Save the converted model
with open("exercise_classifier.tflite", "wb") as f:
    f.write(tflite_model)

print("✅ Model successfully converted to TensorFlow Lite: exercise_classifier.tflite")
