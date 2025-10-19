import cv2

def segment_characters(img):
    contours, _ = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    char_images = []
    bounding_boxes = sorted([cv2.boundingRect(c) for c in contours], key=lambda b: b[0])
    for box in bounding_boxes:
        x, y, w, h = box
        char_img = img[y:y+h, x:x+w]
        char_img = cv2.resize(char_img, (28,28))
        char_img = char_img / 255.0
        char_img = char_img.reshape(28,28,1)
        char_images.append(char_img)
    return char_images

