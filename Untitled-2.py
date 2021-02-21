from  PIL import  Image
import pytesseract
from cv2 import cv2 as cv
 
#img_path='F:/fb/xxx.jpg'
img_path='C:/Users/Administrator/Pictures/Camera Roll/chinese2.PNG'
# img_path='orgin.jpg'
 
# img_path='F:/fb/hpop.jpg'
 
# 依赖opencv
img=cv.imread(img_path)
text=pytesseract.image_to_string(Image.fromarray(img),lang='chi_sim')
 
 
# 不依赖opencv写法
# text=pytesseract.image_to_string(Image.open(img_path))
print(text)
 
 