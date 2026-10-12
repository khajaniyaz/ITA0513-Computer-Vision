import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread("C:/slot a/image.jpg")

# Check whether the image was loaded
if img is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blur = cv2.GaussianBlur(img, (15, 15), 0)

    # Convert BGR to RGB for displaying
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    blur_rgb = cv2.cvtColor(blur, cv2.COLOR_BGR2RGB)

    # Display original and blurred images
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(img_rgb)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(blur_rgb)
    plt.title("Gaussian Blur")
    plt.axis("off")

    plt.tight_layout()
    plt.show()

    # Save the blurred image
    cv2.imwrite("C:/slot a/blurred_image.jpg", blur)

    print("Gaussian Blur completed successfully!")
