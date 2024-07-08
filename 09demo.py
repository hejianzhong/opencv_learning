import numpy as np
import cv2

img = cv2.imread("data/img/math.png", 1)
grayImg = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
_, threshImg = cv2.threshold(grayImg, 180, 255, cv2.THRESH_BINARY)
adaptiveThreshImg = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 3, 0)
kernel = np.ones((2,2))
# kernel = cv2.getGaussianKernel(2, 0.5)
erodeImg = cv2.erode(adaptiveThreshImg, kernel, iterations=1)
dilateImg = cv2.dilate(erodeImg, kernel, iterations=1)
cv2.imshow("dilateImg", dilateImg)

openOp = cv2.morphologyEx(adaptiveThreshImg, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("openOp", openOp)

cv2.waitKey(0)