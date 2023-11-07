import cv2

image = cv2.imread("D:\Study\github\CV_Introduction\Images\documentscanner2.jpg")

#setting the threoshold values

t_lower = 400
t_higher = 500

# Apply Canny Edge detector

edge = cv2.Canny(image, t_lower, t_higher)

cv2.imshow("Output", edge)

cv2.waitKey(0)

cv2.destroyAllWindows()
