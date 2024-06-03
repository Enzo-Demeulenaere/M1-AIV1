# Import functions and libraries
import numpy as np
import cv2
import matplotlib.pyplot as plt


BAYER_CFA = {"RGGB": 0, "BGGR": 1, "GRBG": 2, "GBRG":3}

img = cv2.imread("lighthouse.png")
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
newImg = np.zeros([img.shape[0],img.shape[1]])

def cfa_image(img, cfa="GRBG"):
    """ Return the CFA image from color image <img> (numpy array) with given <cfa>
    """

    newImg[1::2,0::2] = img[1::2,0::2,0] #R  
    newImg[0::2,1::2] = img[0::2,1::2,2] #B 
    newImg[0::2,0::2] = img[0::2,0::2,1] #G 
    newImg[1::2,1::2] = img[1::2,1::2,1] #G  

   # plt.imshow(newImg,cmap='gray')
   # plt.show()
    return newImg


def cfa_samples(cfa_img, channel, cfa="GRBG"):
    """ Return the CFA samples of <channel> ("R".."B") from CFA image <cfa_img> (numpy array) with given <cfa>
    """
    newImg = np.zeros([cfa_img.shape[0],cfa_img.shape[1]] )
    if (channel == "G"):
        newImg[0::2,0::2] = cfa_img[0::2,0::2] #G   
        newImg[1::2,1::2] = cfa_img[1::2,1::2] #G
    elif (channel == "R"):
        newImg[1::2,0::2] = cfa_img[1::2,0::2]
    else :
        newImg[0::2,1::2] = cfa_img[0::2,1::2]

    return newImg

def demat_bilin(img_name, cfa="GRBG", show=False, write= False):
    cfa_img = cfa_image(img_name,cfa)
    sampleR = cfa_samples(cfa_img,"R",cfa)
    sampleG = cfa_samples(cfa_img,"G",cfa)
    sampleB = cfa_samples(cfa_img,"B",cfa)  

    masqueG = 1/4*np.array([[0,1,0],[1,4,1],[0,1,0]])
    masqueRB = 1/4*np.array([[1,2,1],[2,4,2],[1,2,1]])

    convolutionR = cv2.filter2D(sampleR,-1,masqueRB.astype(np.float32)).astype(np.uint8)
    convolutionG = cv2.filter2D(sampleG,-1,masqueG.astype(np.float32)).astype(np.uint8)
    convolutionB = cv2.filter2D(sampleB,-1,masqueRB.astype(np.float32)).astype(np.uint8)

    """ plt.imshow(convolutionG)
    plt.show() """

    newImg = cv2.merge([convolutionR,convolutionG,convolutionB])

    plt.imshow(newImg)
    plt.show()

def est_G_ha(cfa_img, cfa="GRBG"):
    """ Return the G plane estimated by H&A algorithm from <cfa_img> (numpy array) with given <cfa>
    """
    newImg = np.zeros(cfa_img.shape[:2])
    newImg[0::2,0::2] = cfa_img[0::2,0::2] #G   
    newImg[1::2,1::2] = cfa_img[1::2,1::2] #G

    gradientBlueX = np.gradient(cfa_img[0::2,1::2],axis=1)
    gradientBlueY = np.gradient(cfa_img[0::2,1::2],axis=0)

    gradientRedX = np.gradient(cfa_img[1::2,0::2],axis=1)
    gradientRedY = np.gradient(cfa_img[1::2,0::2],axis=0)

    # j'ai commencé à calculer les gradients locaux à chaque pixel il faut encore appliquer HA dessus et les ajouter à la nouvelle img



if (__name__ == "__main__"):

    demat_bilin(img)


# Ca c'est ce que me donne GPT pour le calcul de gradient en forcant le slicing et aucune boucle for


# indices_blue = np.column_stack(np.where(cfa_img[0::2, 1::2]))

# # Initialiser l'image estimée pour les composantes vertes
# estimated_green = np.zeros_like(cfa_img)

# # Calculer les gradients X et Y pour chaque pixel bleu
# gradientX = gradientBlueX[0::2, 1::2]
# gradientY = gradientBlueY[0::2, 1::2]

# # Calculer les indices adjacents
# left_indices = indices_blue - np.array([0, 1])
# right_indices = indices_blue + np.array([0, 1])
# top_indices = indices_blue - np.array([1, 0])
# bottom_indices = indices_blue + np.array([1, 0])

# # Appliquer la logique décrite pour chaque cas
# estimated_green[indices_blue[:, 0] * 2, indices_blue[:, 1] * 2] = np.where(
#     gradientX > gradientY,
#     (cfa_img[left_indices[:, 0] * 2, left_indices[:, 1] * 2] +
#      cfa_img[right_indices[:, 0] * 2, right_indices[:, 1] * 2]) / 2 +
#     (2 * cfa_img[indices_blue[:, 0] * 2, indices_blue[:, 1] * 2] -
#      cfa_img[indices_blue[:, 0] * 2, (indices_blue[:, 1] - 2) * 2] -
#      cfa_img[indices_blue[:, 0] * 2, (indices_blue[:, 1] + 2) * 2]) / 4,

#     np.where(
#         gradientY > gradientX,
#         (cfa_img[top_indices[:, 0] * 2, top_indices[:, 1] * 2] +
#          cfa_img[bottom_indices[:, 0] * 2, bottom_indices[:, 1] * 2]) / 2 +
#         (2 * cfa_img[indices_blue[:, 0] * 2, indices_blue[:, 1] * 2] -
#          cfa_img[(indices_blue[:, 0] - 2) * 2, indices_blue[:, 1] * 2] -
#          cfa_img[(indices_blue[:, 0] + 2) * 2, indices_blue[:, 1] * 2]) / 4,

#         (cfa_img[(top_indices[:, 0] - 1) * 2, (top_indices[:, 1] - 1) * 2] +
#          cfa_img[(top_indices[:, 0] - 1) * 2, (top_indices[:, 1] + 1) * 2] +
#          cfa_img[(bottom_indices[:, 0] + 1) * 2, (bottom_indices[:, 1] - 1) * 2] +
#          cfa_img[(bottom_indices[:, 0] + 1) * 2, (bottom_indices[:, 1] + 1) * 2]) / 4 +
#         (2 * cfa_img[indices_blue[:, 0] * 2, indices_blue[:, 1] * 2] -
#          cfa_img[(indices_blue[:, 0] - 2) * 2, (indices_blue[:, 1] - 2) * 2] -
#          cfa_img[(indices_blue[:, 0] - 2) * 2, (indices_blue[:, 1] + 2) * 2] -
#          cfa_img[(indices_blue[:, 0] + 2) * 2, (indices_blue[:, 1] - 2) * 2] -
#          cfa_img[(indices_blue[:, 0] + 2) * 2, (indices_blue[:, 1] + 2) * 2]) / 8
#     )
# )

# # Afficher l'image estimée pour les composantes vertes
# print(estimated_green)