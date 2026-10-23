import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Convert grayscale image to float32
    gray = np.float32(gray)

    # Apply Harris Corner Detection
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)

    # Dilate the result to mark corners clearly
    dst = cv2.dilate(dst, None)

    # Mark detected corners in red
    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    # Display the result
    cv2.imshow("Harris Corner Detection", img)

    # Save the output image
    cv2.imwrite("harris_corners.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Harris corner detection completed successfully!")
