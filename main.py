import cv2

import auto_transform
import enhance
import compression
import utils

img_name = 'test.jpeg'
img_path = f'original/{img_name}'

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_enhance = enhance.enhance(img)
cv2.imwrite(f'enhanced/{img_name}', img_enhance)

img_scanned = auto_transform.warping(img_enhance)
cv2.imwrite(f'scanned/{img_name}', img_scanned)

compression.use_pil(img_name)

# utils.compare_img(img_scanned, img_compressed)
utils.compare_file_size(img_name)

utils.compare_img_sidebyside(img_name)

cv2.waitKey(0)