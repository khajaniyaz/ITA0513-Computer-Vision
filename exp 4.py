import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply histogram equalization
    equalized = cv2.equalizeHist(gray)

    # Display original and equalized images
    plt.subplot(1, 2, 1)
    plt.imshow(gray, cmap="gray")
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(equalized, cmap="gray")
    plt.title("Histogram Equalized Image")
    plt.axis("off")

    plt.show()

    # Save the equalized image
    cv2.imwrite("equalized_image.jpg", equalized)

    print("Histogram equalization completed successfully!")
