import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_dx = img_gray.copy()
img_dy = img_gray.copy()

for j in range(img_gray.shape[1]):
    for i in range(img_gray.shape[0] - 1):
        img_dx[i][j] = img_gray[i + 1][j] - img_gray[i][j]


for i in range(img_gray.shape[0]):
    for j in range(img_gray.shape[1] - 1):
        img_dy[i][j] = img_gray[i][j + 1] - img_gray[i][j]

plt.subplot(2, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Gray')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 3)
plt.imshow(img_dx, cmap='gray')
plt.title('img_dx')
plt.xticks([])
plt.yticks([])

plt.subplot(2, 2, 4)
plt.imshow(img_dy, cmap='gray')
plt.title('img_dy')
plt.xticks([])
plt.yticks([])

plt.show()
