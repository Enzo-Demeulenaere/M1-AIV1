import cv2 
import numpy as np
from sklearn.metrics import confusion_matrix

dir = 'Fichiers_utiles_TP10_2023/'

img3classes = cv2.imread(dir+'2classes_100_100_8bits.png',cv2.IMREAD_UNCHANGED)
hist = cv2.calcHist([img3classes],[0],None,[256],[0,256]) 

# # sauf que nous avons 3 régions 
# maxVariance = -np.inf
# # puisque la taille de l'image en hauteur est de 156 nous avons : 

# height = 100
# width = 100

# N = height*width

# # 2 classes

# for t in range(256): 
#     nOmega1 =0
#     nOmega2 =0
#     u1 = 0
#     u2 = 0
#     mu1 = 0
#     mu2 = 0

#     # Premiere serie de boucles pour les P et N  
#     for i in range(t+1):
#         nOmega1 += hist[i] 
#         u1 += i * hist[i] 
#     pOmega1 = nOmega1/N
#     if nOmega1 != 0 :
#         mu1 = u1/ nOmega1

#     for j in range(t+1,256):
#         nOmega2 += hist[j]
#         u2 += j * hist[j] 
#     pOmega2 = nOmega2/N  
#     if nOmega2 != 0: 
#         mu2 = u2/ nOmega2

#     # # Seconde serie de boucles pour la variance 
    
#     # sum1 = 0
#     # sum2 = 0
    
#     # for i in range(t+1):
#     #     sum1 += np.power(i-mu1,2)*hist[i] 
#     # for j in range(t+1,256):
#     #     sum2 += np.power(j-mu2,2)*hist[j]  
#     # # On peut maintenant calculer la variance
#     # facteur1 = 0
#     # if nOmega1 != 0:
#     #     facteur1 = pOmega1*sum1/nOmega1
#     # facteur2 = 0
#     # if nOmega2 != 0:
#     #     facteur2 = pOmega2*sum2/nOmega2

#     variance = pOmega1*pOmega2*np.power(mu1-mu2,2)

#     if(variance > maxVariance):
#         tmax = t
#         maxVariance = variance

# print(tmax)

# (retVal1, ImgSeuil) = cv2.threshold(img3classes,tmax,127,cv2.THRESH_BINARY)

# GTimg = cv2.imread(dir+'2classes_100_100_8bits_GT.png',cv2.IMREAD_UNCHANGED)
# GTimg1D = np.zeros((height*width,1),dtype=int)
# ImgSeuil1D = np.zeros((height*width,1),dtype=int)

# for i in range(height):
#     for j in range(width):
#         GTimg1D[i*width + j]= GTimg[i,j]
#         ImgSeuil1D[i*width + j]= ImgSeuil[i,j]

# cm = confusion_matrix(GTimg1D,ImgSeuil1D)
# print(cm)

# 3 classes

# for t2 in range(256): 
#     for t1 in range(t2+1):
#         nOmega1 =0
#         nOmega2 =0
#         nOmega3 =0
#         u1 = 0
#         u2 = 0
#         u3 = 0
#         mu1 = 0
#         mu2 = 0
#         mu3 = 0

#         # Premiere serie de boucles pour les P et N  
#         for i in range(t1+1):
#             nOmega1 += hist[i] 
#             u1 += i * hist[i] 
#         pOmega1 = nOmega1/N
#         if nOmega1 != 0 :
#             mu1 = u1/ nOmega1

#         for j in range(t1+1,t2):
#             nOmega2 += hist[j]
#             u2 += j * hist[j] 
#         pOmega2 = nOmega2/N  
#         if nOmega2 != 0: 
#             mu2 = u2/ nOmega2

#         for k in range(t2+1,256):
#             nOmega3 += hist[k]
#             u3 += k * hist[k] 
#         pOmega3 = nOmega3/N 
#         if nOmega3 != 0:
#             mu3 = u3 / nOmega3
#         # Seconde serie de boucles pour la variance 
        
#         sum1 = 0
#         sum2 = 0
#         sum3 = 0
        
#         for i in range(t1+1):
#             sum1 += np.power(i-mu1,2)*hist[i] 
#         for j in range(t1+1,t2):
#             sum2 += np.power(j-mu2,2)*hist[j]  
#         for k in range(t2+1,256):
#             sum3 += np.power(k-mu3,2)*hist[k]  
#         # On peut maintenant calculer la variance
#         facteur1 = 0
#         if nOmega1 != 0:
#             facteur1 = pOmega1*sum1/nOmega1
#         facteur2 = 0
#         if nOmega2 != 0:
#             facteur2 = pOmega2*sum2/nOmega2
#         facteur3 = 0
#         if nOmega3 != 0:
#             facteur3 = pOmega3*sum3/nOmega3
        
