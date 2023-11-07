import cv2

image = cv2.imread("D:\Study\github\CV_Introduction\Images\car.jpg")

print("Original image shape", image.shape)

img_cropped = image[0:200,200:500]

cv2.imshow("Output",img_cropped )

cv2.imshow("Original", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
