#coding = utf -8
from PIL import Image
import pytesseract
 
im = Image.open("C:/Users/Administrator/Pictures/Camera Roll/name.jpg")
a = pytesseract.image_to_string((im))
print(a)