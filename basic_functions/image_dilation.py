import cv2
import numpy as np

kernel = np.ones((5,5), np.uint8)

image = cv2.imread("D:\Study\github\CV_Introduction\Images\documentscanner2.jpg")

#setting the threoshold values

t_lower = 400
t_higher = 500

# Apply Canny Edge detector

img_canny = cv2.Canny(image, t_lower, t_higher)

# dilation - dilation increase the thickness of edges

image_dilation = cv2.dilate(img_canny, kernel, iterations=1)


cv2.imshow("Canny", img_canny)

cv2.imshow("Dilated", image_dilation)

cv2.waitKey(0)

cv2.destroyAllWindows()
