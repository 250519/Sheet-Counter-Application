import cv2
import numpy as np
from scipy.signal import find_peaks
from matplotlib import pyplot as plt


def preprocess_image(image):
    # Adjust from -100 to 100
    brightness = -80
    contrast = 3
    # Convert to grayscale
    # Apply the brightness and contrast adjustment
    image=np.array(image)
    img = cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)

    # Invert the image (if needed)
    # thresh = cv2.bitwise_not(thresh)

    return thresh


def count_sheets(image, min_distance=10, prominence=10, edge_threshold1=30, edge_threshold2=90):
    # Read the image
    # image = cv2.imread(image_path)
    if image is None:
        raise ValueError("Could not read the image")

    # Preprocess the image
    preprocessed = preprocess_image(image)

    # Apply edge detection
    edges = cv2.Canny(preprocessed, edge_threshold1, edge_threshold2)

    # Sum the edge pixels along each row
    edge_profile = np.sum(edges, axis=1)

    # Find peaks in the edge profile
    peaks, _ = find_peaks(edge_profile, distance=min_distance, prominence=prominence)

    # Count the number of peaks (sheets)
    sheet_count = len(peaks)//2
    # Divide by 2 because it is detecting two horizontal lines per sheets

    return sheet_count


def visualize_results(image, edges, edge_profile, peaks):
    # Visualize the results
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))

    ax1.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax1.set_title("Original Image")
    ax1.axis('off')

    ax2.imshow(edges, cmap='gray')
    ax2.set_title("Edge Detection")
    ax2.axis('off')

    ax3.plot(edge_profile)
    ax3.plot(peaks, edge_profile[peaks], "x")
    ax3.set_title(f"Edge Profile (Sheet Count: {len(peaks)})")
    ax3.set_xlabel("Row")
    ax3.set_ylabel("Edge Pixel Sum")

    plt.tight_layout()
    plt.show()


# # Main execution
# if __name__ == "__main__":
#     import matplotlib.pyplot as plt
#
#     image_path = "Images/2.jpeg"  # Replace with your image path
#
#     # Hyperparameters
#     min_distance = 10  # Minimum distance between peaks
#     prominence = 10  # Minimum prominence of peaks
#     edge_threshold1 = 50  # Lower threshold for edge detection
#     edge_threshold2 = 150  # Upper threshold for edge detection
#
#     try:
#         sheet_count, edges, edge_profile, peaks = count_sheets(
#             image_path, min_distance, prominence, edge_threshold1, edge_threshold2
#         )
#         print(f"Estimated number of sheets: {sheet_count}")
#
#         # Visualize results
#         image = cv2.imread(image_path)
#         visualize_results(image, edges, edge_profile, peaks)
#
#     except Exception as e:
#         print(f"An error occurred: {str(e)}")



