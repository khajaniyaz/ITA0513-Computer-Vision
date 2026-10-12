import cv2
import matplotlib.pyplot as plt

# Function to analyze the color histogram
def analyze_histogram(image_path):
    # Read the input image
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    # Define colors for each channel
    colors = ('b', 'g', 'r')
    channel_names = ('Blue', 'Green', 'Red')

    # Plot histogram for each color channel
    plt.figure(figsize=(8, 5))

    for i, color in enumerate(colors):
        histogram = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histogram, color=color, label=channel_names[i])

    plt.title("Color Histogram Analysis")
    plt.xlabel("Pixel Intensity (0-255)")
    plt.ylabel("Number of Pixels")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    print("Histogram analysis completed successfully!")

# Call the function
analyze_histogram("image.jpg")
