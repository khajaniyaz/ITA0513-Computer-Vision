
import cv2
import time

cap = cv2.VideoCapture(r"C:\Users\reddy\Downloads\video.mp4")
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

if not frames:
    print("Video not found")
else:
    for frame in reversed(frames):
        cv2.imshow("Reverse Slow Motion", frame)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
