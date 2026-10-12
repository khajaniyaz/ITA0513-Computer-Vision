import cv2

# Read the video
cap = cv2.VideoCapture("video.mp4")

if not cap.isOpened():
    print("Error: Cannot open video!")
else:
    # Display video in slow motion
    print("Slow Motion: Press any key to continue")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Slow Motion", frame)

        # Delay of 100 ms for slow motion
        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Reopen video for fast motion
    cap = cv2.VideoCapture("video.mp4")

    print("Fast Motion: Press q to exit")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        cv2.imshow("Fast Motion", frame)

        # Delay of 10 ms for fast motion
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
