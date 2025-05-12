from fastapi import FastAPI, UploadFile, File, HTTPException
from utils.video_processing import extract_frames
from utils.feature_extraction import compute_color_histogram
from utils.qdrant_client import initialize_collection, upload_feature_vector, search_similar
import shutil
import os
from fastapi.responses import FileResponse
from typing import List
import numpy as np

app = FastAPI()

FRAMES_DIR = "frames"
os.makedirs(FRAMES_DIR, exist_ok=True)
initialize_collection(vector_size=512)  # 8*8*8 = 512 bins for HSV hist

@app.post("/upload-video/")
async def upload_video(file: UploadFile = File(...)):
    temp_video_path = f"temp_{file.filename}"
    with open(temp_video_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    frames = extract_frames(temp_video_path, FRAMES_DIR, interval_sec=1)
    os.remove(temp_video_path)

    for frame_path in frames:
        vector = compute_color_histogram(frame_path)
        metadata = {"frame_path": frame_path}
        upload_feature_vector(vector.tolist(), metadata)

    return {"message": f"Processed {len(frames)} frames"}

@app.post("/search/")
async def search_similar_frames(file: UploadFile = File(...), top_k: int = 5):
    temp_image_path = f"temp_{file.filename}"
    with open(temp_image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    query_vector = compute_color_histogram(temp_image_path)
    results = search_similar(query_vector.tolist(), top_k=top_k)
    os.remove(temp_image_path)

    return [{
        "score": r.score,
        "frame_path": r.payload["frame_path"],
        "vector": r.vector
    } for r in results]
