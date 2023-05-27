import cv2
img = cv2.imread('virat.jpg')

canny = cv2.Canny(img, 90, 130)
sobelx = cv2.Sobel(img, -1, 1, 0)
sobely = cv2.Sobel(img, -1, 0, 1)
sobelxy = cv2.addWeighted(sobelx, 0.3, sobely, 0.8, 1.3)

laplacian = cv2.Laplacian(img, -1)

cv2.imshow('canny image', canny)
cv2.imshow('Original image', img)
cv2.imshow('Sobel X ', sobelx)
cv2.imshow("sobel xy ", sobelxy)
cv2.imshow('laplacian', laplacian)

cv2.waitKey()