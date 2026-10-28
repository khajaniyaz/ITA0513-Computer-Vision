
import cv2
import pytesseract

# Update this path if Tesseract is installed elsewhere
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

cap = cv2.VideoCapture(r"C:\Users\reddy\Downloads\video.mp4")
all_text = []

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray).strip()

    if text:
        print("Detected text:", text)
        all_text.append(text)

cap.release()

with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(all_text))

print("Text saved to extracted_text.txt")
