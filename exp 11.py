from PIL import Image

# Open the image
img = Image.open("image.jpg")

# Rotate 180 degrees clockwise
rotated_img = img.rotate(180)

# Display the rotated image
rotated_img.show()

# Save the rotated image
rotated_img.save("rotated_image.jpg")

print("Image rotated and saved successfully!")
