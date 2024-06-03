import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('nasa_logo.png', cv2.IMREAD_GRAYSCALE) # queryImage
img2 = cv2.imread('nasa_center_2.png',cv2.IMREAD_GRAYSCALE) # refImage

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
        
# Draw good matches over images
#img3 = cv2.drawMatches(img1, kp1, img2, kp2, good, None)

# Extract matched points
ptsA = np.zeros((len(good),2), dtype= "float")
ptsB = np.zeros((len(good),2), dtype= "float")
for (i,m) in enumerate(good):
    ptsA[i] = kp1[m.queryIdx].pt
    ptsB[i] = kp2[m.trainIdx].pt

# Find homography matrix
H, mask = cv2.findHomography(ptsA, ptsB, cv2.RANSAC)
matchesMask = mask.ravel().tolist()

h,w = img1.shape
pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
dst = cv2.perspectiveTransform(pts,H)

img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3,cv2.LINE_AA)

draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                   singlePointColor = None,
                   matchesMask = matchesMask, # draw only inliers
                   flags = 2)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,good,None,**draw_params)

plt.imshow(img3,cmap='gray'), plt.show()