import cv2
import os

def compare_img(img1, img2):

    # # Example usage
    # original_img = cv2.imread('original_image.jpg')
    # compressed_img = compress_image('original_image.jpg', quality=50)

    # Display results
    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def compare_file_size(file_path):

    folders = ['original', 'scanned', 'compressed']

    for folder in folders:
        
        file_size_bytes = os.path.getsize(f"{folder}/{file_path}")

        # Conversion to kilobytes, megabytes, and gigabytes
        file_size_kb = file_size_bytes / 1024
        # file_size_mb = file_size_kb / 1024
        # file_size_gb = file_size_mb / 1024

        print(folder)
        print(f"File Size (KB): {file_size_kb:.2f} KB\n")