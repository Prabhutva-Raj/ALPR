import random
import pytesseract
from PIL import Image



def image_recognize():

    class GetImageDate(object):
        def m(self):
            image = Image.open("C:\\Users\\ADMIN\\Desktop\\New folder\\Images\\Plate6_Fotor.jpg")
            (w,h)=image.size
            print(w,h)
            text = pytesseract.image_to_string(image)
            return text

        def SaveResultToDocument(self):
            text = self.m()
            print (text)
            f = open(u"Verification.txt", "w")
            f.write(str(text))
            f.close()

    g = GetImageDate()
    g.SaveResultToDocument()


def main():
    image_recognize()

if __name__=='__main__':
    main()