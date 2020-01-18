from PIL import Image
from pytesseract import image_to_string
print image_to_string(Image.open('ss.jpeg'))
print image_to_string(Image.open('ss1.jpeg'), lang='eng')
