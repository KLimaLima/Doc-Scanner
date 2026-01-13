import cv2

def compare_img(img1, img2):

    # # Example usage
    # original_img = cv2.imread('original_image.jpg')
    # compressed_img = compress_image('original_image.jpg', quality=50)

    # Display results
    cv2.imshow('Image 1', img1)
    cv2.imshow('Image 2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()