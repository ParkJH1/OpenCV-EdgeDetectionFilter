import cv2
import numpy as np
from matplotlib import pyplot as plt


def filter_func(src, dst, filter):
    h = src.shape[0]
    w = src.shape[1]

    for j in range(1, h - 1):
        for i in range(1, w - 1):
            conv = 0
            for k1 in range(-1, 2):
                for k2 in range(-1, 2):
                    sum = 0
                    for k3 in range(-1, 2):
                        sum += src[j + k1][i + k3] * filter[k3 + 1][k2 + 1]
                    conv += sum
            dst[j][i] = max(0, min(conv + 128, 255))


# filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float32)
filter = np.array([[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]], dtype=np.float32)

# loading image
#img0 = cv2.imread('SanFrancisco.jpg',)
# img0 = cv2.imread('windows.jpg',)
img0 = cv2.imread('image.jpg',)

# converting to gray scale
gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)

# remove noise
img = cv2.GaussianBlur(gray,(3,3),0)
plt.subplot(3,2,1),plt.imshow(img,cmap = 'gray')
plt.title('input'), plt.xticks([]), plt.yticks([])


# convolute with proper kernels
laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y

res = img.copy()
# filter_func(img, res, filter)
res = cv2.filter2D(img, ddepth=cv2.CV_64F, kernel=filter)

plt.subplot(3,2,2),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,3),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,4),plt.imshow(sobelx,cmap = 'gray')
plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,5),plt.imshow(sobely,cmap = 'gray')
plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
plt.subplot(3,2,6),plt.imshow(res,cmap = 'gray')
plt.title('My Laplacian'), plt.xticks([]), plt.yticks([])

plt.show()
