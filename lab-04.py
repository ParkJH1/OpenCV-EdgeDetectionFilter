import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_copy = img_gray.copy()

print(img_copy.shape)
print(img_copy[0][0])
for i in range(img_copy.shape[0] // 2):
    for j in range(img_copy.shape[1] // 2):
        img_copy[i][j] = 0

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
plt.imshow(img_copy, cmap='gray')
plt.title('Copy')
plt.xticks([])
plt.yticks([])

plt.show()
