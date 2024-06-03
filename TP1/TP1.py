import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import math

img128a = cv.imread("textures2/128_a.png", cv.IMREAD_GRAYSCALE)
# print("dimension: " ,img128a.ndim)
# print("data type: ",img128a.dtype)
# print("size: ",img128a.size)
# print(img128a.shape)

# img = plt.imshow(img128a,cmap='gray')
# plt.show()

dft = np.fft.fft2(img128a)
# print(dft)
dftInt = dft.astype(int)
dftInt = np.fft.fftshift(dftInt)
dimensions = dftInt.shape
dftInt = dftInt / (dimensions[0] * dimensions[1])
# plt.imshow(dftInt,cmap='gray')
module = np.abs(dftInt)
spectre = 20*np.log(module)
plt.imshow(spectre, cmap='gray')
plt.show()
