# -----------------------------------------------------------------------
# Extraction d'attributs de contours,
# Master informatique, module AIV1
# Copyleft (C) 2021-2022, Universite de Lille
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
import csv

def contour( image ):
    c, h = cv.findContours( image, cv.RETR_EXTERNAL,
                            cv.CHAIN_APPROX_NONE )
    c = np.array( c[0] ).astype( float )
    return (c[...,0] + 1j * c[...,1]).transpose()[0]

name1 = 'aiv1-patate'
image1 = cv.imread( 'images/' + name1 + '.png', cv.IMREAD_GRAYSCALE )
contour1 = contour( image1 )

# name2 = 'aiv1-carre-80'
# pixels = np.genfromtxt( 'contours/' + name2 + '.csv', delimiter=';',
#                         names=True )
# contour2 = pixels['x'] + 1j * pixels['y']

""" plt.gca().invert_yaxis()
plt.axis( 'equal' )
plt.plot( contour1.real, contour1.imag, color=(1.0, 0.0, 0.0),
          linestyle='-', marker='o' )
plt.plot( contour2.real, contour2.imag, color=(0.0, 0.0, 1.0),
          linestyle='-', marker='x' )
plt.savefig( 'deux-contours.svg' )
plt.show() """

#CODE DECALAGE BARYCENTRE

# desc_fourier = np.fft.fft(contour2)

# desc_fourier_norm = desc_fourier / len(contour2)
# desc_fourier_norm[0] += 10j 
# desc_fourier_inv = np.fft.ifft(desc_fourier_norm * len(contour2))
# newContour2 = desc_fourier_inv

# plt.gca().invert_yaxis()
# plt.axis( 'equal' )
# plt.plot( contour1.real, contour1.imag, color=(1.0, 0.0, 0.0),
#           linestyle='-', marker='o' )
# plt.plot( newContour2.real, newContour2.imag, color=(0.0, 0.0, 1.0),
#           linestyle='-', marker='x' )
# plt.savefig( 'deux-contours.svg' )
# plt.show()

def keepRatioImage(desc,ratio):
    newDesc = desc
    newDesc[:int(desc.size*(1-ratio))]=0
    return newDesc

def keepRatioCSV(desc,ratio):
    newDesc = desc
    newDesc[int(desc.size*ratio):]=0
    return newDesc

desc_fourier_norm = np.fft.fft(contour1) / contour1.size


desc_fourier_norm = keepRatioImage(desc_fourier_norm,0.5)


contour1 = np.fft.ifft(desc_fourier_norm * contour1.size)

plt.gca().invert_yaxis()
plt.axis( 'equal' )
plt.plot( contour1.real, contour1.imag, color=(1.0, 0.0, 0.0),
          linestyle='-', marker='o' )
# plt.plot( contour2.real, contour2.imag, color=(0.0, 0.0, 1.0),
#           linestyle='-', marker='x' )
#plt.savefig( 'deux-contours.svg' )
plt.show()

