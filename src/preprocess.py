import cv2 as cv
import numpy as np

img = cv.imread('data/receipts/sample_receipt.jpg')

greyscale_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

blurred_img = cv.GaussianBlur(greyscale_img, (5, 5), 0)

binary_img = cv.adaptiveThreshold(blurred_img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)




cv.imshow('receipt', binary_img)
cv.waitKey(0)
cv.destroyAllWindows()
