import cv2
import numpy as np
import os

folders = ['original', 'scanned', 'compressed', 'enhanced']

def compare_img(img_name):

    for folder in folders:

        img  = cv2.imread(f"{folder}/{img_name}")
        cv2.imshow(folder, img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Display results
    # cv2.imshow('Image 1', img1)
    # cv2.imshow('Image 2', img2)

# display image side by side
# def compare_img_sidebyside(img_name):

#     # get all image in each folder

#     img1 = cv2.imread(f"{folders[0]}/{img_name}")
#     img2 = cv2.imread(f"{folders[1]}/{img_name}")
#     img3 = cv2.imread(f"{folders[2]}/{img_name}")

#     all_img = np.hstack((img1, img2, img3))

#     cv2.imshow("Image comparison", all_img)
#     cv2.waitKey(0)

def compare_file_size(file_path):

    for folder in folders:
        
        file_size_bytes = os.path.getsize(f"{folder}/{file_path}")

        # Conversion to kilobytes, megabytes, and gigabytes
        file_size_kb = file_size_bytes / 1024
        # file_size_mb = file_size_kb / 1024
        # file_size_gb = file_size_mb / 1024

        print(folder)
        print(f"File Size (KB): {file_size_kb:.2f} KB\n")