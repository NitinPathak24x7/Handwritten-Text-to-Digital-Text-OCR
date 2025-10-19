import pytesseract
from PIL import Image
import cv2
from preprocess import preprocess_image  # Fixed import

def predict_text(img_path):
    # Preprocess the image (optional but improves accuracy)
    img = preprocess_image(img_path)

    # Convert OpenCV grayscale image to PIL image
    pil_img = Image.fromarray(img)

    # Tesseract config (LSTM OCR engine, assume single block of text)
    custom_config = r'--oem 3 --psm 6'

    # Run OCR
    text = pytesseract.image_to_string(pil_img, config=custom_config, lang='eng')
    return text

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py <image_path>")
    else:
        result = predict_text(sys.argv[1])
        print("📝 Predicted text:\n", result)

