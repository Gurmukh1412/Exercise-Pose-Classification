import os
import shutil

def flatten_frames_by_class(input_root, output_root):
    """
    Flattens nested frame folders (Frames/class/video/frame.jpg) into:
    output_root/class/frame.jpg
    """
    for exercise in os.listdir(input_root):
        exercise_path = os.path.join(input_root, exercise)
        if not os.path.isdir(exercise_path):
            continue
        
        output_class_path = os.path.join(output_root, exercise)
        os.makedirs(output_class_path, exist_ok=True)

        for video_folder in os.listdir(exercise_path):
            video_path = os.path.join(exercise_path, video_folder)
            if not os.path.isdir(video_path):
                continue
            
            for frame_file in os.listdir(video_path):
                src = os.path.join(video_path, frame_file)
                # Rename to avoid name collisions
                new_filename = f"{exercise}_{video_folder}_{frame_file}"
                dst = os.path.join(output_class_path, new_filename)
                shutil.copy(src, dst)

        print(f"[INFO] Flattened '{exercise}' into {output_class_path}")

# Example usage:
flatten_frames_by_class("Frames", "Dataset")
