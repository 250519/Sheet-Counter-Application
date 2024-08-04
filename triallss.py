import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.signal import find_peaks

img=cv2.imread('Images/4.jpeg')
# def update_image(val):
#     brightness = cv2.getTrackbarPos('Brightness', 'Image') - 100
#     contrast = cv2.getTrackbarPos('Contrast', 'Image') / 50.0
#     adjusted_image = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
#     cv2.imshow('Image', adjusted_image)
#
# # Create a window
# cv2.namedWindow('Image')
#
# # Create trackbars for brightness and contrast adjustment
# cv2.createTrackbar('Brightness', 'Image', 100, 200, update_image)
# cv2.createTrackbar('Contrast', 'Image', 50, 150, update_image)
# cv2.imshow('Imagec', img)

brightness = -80  # Adjust from -100 to 100
contrast = 3   # Adjust from 0.0 to 3.0

# Apply the brightness and contrast adjustment
img = cv2.convertScaleAbs(img, alpha=contrast, beta=brightness)
grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('Imageb',adjusted_image)
blur=cv2.GaussianBlur(grey,[5,5],cv2.BORDER_DEFAULT)

thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# edges=cv2.Canny(blur,125,160)
cv2.imshow('threshold',thresh)

# cv2.imshow('blur',blur)
lines = cv2.HoughLinesP(thresh, 1, np.pi/180, threshold=100,
                            minLineLength=250, maxLineGap=2)
# Filter horizontal lines
horizontal_lines = []
for line in lines:
    x1, y1, x2, y2 = line[0]
    print(x1, y1, x2, y2)
    cv2.line(img,(x1,y1),(x2,y2),(255,0,0),2)
    if abs(y2 - y1) < 10:  # Consider lines with small vertical difference
        horizontal_lines.append((y1 + y2) // 2)
# min_distance=15
# prominence=20
# edge_threshold1=30
# edge_threshold2=90
# # Apply edge detection
# edges = cv2.Canny(blur, edge_threshold1, edge_threshold2)
# cv2.imshow('Canny',edges)
#     # Sum the edge pixels along each row
# edge_profile = np.sum(thresh, axis=1)
# print(edge_profile)
#     # Find peaks in the edge profile
# peaks, _ = find_peaks(edge_profile, distance=min_distance, prominence=prominence)
#
#     # Count the number of peaks (sheets)
# sheet_count = len(peaks)
# Sort and remove duplicates
# horizontal_lines = sorted(set(horizontal_lines))
#
# # Count sheets by measuring gaps between lines
# sheet_count = 0
# prev_y = None
# min_gap = 6  # Minimum gap between sheets
#
# for y in horizontal_lines:
#     if prev_y is None or y - prev_y > min_gap:
#         sheet_count += 1
#     prev_y = y
#
print(sheet_count)
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 6))


ax1.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
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

cv2.imshow('img',img)
cv2.waitKey(0)