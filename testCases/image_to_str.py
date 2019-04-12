# from PIL import Image
# import pytesseract
#
#
# text = pytesseract.image_to_string(Image.open(r'E:\PaaS\testCases\getValidateCode.png'))
# print(text)


a = range(1000, 3000)
temp = []
for i in a:
    s = str(i)
    Y = [False if int(i) % 2 else True for i in s]
    # print(Y)
    if False not in Y:
        temp.append(i)
        print(i)
