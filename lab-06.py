import cv2
import numpy as np
import matplotlib.pyplot as plt


def filter_func(src, dst, filter):
    h = src.shape[0]
    w = src.shape[1]

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            sum = 0
            print('process...', i, j, '[', h, w, ']')
            for k1 in range(-1, 2):
                for k2 in range(-1, 2):
                    sum += filter[k1 + 1][k2 + 1] * src[i + k1][j + k2]
            dst[i][j] = sum
    print('done.')

filter = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.float64)
# filter = np.array([[-1, 0, 0],
#                    [0, 1, 0],
#                    [0, 0, 0]], dtype=np.float32)

# filter = np.array([[1, 1, 1],
#                    [1, -8, 1],
#                    [1, 1, 1]], dtype=np.float32)


img = cv2.imread('image/3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_gray = np.float64(img_gray)

img_filter = img_gray.copy()
filter_func(img_gray, img_filter, filter)

plt.subplot(1, 3, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Gray')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 3, 3)
plt.imshow(img_filter, cmap='gray')
plt.title('img_filter')
plt.xticks([])
plt.yticks([])

plt.show()
