import cv2
import matplotlib.pyplot as plt

img = cv2.imread('image/3.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 2, 1)
plt.imshow(img, cmap='gray')
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(1, 2, 2)
plt.imshow(img_gray, cmap='gray')
plt.title('Gray')
plt.xticks([])
plt.yticks([])

plt.show()
