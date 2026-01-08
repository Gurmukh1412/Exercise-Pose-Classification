import cv2
import os
import mediapipe as mp
import csv
from tqdm import tqdm

# Initialize MediaPipe pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)
mp_drawing = mp.solutions.drawing_utils

def extract_pose_keypoints(image_path):
    """Extracts 33 pose landmarks (x, y, visibility) from an image."""
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        return None  # No pose detected

    keypoints = []
    for lm in results.pose_landmarks.landmark:
        keypoints.extend([lm.x, lm.y, lm.visibility])
    return keypoints

def process_dataset(dataset_path, output_csv="pose_data.csv"):
    """Walks through Dataset/class_name/*.jpg and writes keypoints + label to CSV."""
    with open(output_csv, mode='w', newline='') as f:
        writer = csv.writer(f)

        # Header: x0, y0, v0, ..., x32, y32, v32, label
        header = []
        for i in range(33):
            header.extend([f'x{i}', f'y{i}', f'v{i}'])
        header.append('label')
        writer.writerow(header)

        # Process each class folder
        for label in os.listdir(dataset_path):
            label_path = os.path.join(dataset_path, label)
            if not os.path.isdir(label_path):
                continue

            print(f"[INFO] Processing label: {label}")
            for img_file in tqdm(os.listdir(label_path)):
                img_path = os.path.join(label_path, img_file)
                keypoints = extract_pose_keypoints(img_path)

                if keypoints:  # Only write if pose was detected
                    keypoints.append(label)
                    writer.writerow(keypoints)

# Example usage:
process_dataset("Dataset", "pose_data.csv")

