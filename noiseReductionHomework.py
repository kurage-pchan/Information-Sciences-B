#source https://docs.opencv.org/3.4/dd/dd7/tutorial_morph_lines_detection.html

import cv2
import sys
import numpy as np
import matplotlib.pyplot as plt

class ImageProcessingUtils:
    def cleanIsolatedPoints(img,kernel):
        img = 255-img
        erosion = cv2.erode(img,kernel,iterations = 1)
        delation = cv2.dilate(img,kernel,iterations = 1)
        img = 255-img
        print(img.shape)
        plt.imshow(img,cmap="gray")
        plt.show()

    def findLinesCanny(gray_image):
        gray_image = 255 - gray_image
        t_lower = 100
        t_upper = 150

        edge = cv2.Canny(gray_image,t_lower,t_upper)
        plt.imshow(edge, cmap="gray")
        plt.show()


    def detectVerticalLines(gray):
        vertical = np.copy(gray)

        vertical = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 35, -2)
        # plt.imshow(vertical, cmap = "gray")
        # plt.imsave("aaa.jpg", vertical, cmap="gray")
        # plt.show()

        rows = vertical.shape[1]
        vertical_size = rows // 50
        print(vertical_size)
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1,vertical_size))
        vertical = cv2.erode(vertical, verticalStructure)
        vertical = cv2.dilate(vertical, verticalStructure)

        # return resulting image
        plt.imshow( vertical, cmap="gray")
        plt.show()



def main(argv):
    print("argv",argv[1])
    img=cv2.imread(argv[1],cv2.IMREAD_GRAYSCALE)
    if img is None:
        print ('Error opening image: ' + argv[0])
        return -1
    if len(img.shape) != 2:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        gray = img

    kernel = np.ones((2, 2), np.uint8)
    isolated=ImageProcessingUtils.cleanIsolatedPoints(gray,kernel[0])

    canny=ImageProcessingUtils.findLinesCanny(gray)

    verticalLines=ImageProcessingUtils.detectVerticalLines(255-gray)


if __name__ == '__main__':
    main(sys.argv)
