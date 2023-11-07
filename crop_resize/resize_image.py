import cv2

image = cv2.imread("D:\Study\github\CV_Introduction\Images\car.jpg")


resized_image = cv2.resize(image,(600,400))

cv2.imshow("Original",image)

cv2.imshow("Resized",resized_image)

cv2.waitKey(0)

cv2.destroyAllWindows()