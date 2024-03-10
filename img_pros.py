#Create Border for PNG to identify the table and hence get the coords of the table
import cv2
import numpy as np
from img2table.ocr import TesseractOCR
from img2table.document import Image
from img2table.ocr.base import OCRInstance
from img2table.document import PDF
from PIL import Image as PILImage
from pdf2image import convert_from_path


def display_borderless_tables(img: Image, ocr: OCRInstance) -> np.ndarray: #(return type)
    """
    Create display of borderless table extraction
    :param img: Image object
    :param ocr: OCRInstance object
    :return: display image
    """
    # Extract tables
    extracted_tables = img.extract_tables(ocr=ocr,
                                      implicit_rows=True,
                                      borderless_tables=True,
                                      min_confidence=50)

    # Create image displaying extracted tables
    display_image = cv2.cvtColor(list(img.images)[0], cv2.COLOR_GRAY2RGB)
    
    for page, tables in extracted_tables.items():
        for idx, table in enumerate(tables):
            
            for row in table.content.values():
                for cell in row:
                    cv2.rectangle(display_image, (cell.bbox.x1, cell.bbox.y1), (cell.bbox.x2, cell.bbox.y2),
                                    (255, 0, 0), 2)

    # Create white separator image
    width = min(display_image.shape[1] // 10, 100)
    white_img = cv2.cvtColor(255 * np.ones((display_image.shape[0], width), dtype=np.uint8), cv2.COLOR_GRAY2RGB)

    # Stack images
    final_image = np.hstack([white_img,
                            display_image])

    return final_image

#doc = path of pdf
def border(image_path):
    # Instantiation of OCR
    ocr = TesseractOCR(n_threads=1, lang="eng")
    pdf_path = image_path
    
    doc = PDF(src=pdf_path)

    # Extraction of tables and creation of a xlsx file containing tables
    display_img = display_borderless_tables(img=doc, ocr=ocr)
    
    
    data = PILImage.fromarray(display_img) 
        
        # saving the final output  
        # as a PNG file 
    data.save("output.png")


def crop(image):
    
    image = cv2.imread("output.jpg")
    height, width = image.shape[:2]

# Iterate over the pixels of the image
    for y in range(height):
        for x in range(width):
            # Get the pixel value at (x, y)
            pixel = image[y, x]
            if pixel == (255,0,0):
                image = image[x: ]


            # Print the pixel value
            print(pixel)



image_path = "1sample_report_pdf.pdf"
border(image_path)

#def get_table():
