from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
import uuid

COLLECTION_NAME = "video_frames"

client = QdrantClient(":memory:")  # In-memory for simplicity; switch to actual DB in production

def initialize_collection(vector_size: int):
    if COLLECTION_NAME not in [c.name for c in client.get_collections().collections]:
        client.recreate_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(size=vector_size, distance=Distance.COSINE)
        )

def upload_feature_vector(vector: list, metadata: dict):
    point_id = str(uuid.uuid4())
    client.upsert(
        collection_name=COLLECTION_NAME,
        points=[PointStruct(id=point_id, vector=vector, payload=metadata)]
    )
    return point_id

def search_similar(vector: list, top_k=5):
    results = client.search(
        collection_name=COLLECTION_NAME,
        query_vector=vector,
        limit=top_k
    )
    return results
