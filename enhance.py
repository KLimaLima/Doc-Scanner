import cv2

def enhance(img):

    # _, result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

    return adaptive_result