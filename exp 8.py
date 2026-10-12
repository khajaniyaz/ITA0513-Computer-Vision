import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Create a kernel
    kernel = np.ones((5, 5), np.uint8)

    # Apply dilation
    dilated = cv2.dilate(img, kernel, iterations=1)

    # Display original image
    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title("Original Image")
    plt.axis("off")

    # Display dilated image
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(dilated, cv2.COLOR_BGR2RGB))
    plt.title("Dilated Image")
    plt.axis("off")

    plt.show()

    # Save the dilated image
    cv2.imwrite("dilated_image.jpg", dilated)

    print("Image dilation completed successfully!")
