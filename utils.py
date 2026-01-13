import cv2
import numpy as np
import os

folders = ['original', 'scanned', 'compressed']

def compare_img(img1, img2):

    # # Example usage
    # original_img = cv2.imread('original_image.jpg')
    # compressed_img = compress_image('original_image.jpg', quality=50)

    # Display results
    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def compare_img_sidebyside(img_name):

    list_img = []
    n = len(folders)

    for folder in folders:

        img = cv2.imread(f"{folder}/{img_name}")
        list_img.append(img)

        try:
            all_img = np.hstack((all_img, img))
        except:
            all_img = img

    cv2.imshow("Image comparison", all_img)
    cv2.waitKey(0)
    
    # img_hor = np.hstack((list_img[n-3], list_img[n-2], list_img[n-1]))

def compare_file_size(file_path):

    # folders = ['original', 'scanned', 'compressed']

    for folder in folders:
        
        file_size_bytes = os.path.getsize(f"{folder}/{file_path}")

        # Conversion to kilobytes, megabytes, and gigabytes
        file_size_kb = file_size_bytes / 1024
        # file_size_mb = file_size_kb / 1024
        # file_size_gb = file_size_mb / 1024

        print(folder)
        print(f"File Size (KB): {file_size_kb:.2f} KB\n")