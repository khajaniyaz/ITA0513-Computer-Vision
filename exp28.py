
import cv2

# Download yolov8n.pt before running
model = None

try:
    from ultralytics import YOLO
    model = YOLO("yolov8n.pt")
except ImportError:
    print("Install ultralytics: pip install ultralytics")

if model is not None:
    cap = cv2.VideoCapture(
        r"C:\Users\reddy\Downloads\video.mp4"
    )

    vehicle_ids = [2, 3, 5, 7]  # car, motorcycle, bus, truck

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        results = model(frame, verbose=False)

        for box in results[0].boxes:
            class_id = int(box.cls[0])

            if class_id in vehicle_ids:
                x1, y1, x2, y2 = map(
                    int, box.xyxy[0].tolist()
                )
                label = model.names[class_id]

                cv2.rectangle(
                    frame, (x1, y1), (x2, y2),
                    (0, 255, 0), 2
                )
                cv2.putText(
                    frame, label, (x1, y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.6, (0, 255, 0), 2
                )

        cv2.imshow("Vehicle Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
