from PIL import Image

# Open the image
img = Image.open("image.jpg")

# Rotate 270 degrees clockwise
rotated_img = img.rotate(90, expand=True)

# Display the rotated image
rotated_img.show()

# Save the rotated image
rotated_img.save("rotated_image.jpg")

print("Image rotated 270 degrees clockwise successfully!")
