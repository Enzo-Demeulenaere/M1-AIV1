import cv2
import numpy as np
from sklearn.metrics import confusion_matrix

dir = './Fichiers_utiles_TP9_2023/'

# nom = dir + '2classes_100_100_8bits.png'
# nomFenetre = 'original'
# image = cv2.imread(nom, cv2.IMREAD_UNCHANGED)

# nomGT =  dir + '2classes_100_100_8bits_GT.png'
# GTimg = cv2.imread(nomGT, cv2.IMREAD_UNCHANGED)
# height = 100
# width = 100
# GTimg1D = np.zeros((height*width,1),dtype=int)
# ImgSeuil1D = np.zeros((height*width,1),dtype=int)

#Affichage
# cv2.imshow(nomFenetre,image)

#calcul de l'histogramme
# hist = cv2.calcHist([image],[0],None,[256],[0,256])
#seuillage
# seuil = 145
# (retVal, ImgSeuil)= cv2.threshold(image,seuil,255,cv2.THRESH_BINARY)

# QUESTION 2

# for i in range(height):
#     for j in range(width):
#         GTimg1D[i*width + j]= GTimg[i,j]
#         ImgSeuil1D[i*width + j]= ImgSeuil[i,j]    

# cm = confusion_matrix(GTimg1D,ImgSeuil1D)
#print(cm)

# hist = cv2.calcHist([image],[0],None,[256],[0,256])
# omega1 = cv2.imread(dir+'2classes_100_100_8bits_omega1.png',cv2.IMREAD_UNCHANGED)
# hist1 = cv2.calcHist([omega1],[0],None,[256],[0,256])
# omega2 = cv2.imread(dir+'2classes_100_100_8bits_omega2.png',cv2.IMREAD_UNCHANGED)
# hist2 = cv2.calcHist([omega2],[0],None,[256],[0,256])


# epsilon = np.inf
# tmin = 0
# pOmega1 = 56/100
# pOmega2 = 44/100
# for t in range(256):
#     sum1 = 0
#     sum2 = 0
#     for i in range(t+1):
#         if(hist[i] != 0 ):
#             sum1 += hist2[i]/hist[i] *pOmega2  
#     for j in range(t+1,256):
#         if(hist[j] != 0 ):
#             sum2 += hist1[j]/hist[j] *pOmega1  
#     if (sum1 + sum2 < epsilon):
#         tmin = t
#         epsilon = sum1 + sum2

# print(epsilon,tmin)


# QUESTION 3



# img3classes = cv2.imread(dir+'3classes_100_156_8bits.png',cv2.IMREAD_UNCHANGED)
# hist = cv2.calcHist([img3classes],[0],None,[256],[0,256])
# omega1 = img3classes[:56]
# hist1 = cv2.calcHist([omega1],[0],None,[256],[0,256])
# omega2 = img3classes[56:100]
# hist2 = cv2.calcHist([omega2],[0],None,[256],[0,256])
# omega3 = img3classes[100:] 
# hist3 = cv2.calcHist([omega3],[0],None,[256],[0,256])  



# epsilon = 0
# t1min = 0
# t2min = 0
# pOmega1 = 56/156
# pOmega2 = 44/156
# pOmega3 = 56/156
# for t2 in range(256): 
#     for t1 in range(t2+1):
#         sum1 = 0
#         sum2 = 0
#         sum3 = 0
#         for i in range(t1+1):
#             if(hist[i] != 0 ):
#                 sum1 += hist1[i]/hist[i] *pOmega1  
#         for j in range(t1+1,t2):
#             if(hist[j] != 0 ):
#                 sum2 += hist2[j]/hist[j] *pOmega2     
#         for k in range(t2+1,256):
#             if(hist[k] !=0 ):
#                 sum3 += hist3[k]/hist[k] *pOmega3
#         if (sum1 + sum2 + sum3 > epsilon):
#             t1min = t1
#             t2min = t2
#             epsilon = sum1 + sum2 + sum3

# print(epsilon,t1min,t2min)

# (retVal1, ImgSeuil1) = cv2.threshold(img3classes,t1min,127,cv2.THRESH_BINARY)
# (retVal2, ImgSeuil2) = cv2.threshold(img3classes,t2min,255,cv2.THRESH_BINARY)
# [dest]  = np.maximum([ImgSeuil1],[ImgSeuil2]) 

# height = 156
# width = 100

# GTimg = cv2.imread(dir+'3classes_100_156_8bits_GT.png',cv2.IMREAD_UNCHANGED)
# GTimg1D = np.zeros((height*width,1),dtype=int)
# ImgSeuil1D = np.zeros((height*width,1),dtype=int)

# for i in range(height):
#     for j in range(width):
#         GTimg1D[i*width + j]= GTimg[i,j]
#         ImgSeuil1D[i*width + j]= dest[i,j]

# cm = confusion_matrix(GTimg1D,ImgSeuil1D)
# print(cm)
# cv2.imshow('seuil',dest)

# cv2.imshow('Image_seuil',ImgSeuil)

# QUESTION 4

image = cv2.imread(dir+'rdf-chiffre-0-8bits.png')

hist = cv2.calcHist([image],[0],None,[256],[0,256])
omega1 = cv2.imread(dir+'rdf-chiffre-0-8bits_omega1.png',cv2.IMREAD_UNCHANGED)
hist1 = cv2.calcHist([omega1],[0],None,[256],[0,256])
omega2 = cv2.imread(dir+'rdf-chiffre-0-8bits_omega2.png',cv2.IMREAD_UNCHANGED)
hist2 = cv2.calcHist([omega2],[0],None,[256],[0,256])

# for i in range(height):
#     for j in range(width):
#         GTimg1D[i*width + j]= GTimg[i,j]
#         ImgSeuil1D[i*width + j]= ImgSeuil[i,j]    

# cm = confusion_matrix(GTimg1D,ImgSeuil1D)
#print(cm)

height = 24
width = 20

epsilon = np.inf
tmin = 0
pOmega1 = np.count_nonzero(omega1 != 255)/ (height*width) 
pOmega2 = np.count_nonzero(omega2 != 255)/ (height*width) 
for t in range(256):
    sum1 = 0
    sum2 = 0
    for i in range(t+1):
        if(hist[i] != 0 ):
            sum1 += hist2[i]/hist[i] *pOmega2  
    for j in range(t+1,256):
        if(hist[j] != 0 ):
            sum2 += hist1[j]/hist[j] *pOmega1  
    if (sum1 + sum2 < epsilon):
        tmin = t
        epsilon = sum1 + sum2

# pour chiffre 0
#(retVal, ImgSeuil) = cv2.threshold(image,tmin,255,cv2.THRESH_BINARY)

image1 = cv2.imread(dir+'rdf-chiffre-1-8bits.png')
(retVal, ImgSeuil) = cv2.threshold(image1,tmin,255,cv2.THRESH_BINARY)

cv2.imshow('seuil',ImgSeuil)

cv2.waitKey(0)
cv2.destroyAllWindows()