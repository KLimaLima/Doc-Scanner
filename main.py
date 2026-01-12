import cv2

import auto_transform
import enhance

img_path = 'test.jpeg'

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_enhance = enhance.enhance(img)

result = auto_transform.warping(img_enhance)

cv2.imshow("output", result)

cv2.waitKey(0)