import cv2
import numpy as np

def compress_image(img, quality=90):

    # Encode the image with JPEG compression
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)
        
    # Decode the compressed image
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_GRAYSCALE)
        
    return decoded_img