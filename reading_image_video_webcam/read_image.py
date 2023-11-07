import cv2

#To read the image i will use imread function
image = cv2.imread("../Images/car.jpg")

#Display the output image
cv2.imshow("Output", image)
cv2.waitKey(0)

