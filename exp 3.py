import cv2

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect edges using Canny
    edges = cv2.Canny(gray, 100, 200)

    # Display the original image
    cv2.imshow("Original Image", img)

    # Display the image outline
    cv2.imshow("Canny Edge Detection", edges)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()
