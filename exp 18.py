
import cv2

# Read the original image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Display the original image
    cv2.imshow("Original Image", img)

    # Select Region of Interest (ROI)
    roi = img[50:200, 50:200]

    # Crop the selected ROI
    cv2.imshow("Cropped Image", roi)
    cv2.imwrite("cropped_image.jpg", roi)

    # Copy the ROI
    copied_roi = roi.copy()

    # Paste the copied ROI at a new location
    h, w = copied_roi.shape[:2]

    # Destination coordinates (top-left corner)
    x, y = 250, 100

    # Check whether the ROI fits inside the image
    if y + h <= img.shape[0] and x + w <= img.shape[1]:
        result = img.copy()
        result[y:y+h, x:x+w] = copied_roi

        # Display and save the result
        cv2.imshow("Image with Pasted ROI", result)
        cv2.imwrite("pasted_image.jpg", result)

        print("ROI cropped, copied and pasted successfully!")
    else:
        print("Error: Destination area is outside the image.")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
