import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE) # queryImage
img2 = cv2.imread('box_in_scene.png',cv2.IMREAD_GRAYSCALE) # refImage

# Find keypoints and descriptors with SIFT
sift = cv2.SIFT_create(contrastThreshold=0.1)
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# Perform BF match with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1, des2, k=2)

# Apply ratio test to filter matches
good = []
for m, n in matches:
    if m.distance < 0.8*n.distance:
        good.append(m)
        
# Filter 10 best matches
best10 = sorted(good, key=lambda x: x.distance)[:10]

# Draw good matches over images
img3 = cv2.drawMatches(img1, kp1, img2, kp2, best10, None)
plt.imshow(img3), plt.show()