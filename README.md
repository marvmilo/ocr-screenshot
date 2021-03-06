# OCR Screenshot
**Version:** 1.0

**Software Dependencies:** 
- Python 3.9
- Git CLI
- Tesseract

**Python Dependencies:**
- pillow
- opencv-python
- pytesseract
- pyperclip

# Description:
Tool for extracting text with OCR from picture in clipboard. Can be used with Windows Snip & Sketch. You can replace picture with edited OCR text in your clipboard.

# Install
1. Download repository: ```git clone https://github.com/marvmilo/ocr-screenshot```
1. Create python virtual enviroment: ```python -m venv env```
1. Activate virtual enviroment: ```.\env\Scripts\activate```
1. Install requirements: ```pip install -r requirements.txt```
1. Install tesseract with the setup .EXE file in repository (remember path of tesseract.exe!)
1. Update ```tesseract_path``` of tesseract.exe in ```settings.json```
1. Create shortcut of batch file on desktop: ```right click -> new -> shortcut -> select run.bat```
1. Add keycombination to shortcut: ```right click on shortcut icon -> properties -> set shortcut key```

# How to use:
1. Copy Image or take Screenshot with ```Win + shift + S```
1. Press your selected shortcut -> CMD and Notepad popup
1. Correct text and Notepad, then save and close
1. Now text is in your clipboard