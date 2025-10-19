import cv2

def preprocess_image(img_path):
    # Read image in grayscale
    img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

    # Optional: threshold to enhance handwritten text
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

    # Optional: resize huge images to max width 1024px
    max_width = 1024
    if img.shape[1] > max_width:
        scale = max_width / img.shape[1]
        img = cv2.resize(img, (0,0), fx=scale, fy=scale)

    return img

