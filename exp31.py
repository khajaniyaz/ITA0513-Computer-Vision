
import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, result = cv2.threshold(gray, 127, 255,
                              cv2.THRESH_BINARY)

    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(result, cmap="gray")
    plt.title("Segmented Image")
    plt.axis("off")

    plt.show()
