import cv2

import numpy as np

import pytesseract

import matplotlib.pyplot as plt

from PIL import Image
import string
import re



# Recognize text with tesseract for python

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Path of working folder on Disk

src_path = r"D:/Faculty" # source of images



def get_string(img_path):

    # Read image with opencv
    # print("soka1")
    img = cv2.imread(img_path)
    # print("soka")


    # Convert to gray

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print("sssss")


    # Apply dilation and erosion to remove some noise

    #kernel = np.ones((2, 2), np.uint8)

    kernel =cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2, 2))



    #img = cv2.dilate(img, kernel, iterations=1)

    img_erode = cv2.erode(img, kernel, iterations=1)



    # Write image after removed noise

    #plt.imshow(img1)

    #cv2.imshow('removed_noise.png',img_erode)

    #cv2.waitKey(0)







    # Apply threshold to get image with only black and white

    (thresh,img_threshold) = cv2.threshold(img, 117, 255, cv2.THRESH_BINARY)

    #img_threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 33, 2)

    #cv2.imshow('image_threshold.png',img_threshold)

    #cv2.waitKey(0)



    # Write the image after apply opencv to do some ...

    #cv2.imwrite(src_path + "thres.png", img)



    # Recognize text with tesseract for python

    result = pytesseract.image_to_string(img_path,lang='eng+ara')





    return result



# print ("------ Done -------")
# Function to extract all the numbers from the given string
def Number(str):
    array = re.findall(
        r'[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]+|[0-9][0-9][0-9][0-9][-|" "][0-9][0-9][0-9][0-9][-|" "][0-9][0-9][0-9][0-9][-|" "][0-9][0-9][0-9]+',
        str)
    if (len(array) > 1):
        if (array[0] == array[1]):
            array = array[0]
        elif (array[0] != array[1] or array[0] != array[1] != array[2]):
            return array[0]
        else:
            array = array[0]
    return ''.join(array)

def getCardNO(imageName):
    # imagePath = "../" + imageName
    str = get_string(imageName)
    array = Number(str)
    array = array.replace("-", "").replace(" ", "")
    x = int(array)
    # print(x)
    return (x)

def NameC(imageName):
    # imagePath = "../" + imageName
    imagePath = get_string(imageName)
    ss = "i can't detect the sim card :("

    if (re.findall(r'etisalat|اتصالات|Etisalat|"*إتصالات|"*556', imagePath)):

        ss = "etisalat"

    elif (re.findall(r'فودافون|VODAFONE|vodafone|كارت لفرحة|فونلون|"*585*"|Vodafone', imagePath)):

        ss = "vodafone"

    elif (re.findall(r'اورانج|orange|Orange|اوراتج|اورائج', imagePath)):

        ss = "orange"

    elif (re.findall(r'we|WE', imagePath)):

        ss = "we"

    return ss


# getCardNO("media/26.jpg")
# ss = NameC("media/26.jpg")
#ss = ss.translate({ord(c): None for c in string.whitespace})
#ss= ss.replace("-", "")
# print("my company is " + (ss))


            # found = True # Not necessary
#print ('--- Start recognize text from image ---')
# print (get_string("D:/Faculty/26.jpg"))
#print (Name(get_string("C:/Program Files/Tesseract-OCR/Temp/8.png")))
#print ("------ Done -------")