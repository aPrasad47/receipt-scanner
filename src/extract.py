import pytesseract as pt
from preprocess import preprocess_image

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

image_path = 'data/receipts/sample_receipt.jpg'
preprocessed_image = preprocess_image(image_path)

config = rf'--oem 3 --psm 4'
text = pt.image_to_string(preprocessed_image, config=config)
print(text)