#         variance = facteur1 + facteur2 + facteur3

#         if(variance < minVariance):
#             t1min = t1
#             t2min = t2
#             minVariance = variance

# print(t1min,t2min)
 
# Résultats obtenus : 85, 157 

# (retVal1, ImgSeuil1) = cv2.threshold(img3classes,t1min,127,cv2.THRESH_BINARY)
# (retVal2, ImgSeuil2) = cv2.threshold(img3classes,t2min,255,cv2.THRESH_BINARY)
# [dest]  = np.maximum([ImgSeuil1],[ImgSeuil2])



# GTimg = cv2.imread(dir+'3classes_100_156_8bits_GT.png',cv2.IMREAD_UNCHANGED)
# GTimg1D = np.zeros((height*width,1),dtype=int)
# ImgSeuil1D = np.zeros((height*width,1),dtype=int)

# for i in range(height):
#     for j in range(width):
#         GTimg1D[i*width + j]= GTimg[i,j]
#         ImgSeuil1D[i*width + j]= dest[i,j]

# cm = confusion_matrix(GTimg1D,ImgSeuil1D)
# print(cm)

# matrice obtenue: 
# [[5157  443    0]
#  [ 300 4006   94]
#  [   0  182 5418]] 

# 93,46% de pixels bien placés en non supervisé (ici)

# 93,48% de pixels bien placés en supervisé 

def binarize2classes(image):
    hist = cv2.calcHist([image],[0],None,[256],[0,256]) 

    maxVariance = -np.inf

    height,width =  image.shape

    N = height*width

    for t in range(256): 
        nOmega1 =0
        nOmega2 =0
        u1 = 0
        u2 = 0
        mu1 = 0
        mu2 = 0

        # calcul des pOmega, et mu
        for i in range(t+1):
            nOmega1 += hist[i] 
            u1 += i * hist[i] 
        pOmega1 = nOmega1/N
        if nOmega1 != 0 :
            mu1 = u1/ nOmega1

        for j in range(t+1,256):
            nOmega2 += hist[j]
            u2 += j * hist[j] 
        pOmega2 = nOmega2/N  
        if nOmega2 != 0: 
            mu2 = u2/ nOmega2

        variance = pOmega1*pOmega2*np.power(mu1-mu2,2)

        if(variance > maxVariance):
            tmax = t
            maxVariance = variance

    #print(tmax)

    (retVal, ImgSeuil) = cv2.threshold(image,tmax,255,cv2.THRESH_BINARY)

    # GTimg = cv2.imread(imageName+'_GT.png',cv2.IMREAD_UNCHANGED)
    # GTimg1D = np.zeros((height*width,1),dtype=int)
    # ImgSeuil1D = np.zeros((height*width,1),dtype=int)

    # for i in range(height):
    #     for j in range(width):
    #         GTimg1D[i*width + j]= GTimg[i,j]
    #         ImgSeuil1D[i*width + j]= ImgSeuil[i,j]

    # cm = confusion_matrix(GTimg1D,ImgSeuil1D)
    # print(cm)
    return ImgSeuil

def binarize2classesFromName(imageName):
    image = cv2.imread(imageName,cv2.IMREAD_UNCHANGED)
    return binarize2classes(image)


# Question 3


def splitAndMerge(imageName):
    img = cv2.imread(imageName,cv2.IMREAD_UNCHANGED)
    b,g,r = cv2.split(img)
    imgB = binarize2classes(b)
    #cv2.imshow('imgB',imgB)
    imgG = binarize2classes(g)
    #cv2.imshow('imgG',imgG)
    imgR = binarize2classes(r)
    #cv2.imshow('imgR',imgR)
    mergedImg = cv2.merge([imgB,imgG,imgR])
    return mergedImg

imgName0 = dir+'IMAGE3D_V0.bmp'
imgName9 = dir+'IMAGE3D_V9.bmp'
imgName16 = dir+'IMAGE3D_V16.bmp'
imgName25 = dir+'IMAGE3D_V25.bmp'

cv2.imshow('merged Image V0',splitAndMerge(imgName0))
cv2.imshow('merged Image V9',splitAndMerge(imgName9))
cv2.imshow('merged Image V16',splitAndMerge(imgName16))
cv2.imshow('merged Image V25',splitAndMerge(imgName25))

cv2.waitKey(0)


