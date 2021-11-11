import cv2

img = cv2.imread('chess/chess.jfif')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite('chess_grayscale.jpg', gray)
