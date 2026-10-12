import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply erosion
    eroded = cv2.erode(img, kernel, iterations=1)

    # Display original and eroded images
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(eroded, cv2.COLOR_BGR2RGB))
    plt.title("Eroded Image")
    plt.axis("off")

    plt.show()

    # Save the eroded image
    cv2.imwrite("eroded_image.jpg", eroded)

    print("Image erosion completed successfully!")
