#pyzbar function from the pyzbar library to decode find the barcodes present within the image
from pyzbar import pyzbar
import argparse
import cv2
import imutils

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True, help = "Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = imutils.resize(image, width = 600)
barcodes = pyzbar.decode(image)

#iterate over the obtained barcodes
for barcode in barcodes:
    #extracting the rectangle containing the barcode
    #and constructing a border to bound it
    (x, y, w, h) = barcode.rect
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #coverting the data type of the barcode to string 
    barcodeData = barcode.data.decode("utf-8")
    barcodeType = barcode.type

    #writing the info encoded by the qr code into the image itself above the boundaries
    text = "{} ({})".format(barcodeData, barcodeType)
    cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    
    #printing the info into the terminal
    print(barcodeData, barcodeType)
    print("[INFO] Found {} barcode: {}". format(barcodeType, barcodeData))
    cv2.waitKey(0)

#print the output image
cv2.imshow("Image", image)
cv2.waitKey(0)
