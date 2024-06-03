import cv2 
import numpy as np
from sklearn.cluster import KMeans

dir = 'Fichiers_utiles_TP11/'

imgName = 'cas_1_dalton42.bmp'

img = cv2.imread(dir+imgName,cv2.IMREAD_UNCHANGED)

height,width,channels = img.shape
N = width*height

R = img[:,:,0]
R_1D = R.flatten()
G = img[:,:,1]
G_1D = G.flatten() 
B = img[:,:,2]
B_1D = B.flatten(

) 
X = np.zeros((N,3),dtype = int)
X[:,0] = R_1D[:]
X[:,1] = G_1D[:]
X[:,2] = B_1D[:]     

def ACP(matrice):
    meaned = matrice - np.mean(matrice,axis = 0)
    cov_mat = np.cov(meaned, rowvar =False )
    eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)
    sorted_index = np.argsort(eigen_values)[::-1] 
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
    projected = np.dot(sorted_eigenvectors.transpose(),meaned.transpose()).transpose()

    #print(projected) 
    return projected  

#XPCA = X
XPCA = ACP(X)

def normalize(matrice):
    a = np.min(matrice)
    b = np.max(matrice)
    return matrice-a/(b-a)*255


XPCA = normalize(XPCA)
XPCA = XPCA.astype('uint8')


C0 = np.reshape(XPCA[:,0],(height,width))
cv2.imshow('C0',C0)
C1 = np.reshape(XPCA[:,1],(height,width))
cv2.imshow('C1',C1)
C2 = np.reshape(XPCA[:,2],(height,width))
cv2.imshow('C2',C2)



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

    (retVal, ImgSeuil) = cv2.threshold(image,tmax,255,cv2.THRESH_BINARY)
    return ImgSeuil

newR = binarize2classes(C0)
newG = binarize2classes(C1)
newB = binarize2classes(C2)

cv2.imshow('result',cv2.merge([newR,newG,newB]))

cv2.waitKey(0)

