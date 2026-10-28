
import cv2
import numpy as np

width = int(input("Enter image width: "))
height = int(input("Enter image height: "))
size = 60

img = np.ones((height, width, 3), dtype=np.uint8) * 255

# OpenCV uses BGR color order
cv2.rectangle(img, (0, 0), (size, size), (0, 0, 0), -1)
cv2.rectangle(img, (width-size, 0),
              (width-1, size), (255, 0, 0), -1)
cv2.rectangle(img, (0, height-size),
              (size, height-1), (0, 255, 0), -1)
cv2.rectangle(img, (width-size, height-size),
              (width-1, height-1), (0, 0, 255), -1)

cv2.imshow("Colored Corner Boxes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
