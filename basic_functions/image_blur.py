import cv2

image = cv2.imread("D:\Study\github\CV_Introduction\Images\car.jpg")

#Kernel Vaues should be an ODD number

imgBlur = cv2.GaussianBlur(image, (121,121), 0)

cv2.imshow("Output", imgBlur)

cv2.imshow("Original", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
