import cv2

import auto_transform
import enhance
import compression
import utils

img_path = 'original/test.jpeg'

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_enhance = enhance.enhance(img)
cv2.imwrite(f'enhanced/{img_path}', img_enhance)

img_scanned = auto_transform.warping(img_enhance)
cv2.imwrite(f'scanned/{img_path}', img_scanned)

img_compressed = compression.compress_image(img_scanned, 20)
cv2.imwrite(f'compressed/{img_path}', img_compressed)

utils.compare_img(img_scanned, img_compressed)

cv2.waitKey(0)