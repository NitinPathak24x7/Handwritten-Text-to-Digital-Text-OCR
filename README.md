# Handwritten-Text-to-Digital-Text-OCR
Convert handwritten letters, digits, and full sentences into editable, copyable digital text using **Tesseract OCR** and **OpenCV**.    This project bypasses the need for model training (no EMNIST), works with **any image size**, and can handle **cursive and mixed handwriting**.

Features---------
- Detects handwritten letters, digits, and words
- Works with images of any dimensions
- Preprocessing includes grayscale, thresholding, and resizing
- Optional GUI support for drag & drop image testing
- Lightweight and easy to set up (no training required)

project structure-----------
OCR/
│
├── src/
│ ├── main.py # Main script to run OCR
│ ├── preprocess.py # Image preprocessing (grayscale, threshold)
│ └── utils.py # Optional helper functions
├── test_images/ # Place your handwritten images here
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment
