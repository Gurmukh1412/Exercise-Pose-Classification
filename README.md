# Exercise-Pose-Classification
This project implements an end-to-end exercise classification system using human pose estimation. Exercise videos are converted into frames, pose keypoints are extracted using MediaPipe, and a Keras-based MLP model is trained on landmark features. The trained model is converted to TensorFlow Lite for efficient deployment on edge and mobile devices.

---

## 🚀 Project Pipeline
1. Video to frame extraction using OpenCV  
2. Dataset flattening and labeling by exercise class  
3. Pose keypoint extraction (33 landmarks × x, y, visibility)  
4. CSV dataset generation  
5. MLP model training using TensorFlow Keras  
6. Model conversion to TensorFlow Lite (TFLite)

---

## 🧠 Model Details
- Input Features: 99 (33 pose landmarks × x, y, visibility)  
- Model Type: Multi-Layer Perceptron (MLP)  
- Framework: TensorFlow / Keras  
- Loss Function: Categorical Cross-Entropy  
- Optimizer: Adam  
- Output: Exercise class prediction  

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- MediaPipe Pose  
- TensorFlow / Keras  
- Scikit-learn  
- NumPy  
- Pandas  
- TensorFlow Lite  

---

## 📂 Folder Structure

