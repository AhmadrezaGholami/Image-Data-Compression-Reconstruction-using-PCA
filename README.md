## 📷 Image Compression using PCA

![PCA Image Compression](https://img.shields.io/badge/PCA-Compression-blue?style=for-the-badge&logo=fastapi)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-green?style=for-the-badge&logo=fastapi)

### 🚀 Project Overview
This project implements **Principal Component Analysis (PCA)** to compress grayscale images while maintaining essential features. The **FastAPI** framework provides an API endpoint to upload images, compress them using PCA, and return both the original and reconstructed images in **base64** format.

---
### 📌 Features
✅ **Image Upload** via API<br>
✅ **PCA-based Dimensionality Reduction**<br>
✅ **Reconstruction of Compressed Images**<br>
✅ **Base64 Encoding for Image Transmission**<br>
✅ **CORS Enabled** for Cross-Origin Requests

---
### 🏗️ Tech Stack
- 🐍 **Python**
- ⚡ **FastAPI**
- 📦 **Joblib** (Model loading)
- 📊 **NumPy** (Array computations)
- 🎨 **PIL (Pillow)** (Image processing)

---
### 📁 Setup Instructions
```bash
# Clone this repository
git clone https://github.com/AhmadrezaGholami/Image-Data-Compression-Reconstruction-using-PCA.git
cd Image-Data-Compression-Reconstruction-using-PCA

# Run the FastAPI server
uvicorn main:app --reload
```

---
### 🔥 API Endpoint
#### `POST /compress_image/`
- **Description:** Uploads an image and compresses it using PCA.
- **Request:**
  - `file`: UploadFile (grayscale image)
- **Response:** JSON with compressed and reconstructed images in base64 format.

---
### 📊 PCA Model
The PCA model (`pca_200_.pkl`) is trained to retain **200 principal components** while reducing dimensionality.
For more details, visit the Kaggle Notebook where the PCA model was trained:

[![Kaggle](https://img.shields.io/badge/Kaggle-Notebook-blue?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/code/ahmadrezagholami2001/image-data-compression-reconstruction)

---
### ✨ Sample Response
```json
{
    "original_shape": "(256, 256)",
    "original_size": "524288 bytes",
    "compressed_shape": "(1, 200)",
    "compressed_size": "1600 bytes",
    "original_image": "data:image/png;base64,iVBORw...",
    "reconstructed_image": "data:image/png;base64,iVBORw..."
}
```

---
### 📜 License
📝 This project is licensed under the **MIT License**.

---
### 🌟 Show Your Support!
If you like this project, please ⭐️ the repository!
