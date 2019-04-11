from PIL import Image
import pytesseract


text = pytesseract.image_to_string(Image.open(r'E:\PaaS\testCases\getValidateCode.png'))
print(text)
