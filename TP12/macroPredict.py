from sklearn.cluster import KMeans
import cv2 
import numpy as np 
import sys

dir = 'Fichiers_utiles_TP11/'

fileName = 'cas_2_dalton73.bmp'


image = cv2.imread(dir+fileName, cv2.IMREAD_UNCHANGED) # ouverture du fichier avec cv2  
height, width = image.shape[:2] # taille de l'image

X = image.reshape(width*height,3)

n = 8
# n : nombre de classes
k_means = KMeans(n_clusters=n)
# a : vecteur de dimension nbpixels x 3, ici a correpond à X
k_means.fit(X)
# centroids : vecteur de dimension n x 3 
centroids = k_means.cluster_centers_
centroids = np.uint8(centroids)
# labels: vecteur de dimension nbpixels x 1
labels = k_means.labels_
# a2: vecteur de dimension nbpixels x 3 

originale = centroids[labels]
originale = originale.reshape(image.shape)


def predict(file):
    image2 = cv2.imread(dir+file, cv2.IMREAD_UNCHANGED) # ouverture du fichier avec cv2  
    height2, width2 = image2.shape[:2] # taille de l'image


    Y = image2.reshape(width2*height2,3)
    newLabels = k_means.predict(Y)

    newImage = centroids[newLabels]
    newImage = newImage.reshape(image2.shape)

    cv2.imshow('image originale',originale)
    cv2.imshow('nouvelle image',newImage)
    cv2.waitKey(0)

if __name__ == "__main__":
    args = sys.argv
    fileName = args[1]
    predict(fileName)