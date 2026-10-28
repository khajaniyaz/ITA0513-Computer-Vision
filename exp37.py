
import cv2
import numpy as np

img = cv2.imread(r"C:\Users\reddy\Downloads\tinea.jpg")

if img is None:
    print("Image not found")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Example: extract green-colored objects
    lower = np.array([35, 40, 40])
    upper = np.array([85, 255, 255])

    mask = cv2.inRange(hsv, lower, upper)
    result = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Original", img)
    cv2.imshow("Foreground", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
