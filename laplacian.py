import cv2
import numpy as np


def filter_func(src, dst, filter):
    h = src.shape[0]
    w = src.shape[1]

    for j in range(1, h - 1):
        sum = 0
        for i in range(1, w - 1):
            sum += src[j - 1][i]
            sum += src[j][i - 1]
            sum += src[j + 1][i]
            sum += src[j][i + 1]
            sum -= 4 * src[j][i]
            dst[j][i] = max(0, min(sum + 128, 255))


# filter = np.zeros((3, 3), np.uint8)
filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)
img = cv2.imread('image.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(img,(3,3),0)

res = img.copy()
filter_func(img, res, filter)
cv2.imshow('img', img)
cv2.imshow('res', res)

res2 = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
cv2.imshow('res2', res)
cv2.waitKey(0)
