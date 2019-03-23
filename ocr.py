from PIL import Image
import pytesseract
import argparse
import cv2
import os
from rake_nltk import Rake

r = Rake()
def ocr():
    image=cv2.imread('/Users/rushikeshdeotale/Desktop/Plato/qw.jpg')
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string((cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)))
    return text
text = ocr()
#l = (text.split('?'))
print(text)
r.extract_keywords_from_text(text)
print(r.get_ranked_phrases()) 