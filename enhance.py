import cv2
import numpy as np

def enhance(img):

    # _, result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

    return adaptive_result

def sharpen(img):

    # Create the sharpening kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

    # Sharpen the image
    sharpened_image = cv2.filter2D(img, -1, kernel)

    #Save the image
    cv2.imwrite('sharpened_image.jpg', sharpened_image)

    return sharpened_image

def gaus_blur(img):

    blurred_img = cv2.GaussianBlur(img, (3,3), 0)

    return blurred_img