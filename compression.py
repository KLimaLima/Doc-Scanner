import cv2
import numpy as np
from PIL import Image

def use_cv2(img, quality=90):

    # Encode the image with JPEG compression
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
    _, encoded_img = cv2.imencode('.jpg', img, encode_param)
        
    # Decode the compressed image
    decoded_img = cv2.imdecode(encoded_img, cv2.IMREAD_GRAYSCALE)
        
    return decoded_img

def use_pil(img_name, quality= 20):

    input_img = f"scanned/{img_name}"
    output_img = f"compressed/{img_name}"

    # Open the image
    with Image.open(input_img) as comp_img:
        # Compress and saving the image
        comp_img.save(output_img, "JPEG", quality=quality)

    print(f"Image compressed successfully")