from sklearn.cluster import KMeans
import cv2 
import numpy as np 
import sys

dir = 'Fichiers_utiles_TP11/'

fileName = 'cas_2_dalton73.bmp'


image = cv2.imread(dir+fileName, cv2.IMREAD_UNCHANGED) # ouverture du fichier avec cv2  
height, width = image.shape[:2] # taille de l'image

X = image.reshape(width*height,3)

def ACP(matrice):
    meaned = matrice - np.mean(matrice,axis = 0)
    cov_mat = np.cov(meaned, rowvar =False )
    eigen_values, eigen_vectors = np.linalg.eigh(cov_mat)
    sorted_index = np.argsort(eigen_values)[::-1] 
    sorted_eigenvectors = eigen_vectors[:,sorted_index]
    projected = np.dot(sorted_eigenvectors.transpose(),meaned.transpose()).transpose()

    return projected 

XPCA = ACP(X)

n = 8
# n : nombre de classes
k_means = KMeans(n_clusters=n)
# a : vecteur de dimension nbpixels x 3, ici a correpond à X
k_means.fit(XPCA)
# centroids : vecteur de dimension n x 3 
centroids = k_means.cluster_centers_
centroids = np.uint8(centroids)
# labels: vecteur de dimension nbpixels x 1
labels = k_means.labels_
# a2: vecteur de dimension nbpixels x 3 

originale = centroids[labels]
originale = originale.reshape(image.shape)

cv2.imshow('image originale',image)
cv2.imshow('image ACP segmentee',originale)
cv2.waitKey(0)
