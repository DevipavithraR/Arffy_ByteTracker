import cv2
import numpy as np
import time
import os

def preprocess_image(image, shape):
    _, _, h, w = shape
    resized = cv2.resize(image, (w, h))
    transposed = np.transpose(resized, (2, 0, 1))
    return np.expand_dims(transposed, axis=0).astype(np.float32)

def classify_head_position(pitch, down_threshold=20, up_threshold=-20):
    if pitch >= down_threshold:
        return "Down"
    elif pitch <= up_threshold:
        return "Up"
    else:
        return "Forward"
    
def getdatapath(current_script_dir, backward, data_dir):
    # Navigate to the parent directory (one level up)
    parent_dir = os.path.join(current_script_dir, backward)
    # Resolve the '..' to get the absolute path of the parent directory
    absolute_parent_dir = os.path.abspath(parent_dir)

    print(f"Parent directory: {absolute_parent_dir}")

    # Example: Accessing a 'data' folder in the parent directory
    data_folder_path = os.path.join(absolute_parent_dir, data_dir)
    print(f"Data folder path: {data_folder_path}")

    return data_folder_path