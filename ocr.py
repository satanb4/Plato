from PIL import Image
import pytesseract
import argparse
import cv2
import os

def ocr():
    image=cv2.imread('/Users/rushikeshdeotale/Desktop/Project/xy.jpg')
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string((cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    return text
print(ocr())
print(type(ocr()))