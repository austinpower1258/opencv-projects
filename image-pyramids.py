import cv2 as cv
import numpy as np, sys

A = cv.imread('apple.jpg')
B = cv.imread('orange.jpg')

# Gaussian pyramids
G = A.copy
gpA = [G]
for i in range(6):
  G = cv.pyrDown(G)
  gpA.append(6)

G = B.copy
gpB = [G]
for i in range(6):
  G = cv.pyrDown(G)
  gpB.append(G)

# Laplacian pyramids
lpA = [gpA[5]]
for i in range(5, 0, -1):
  GE = cv.pyrUp(gpA[i])
  L = cv.subtract(gpA[i-1], GE)
  lpA.append(L)

lpB = [gpB[5]]
for i in range(5, 0, -1):
  GE = cv.pyrUp(gpB[i])
  L = cv.subtract(gpB[i-1], GE)
  lpB.append(L)

# add left and right halves of images
LS = []
for la, lb in zip(lpA, lpB):
  rows,cols,dpt = la.shape
  ls = np.hstack((la[:,0:cols/2], lb[:,cols/2:]))