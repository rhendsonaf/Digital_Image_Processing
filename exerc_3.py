from turtle import color
import numpy as np
import cv2 as cv

img = cv.imread("imgs/bolhas.png", 0)

floodfill = img.copy()

h, w = img.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

colorToFill = 1
for i in range (0, h):
    for j in range(0, w):
        if (img.item(i, j) == 255):
            cv.floodFill(floodfill, mask, (j,i), colorToFill)
            if (img.item(i+1, j+1) == colorToFill):
                colorToFill += 1

cv.imshow('Mask', mask)
cv.imshow('Original', img)
cv.imshow('FloodFill', floodfill)

cv.waitKey()

cv.destroyAllWindows()