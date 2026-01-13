import cv2

import auto_transform
import enhance
import compression
import utils

########### INPUT IMAGE ##############
img_name = 'test2.jpeg'
img_path = f'original/{img_name}'

img = cv2.imread(img_path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

########### SEGMENT AND TRANSFORM IMAGE ##############
img_scanned = auto_transform.warping(img)
cv2.imwrite(f'scanned/{img_name}', img_scanned)

########### ENCHANCE IMAGE ##############
# # ada tompok hitam
# img_sharpen = enhance.sharpen(img_scanned)

# img_enhance = enhance.enhance(img_sharpen)
# cv2.imwrite(f'enhanced/{img_name}', img_enhance)

# removed noise
img_sharpen = enhance.sharpen(img_scanned)

img_blur = enhance.gaus_blur(img_sharpen)

img_enhance = enhance.enhance(img_blur)
cv2.imwrite(f'enhanced/{img_name}', img_enhance)

########### COMPRESS IMAGE ##############
compression.use_pil(img_name)
# compression.use_pil(img_name, 5)

########### ANALYSIS ##############
utils.compare_file_size(img_name)

utils.compare_img(img_name)
# utils.compare_img_sidebyside(img_name)