from PIL import Image
from pytesseract import pytesseract
  
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Users\Mobilelink\anaconda3\envs\Machine_learning\Scripts\pytesseract.exe"
image_path = r"D:\Fayyaz work\OCR\shahzad ocr\pdftoimage\3384-1625385565-9098\1.jpg"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
# Displaying the extracted text
print(text)