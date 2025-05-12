# 🎥 FastAPI Video Processing App

This project is a FastAPI-based application that performs the following tasks:

- Extracts frames from uploaded videos.
- Computes feature vectors using image color histograms.
- Stores vectors in a Qdrant vector database.
- Supports image-based similarity search over extracted frames.

---

## 🚀 Features

### ✅ Video Processing
- Accepts `.mp4` video uploads via API.
- Extracts frames at 1-second intervals using OpenCV.
- Saves extracted frames as images in a local directory.

### ✅ Feature Vector Computation
- Computes simple feature vectors (color histograms) for each frame.
- Stores the vectors in an in-memory or external [Qdrant](https://qdrant.tech/) vector database.

### ✅ API for Similarity Search
- Upload an image and find visually similar frames from uploaded videos.
- Returns paths to the matched frame images and similarity scores.

---

## 🛠 Technologies Used

- **Python 3.8+**
- **FastAPI** – Web framework
- **OpenCV** – Video frame extraction
- **NumPy** – Image histogram computation
- **Qdrant** – Vector similarity search
- **Uvicorn** – ASGI server

---

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/priyanka0123456/fastapi-video-processing.git
cd <repo-name>
