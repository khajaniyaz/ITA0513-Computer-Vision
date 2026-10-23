
import cv2

# Read the original image
img = cv2.imread("image.jpg")

if img is None:
    print("Error: Image not found!")
else:
    # Copy the original image
    watermarked = img.copy()

    # Watermark text
    text = "Copyright"

    # Set font properties
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)  # White color (BGR)
    thickness = 2

    # Get image dimensions
    h, w = img.shape[:2]

    # Calculate text size
    text_size, baseline = cv2.getTextSize(
        text, font, font_scale, thickness
    )

    # Position watermark at bottom-right
    x = w - text_size[0] - 20
    y = h - 20

    # Insert watermark
    cv2.putText(
        watermarked, text, (x, y),
        font, font_scale, color, thickness,
        cv2.LINE_AA
    )

    # Display original and watermarked images
    cv2.imshow("Original Image", img)
    cv2.imshow("Watermarked Image", watermarked)

    # Save the watermarked image
    cv2.imwrite("watermarked_output.jpg", watermarked)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    print("Watermark inserted successfully!")
