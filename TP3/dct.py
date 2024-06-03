import numpy as np 
import matplotlib.pyplot as plt 
import scipy.fftpack as scp 
import cv2
import math

img = cv2.imread("example.png")
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
img128 = 128*np.ones(img.shape)
img = img-img128

BLOCK_SIZE = 8

QY = np.array([
    [16, 11, 10, 16,  24,  40,  51,  61],
    [12, 12, 14, 19,  26,  58,  60,  55],
    [14, 13, 16, 24,  40,  57,  69,  56],
    [14, 17, 22, 29,  51,  87,  80,  62],
    [18, 22, 37, 56,  68, 109, 103,  77],
    [24, 35, 55, 64,  81, 104, 113,  92],
    [49, 64, 78, 87, 103, 121, 120, 101],
    [72, 92, 95, 98, 112, 100, 103,  99]
]).astype(float)

def dct2d(image):
    dct1D = scp.dct(image,type = 2,axis = 1,norm = "ortho")
    dct2D = scp.dct(dct1D,type = 2,axis = 0, norm = "ortho")
    
    return dct2D

def jpeg(image_name, show=False, quality=50):
    img = cv2.imread(image_name,cv2.IMREAD_GRAYSCALE)
    tempImg = 128*np.ones(img.shape)
    img = img-tempImg
    newImg = np.zeros(img.shape).astype(float)
    if quality >0 and quality<51 :
        Q = QY*50/quality
    elif quality<100:
        Q = QY*(2-(2*quality/100))
    allCoefsBeforeEOB =[] 
    for i in range(0,img.shape[0],BLOCK_SIZE):
        for j in range(0,img.shape[1],BLOCK_SIZE):
            block = img[i:i+BLOCK_SIZE,j:j+BLOCK_SIZE]
            block = dct2d(block)
            block = np.round(block/Q)
            # adding zigzag
            coefs = coeffsBeforeEOB(zigzag(block))
            for k in coefs:
                k += 128
                allCoefsBeforeEOB.append(k)
            
            # now decompressing
            block = block*Q
            block = idct2d(block)
            newImg[i:i+BLOCK_SIZE,j:j+BLOCK_SIZE]= block
    print(len(allCoefsBeforeEOB))
    tmpCoeffsImage = np.zeros(img.shape).astype(float)
    tmpCoeffsImage = np.array(allCoefsBeforeEOB)
    cv2.imwrite("lena_zigzag_5.png", tmpCoeffsImage) 
    newImg = newImg + tempImg
    img = img +tempImg
    error_measures(img,newImg)
    if (show):
        plt.imshow(newImg,cmap='gray')
        plt.show()


def idct2d(coeffs):
    idct1D = scp.idct(coeffs,type = 2, axis = 1, norm = "ortho")
    idct2D = scp.idct(idct1D,type = 2, axis = 0, norm = "ortho")
    return idct2D

def error_measures(I,Iest):
    mn = I.shape[0]*I.shape[1]

    sumAbs = np.sum(np.abs(np.subtract(I,Iest)))
    sumSquare = np.sum(np.square(np.subtract(I,Iest)))

    mae = np.divide(sumAbs,mn)
    mse = np.divide(sumSquare,mn)
    psnr = 10*np.log10((255**2)/mse)

    print("MAE :", mae)
    print("MSE :", mse)
    print("PSNR :", psnr)


def zigzag(coefficients):
    """ Return the list of <coefficients> in zigzag read order
        Adapted from: http://rosettacode.org/wiki/Zig-zag_matrix#Python:_By_sorting_indices
    """
    def compare(xy):
        x, y = xy
        return x + y, -y if (x + y) % 2 else y
    nrows, ncols = coefficients.shape
    assert nrows == ncols
    ind = range(nrows)  # indices along x and y
    ordered_indices = sorted(((x, y) for x in ind for y in ind), key=compare)
    return [coefficients[index] for index in ordered_indices]

def coeffsBeforeEOB(coefficients):
    res =[]
    for coeff in coefficients :
        if coeff != 0:
            res.append(coeff)
        else: break
    return res

if (__name__== "__main__"):
    jpeg("lena.png",True,5)
    #plt.imshow(dct2d,cmap = 'gray')
    #plt.show()
