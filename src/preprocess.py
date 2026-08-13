import cv2 as cv
import numpy as np

def preprocess_image(image_path):
    img = cv.imread(image_path)

    greyscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    blurred_img = cv.GaussianBlur(greyscale_img, (5, 5), 0)

    binary_img = cv.adaptiveThreshold(blurred_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)

    return binary_img

if __name__ == "__main__":
    preprocessed_image = preprocess_image('data/receipts/sample_receipt.jpg')
    cv.imshow('receipt', preprocessed_image)
    cv.waitKey(0)
    cv.destroyAllWindows()

