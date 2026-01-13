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

# img_enhance = enhance.enhance(img_scanned)
# cv2.imwrite(f'enhanced/{img_name}', img_enhance)

img_compressed = compression.compress_image(img_scanned, 25)
cv2.imwrite(f'compressed/{img_name}', img_compressed)


from PIL import Image
input_img = f"scanned/{img_name}"
quality = 20
output_img = f"compressed_{quality}.jpg"


# Open the image
with Image.open(input_img) as comp_img:
    # Compress and saving the image
    comp_img.save(output_img, "JPEG", quality=quality)

print(f"Image compressed successfully")


utils.compare_img(img_scanned, img_compressed)
utils.compare_file_size(img_name)

cv2.waitKey(0)