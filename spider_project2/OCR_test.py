import pytesseract
from PIL import Image

image = Image.open('test_20180626100934.png')
text = pytesseract.image_to_string(image)
print(text)
