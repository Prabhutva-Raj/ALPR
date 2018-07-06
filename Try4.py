import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open('Plate6_Fotor.jpg')  # img is the path of the image
im = im.convert("RGBA")
newimdata = []
datas = im.getdata()

for item in datas:
    if item[0] < 112 or item[1] < 112 or item[2] < 112:
        newimdata.append(item)
    else:
        newimdata.append((255, 255, 255))
im.putdata(newimdata)

im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'),config='-c tessedit_char_whitelist=0123456789abcdefghijklmnopqrstuvwxyz -psm 6', lang='eng')
print(text)
