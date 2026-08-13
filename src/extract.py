import pytesseract as pt
from preprocess import preprocess_image

pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract"

def extract_text_from_image(image_path):
    preprocessed_image = preprocess_image(image_path)
    config = rf'--oem 3 --psm 4'
    text = pt.image_to_string(preprocessed_image, config=config)
    return text

if __name__ == "__main__":
    image_path = 'data/receipts/sample_receipt.jpg'
    extracted_text = extract_text_from_image(image_path)
    print(extracted_text)