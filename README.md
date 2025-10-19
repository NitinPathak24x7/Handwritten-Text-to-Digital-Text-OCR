# Handwritten-Text-to-Digital-Text-OCR

Convert handwritten letters, digits, and full sentences into editable, copyable digital text using **Tesseract OCR** and **OpenCV**.  

This project bypasses the need for model training (no EMNIST), works with **any image size**, and can handle **cursive and mixed handwriting**.

---

## **Features**
- Detects handwritten letters, digits, and words
- Works with images of any dimensions
- Preprocessing includes grayscale, thresholding, and resizing
- Optional GUI support for drag & drop image testing
- Lightweight and easy to set up (no training required)

---
## **Project Structure**

OCR
│
├── src/
│ ├── main.py # Main script to run OCR
│ ├── preprocess.py # Image preprocessing (grayscale, threshold)
│ └── utils.py # Optional helper functions
├── test_images/ # Place your handwritten images here
├── requirements.txt # Python dependencies
└── venv/ # Virtual environment

## **Setup**
Step 1 -
navigate to the project root folder /  (OCR) 

Step 2 -
create and activate virtual environment for the project 
$ python3 -m venv venv
$ source venv/bin/activate   # On Linux/Mac
$ venv\Scripts\activate      # On Windows

Step 3 -
install required packages
$ pip install -r requirements.txt

Step 4 -
move the image in "test_images" directory 

step 5 - 
Run the OCR script:
$ python3 src/main.py test_images/sample.png

---------------Dependencies---------------

Tesseract OCR
pytesseract
opencv-python
Pillow
tk (optional)
