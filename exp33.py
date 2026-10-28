
import cv2
import numpy as np

img = np.ones((400, 400, 3), dtype=np.uint8) * 255

cv2.rectangle(img, (80, 100), (320, 300),
              (0, 0, 255), 3)

cv2.imshow("Rectangle", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
