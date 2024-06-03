
import cv2

def nothing(x):
    pass

# Parameter default value
nLayers = 3
formerNLayers = nLayers
contrast = 0
formerContrast = contrast
edge = 10
formerEdge = edge
# Create window and trackbar
win_name = 'source [ESC to quit]'
cv2.namedWindow(win_name)
cv2.createTrackbar('nLayers', win_name, nLayers, 7, nothing)
cv2.setTrackbarMin('nLayers', win_name, 1)
cv2.createTrackbar('contrastThreshold', win_name, contrast, 10, nothing)
cv2.setTrackbarMin('contrastThreshold', win_name, 0)
cv2.createTrackbar('edgeThreshold', win_name, edge, 20, nothing)
cv2.setTrackbarMin('edgeThreshold', win_name, 1)

img = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
sift = cv2.SIFT_create(0, nLayers)
keypoints = sift.detect(img)
img_with_kp = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv2.imshow(win_name, img_with_kp)

while True:
    nLayers = cv2.getTrackbarPos('nLayers', win_name)
    contrast = cv2.getTrackbarPos('contrastThreshold',win_name)/100
    edge = cv2.getTrackbarPos('edgeThreshold',win_name)
    if nLayers != formerNLayers or contrast != formerContrast or edge != formerEdge:
        sift = cv2.SIFT_create(0,nLayers,contrastThreshold= contrast,edgeThreshold= edge)
        keypoints = sift.detect(img)
        print(len(keypoints))
        img_with_kp = cv2.drawKeypoints(img, keypoints, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow(win_name, img_with_kp)
        formerNLayers = nLayers  
        formerContrast = contrast
        formerEdge = edge
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
