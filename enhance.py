import cv2

def enhance(img):

    # img = cv2.imread('test.jpeg')
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # img = cv2.resize

    # _, result = cv2.threshold(img, 20, 255, cv2.THRESH_BINARY)

    adaptive_result = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 41, 5)

    return adaptive_result

# cv2.imshow("original", img)
# cv2.imshow("adaptive", adaptive_result)
# cv2.waitKey(0)