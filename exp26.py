
import cv2

cap = cv2.VideoCapture(r"C:\Users\reddy\Downloads\Screen Recording 2026-10-03 155403.mp4")
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

fps = cap.get(cv2.CAP_PROP_FPS)
cap.release()

if frames:
    h, w = frames[0].shape[:2]
    out = cv2.VideoWriter(
        "reverse_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps if fps > 0 else 25,
        (w, h)
    )

    for frame in reversed(frames):
        out.write(frame)

    out.release()
    print("Reverse video created successfully")
else:
    print("Video not found or contains no frames")
