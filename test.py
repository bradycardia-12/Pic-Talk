from gtts import gTTS
import os
from langdetect import detect

Text_generated="hello"
language = detect(Text_generated)
text = Text_generated
speech = gTTS(text = text, lang = language, slow = False)
speech.save("text2.mp3")
os.system("start text2.mp3")

'''import pytesseract
import shutil
import os
import random
try:
  from PIL import Image
except ImportError:
  import Image
import glob
import cv2
def read_img(img_list, img):
    n = cv2.imread(img, 0)
    img_list.append(n)
    return img_list

path = glob.glob("*.bmp") #or jpg
list_ = []

cv_image = [read_img(list_, img) for img in path]

image_path_in_colab=r'C:\\Users\\charv\\PicTalk\\uploads\\spacejam2.png'
extractedInformation = pytesseract.image_to_string(Image.open(image_path_in_colab),lang="eng+fra+ita+deu+spa+por+nld")
Text_generated=extractedInformation

print(Text_generated)'''