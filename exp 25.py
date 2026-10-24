import cv2

img = cv2.imread("image.jpg")

if img is None:
    print("Error: image.jpg not found")
    exit()

model = YOLOWorld("yolov8s-worldv2.pt")
model.set_classes(["watch", "wristwatch"])

results = model.predict(img, conf=0.15)

for result in results:
    annotated = result.plot()

    for box in result.boxes:
        print("Detected:", result.names[int(box.cls[0])])

    cv2.imshow("Watch Recognition", annotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
