import cv2
import os

def extract_frames_nested_unique(root_input_folder, root_output_folder, frame_rate=1):
    """
    Extracts frames from videos in a nested folder structure.
    For each exercise folder in root_input_folder:
      - Creates a corresponding folder in root_output_folder.
      - For each video inside the exercise folder, creates a unique subfolder (named after the video)
        and saves its frames there.
    
    Parameters:
    - root_input_folder: str, path to the main folder containing exercise subfolders
    - root_output_folder: str, path to the folder where extracted frames will be saved
    - frame_rate: int, extracts every nth frame (default 1 means every frame)
    """
    # Video file extensions to support
    video_extensions = ['.mp4', '.avi', '.mov', '.mkv']

    for exercise in os.listdir(root_input_folder):
        exercise_input_path = os.path.join(root_input_folder, exercise)
        
        # Check if this is a directory (e.g., "barbell curl")
        if os.path.isdir(exercise_input_path):
            # Create the corresponding exercise folder in the output directory
            exercise_output_path = os.path.join(root_output_folder, exercise)
            os.makedirs(exercise_output_path, exist_ok=True)
            
            # Process each video file in the exercise folder
            for video_file in os.listdir(exercise_input_path):
                file_path = os.path.join(exercise_input_path, video_file)
                name, ext = os.path.splitext(video_file)
                
                if ext.lower() in video_extensions:
                    # Create a unique folder for this video within its exercise folder
                    video_output_folder = os.path.join(exercise_output_path, name)
                    os.makedirs(video_output_folder, exist_ok=True)
                    
                    # Open the video and extract frames
                    cap = cv2.VideoCapture(file_path)
                    count, saved = 0, 0
                    
                    while cap.isOpened():
                        ret, frame = cap.read()
                        if not ret:
                            break
                        # Save every nth frame (according to the frame_rate)
                        if count % frame_rate == 0:
                            frame_filename = os.path.join(video_output_folder, f"frame_{saved:04d}.jpg")
                            cv2.imwrite(frame_filename, frame)
                            saved += 1
                        count += 1
                        
                    cap.release()
                    print(f"[INFO] Extracted {saved} frames from {video_file} into {video_output_folder}")

# Example usage:
extract_frames_nested_unique("Exercises", "Frames", frame_rate=5)

