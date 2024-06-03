import cv2
import matplotlib.pyplot as plt

def unpackSIFTOctave(kpt):
    """unpackSIFTOctave(kpt)->(octave,layer,scale)
    @created by Silencer at 2018.01.23 11:12:30 CST
    @brief Unpack Sift Keypoint by Silencer
    @param kpt: cv2.KeyPoint (of SIFT)
    """
    _octave = kpt.octave
    octave = _octave&0xFF
    layer  = (_octave>>8)&0xFF
    if octave>=128:
        octave |= -128
    if octave>=0:
        scale = float(1/(1<<octave))
    else:
        scale = float(1<<-octave)
    return (octave, layer, scale)

img = cv2.imread('box.png', cv2.IMREAD_GRAYSCALE)
# Constructor default params: nOctaveLayers = 3,
# contrastThreshold = 0.04, edgeThreshold = 10, sigma = 1.6
sift = cv2.SIFT_create() # construct
kp = sift.detect(img) # detect keypoints
foundKps = sorted(kp, key=lambda x: x.response, reverse=True)[:100]  # 3 largest keypoints
octaveLayers=[unpackSIFTOctave(kp) for kp in kp]
octaveLayers= sorted(octaveLayers, key=lambda x: x[0], reverse=True)[:10]  
img_with_kp = cv2.drawKeypoints(img, foundKps, img, None,cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

plt.imshow(img_with_kp)
plt.show()

