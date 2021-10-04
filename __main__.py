from PIL import ImageGrab
import pytesseract
import cv2
import os
import pyperclip

print("opening notepad ...")

#variables
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
OCR_text_file = "OCR.txt"
screenshot_file = "capture.png"
error_msg = "ERROR :(\nNo image was in your clipboard. Couldn't use OCR!"
resize_factor = 3

#saving image
img = ImageGrab.grabclipboard()

#loading text
try:
    img.save(screenshot_file, "PNG")
    img = cv2.imread(screenshot_file)
    img = cv2.resize(img, (img.shape[1]*resize_factor, img.shape[0]*resize_factor))
    cv2.imwrite("img.png", img)
    custom_config = r'--oem 3 --psm 6'
    text = pytesseract.image_to_string(img, config = custom_config)[:-2]
except AttributeError:
    text = "ERROR :(\nNo image in your clipboard. Couldn't run OCR!"


#write to file and open in notepad
with open(OCR_text_file, "w") as wd:
    wd.write(text)
os.system(f"notepad.exe {OCR_text_file}")

#copy saved file to clipboard
with open(OCR_text_file, "r") as rd:
    content = rd.read()
    if not error_msg == content:
        pyperclip.copy(content)
    
#remove files
os.remove(OCR_text_file)
os.remove(screenshot_file)