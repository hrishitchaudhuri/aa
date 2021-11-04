import cv2

img = cv2.imread('atj.jfif')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('atj_grayscale.jpg', gray)
