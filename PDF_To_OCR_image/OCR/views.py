from django.shortcuts import render
from matplotlib.style import context
from traceback import print_tb
from PIL import Image
import pytesseract
import sys
from pdf2image import convert_from_path
import os
# Create your views here.
def index(request):
    pdf = request.POST.get("file")
    print("pdf ", pdf)
    context = {
        "data": "data"
    }
    return render(request, "index.html" , context)

def output(request):
    PDF_file = request.Get.get("pdf")
    # PDF_file = "HR.pdf"
    if(PDF_file):
        print("True")
    '''
    Part #1 : Converting PDF to images
    '''

# Store all the pages of the PDF in a variable
    pages = convert_from_path(PDF_file, 500)
    print("pages are = ", pages)
    # Counter to store images of each page of PDF to image
    image_counter = 1
    
    print("counter is = ", image_counter)
# Iterate through all the pages stored above
    images = []
    for page in pages:
        filename = str(image_counter) + ".jpg"
        print("page = ", page)
        # Declaring filename for each page of PDF as JPG
        # For each page, filename will be:
        # PDF page 1 -> page_1.jpg
        # PDF page 2 -> page_2.jpg
        # PDF page 3 -> page_3.jpg
        # ....
        # PDF page n -> page_n.jpg
        filename = "page_"+str(image_counter)+".jpg"
        
        # Save the image of the page in system
        page.save(filename, 'JPEG')
    
        # Increment the counter to update filename
        image_counter = image_counter + 1
        print("number of images are ", image_counter)
        
    '''
    Part #2 - Recognizing text from the images using OCR
    '''
# Variable to get count of total number of pages
    filelimit = image_counter-1
    print("file limit = ", filelimit)
    # Creating a text file to write the output
    outfile = "output_text.txt"
    
    # Open the file in append mode so that 
    # All contents of all images are added to the same file
    f = open(outfile, "a")
    
    # Iterate from 1 to total number of pages
    for i in range(1, filelimit + 1): 
        # Set filename to recognize text from
        # Again, these files will be:
        # page_1.jpg
        # page_2.jpg
        # ....
        # page_n.jpg
        filename = "page_"+str(i)+".jpg"
        
        # Recognize the text as string in image using pytesserct
        text = str(((pytesseract.image_to_string(Image.open(filename)))))
        print("text = ", text , type(text))
        # The recognized text is stored in variable text
        
        text = text.replace('-\n', '')    
    
        # Finally, write the processed text to the file.
        f.write(text)

    # Close the file after writing all the text.
        f.close()
        context = {
            "text_file" : text,
            "image": filename

        }
        return context