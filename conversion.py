#CONVERSION

#convert pdf to png
from pdf2image import convert_from_path
import img2pdf
from PIL import Image
import os



poppler_path = r"C:\Users\rohit\New folder\Release-24.02.0-0\poppler-24.02.0\Library\bin"

# Store Pdf with convert_from_path function
def pdftopng():
  images = convert_from_path('sample_report_pdf.pdf')
  
  for i in range(len(images)):
    
        # Save pages as images in the pdf
      images[i].save('page'+ str(i) +'.png', 'PNG')


def pngtopdf():
  # storing image path
  img_path = "borderless.jpg"
  
  # storing pdf path
  pdf_path = "output.pdf"
  
  # opening image
  image = Image.open(img_path)
  
  # converting into chunks using img2pdf
  pdf_bytes = img2pdf.convert(image.filename)
  
  # opening or creating pdf file
  file = open(pdf_path, "wb")
  
  # writing pdf files with chunks
  file.write(pdf_bytes)
  
  # closing image file
  image.close()
  
  # closing pdf file
  file.close()
  
  # output
  print("Successfully made pdf file")

pngtopdf()  


