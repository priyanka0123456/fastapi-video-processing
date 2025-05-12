import cv2
import os
from pathlib import Path

def extract_frames(video_path: str, output_dir: str, interval_sec: int = 1):
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps * interval_sec

    frames = []
    count = 0
    success = True

    while success:
        success, frame = cap.read()
        if not success:
            break
        if count % frame_interval == 0:
            frame_name = f"{output_dir}/frame_{count}.jpg"
            cv2.imwrite(frame_name, frame)
            frames.append(frame_name)
        count += 1

    cap.release()
    return frames
