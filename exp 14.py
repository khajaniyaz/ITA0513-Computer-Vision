import cv2
import numpy as np

# Read the input image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    rows, cols = img.shape[:2]

    # Four points from the original image
    pts1 = np.float32([
        [50, 50],
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    # Four points for the transformed image
    pts2 = np.float32([
        [0, 0],
        [cols, 0],
        [0, rows],
        [cols, rows]
    ])

    # Calculate perspective transformation matrix
    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply perspective transformation
    result = cv2.warpPerspective(img, matrix, (cols, rows))

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformation", result)

    # Save transformed image
    cv2.imwrite("perspective_output.jpg", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Perspective transformation completed successfully!")
