from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import joblib
import base64
from io import BytesIO
from PIL import Image

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load PCA model
pca = joblib.load("pca_200_.pkl")

def encode_image(image_array):
    image = Image.fromarray((image_array * 255).astype(np.uint8))
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

@app.post("/compress_image/")
async def compress_image(file: UploadFile = File(...)):
    # Read image
    image = Image.open(file.file).convert("L")
    image = np.array(image) / 255.0  # Normalize
    original_shape = image.shape
    original_size = file.size
    
    # Flatten image
    image_flat = image.flatten().reshape(1, -1)
    
    # Apply PCA compression
    compressed = pca.transform(image_flat)
    compressed_shape = compressed.shape
    compressed_size = compressed.nbytes
    
    # Reconstruct image
    reconstructed = pca.inverse_transform(compressed)
    reconstructed = reconstructed.reshape(original_shape)
    
    return {
        "original_shape": str(original_shape),
        "original_size": f"{original_size} bytes",
        "compressed_shape": str(compressed_shape),
        "compressed_size": f"{compressed_size} bytes",
        "original_image": encode_image(image),
        "reconstructed_image": encode_image(reconstructed),
    }
