
import cv2

img = cv2.imread(r"C:\Users\reddy\Downloads\face.jpg")

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades +
        "haarcascade_frontalface_default.xml"
    )

    faces = cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=5
    )

    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),
                      (0, 255, 0), 2)

    cv2.imshow("Face Detection", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
