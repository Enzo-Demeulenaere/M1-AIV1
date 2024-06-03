
# -----------------------------------------------------------------------
# Extraction d'attributs de texture,
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
import scipy.signal as sig

def binarization( im1, b0, b1 ):
    return ( b0 + b1 * im1 >= 0 )

# seuil | binaire (% segmentation)| binaire inversée
# name = 'aiv1-2-classes-texture-0' # seuil à 0.5 # 0.087% # 99.9% 
# name1 = 'aiv1-2-classes-texture-1' # seuil à 0.55 # 0.879% # 99.1%
# name2 = 'aiv1-2-classes-texture-2' # seuil à 0.4 # 63% # 38%
# name3 = 'aiv1-2-classes-texture-3' # seuil à 0.4 # 62% # 39%
# name4 = 'aiv1-2-classes-texture-4' # seuil indeterminée 

filePrefix = 'aiv1-2-classes-texture-'
fileNumber = 4

fileName = filePrefix+str(fileNumber)

image = plt.imread( 'images/' + fileName + '.png' )

image_ref = plt.imread('images/aiv1-masque-ronds.png')

#print(np.sum(image_ref == binarization(image,0.5,-1))/ image_ref.size * 100)


def mask( width ):
    width = 2 * width + 1
    return np.ones(( width, width )) / width / width

def average( im, width ):
    return sig.convolve2d( im, mask( width ), mode='same' )

def texture( im, width ):
    diff2 = np.power( im - average( im, width ), 2 )
    std = np.sqrt( average( diff2, width ) )
    return std / std.max()


if image.ndim > 2:
    image = image[:,:,0]
    
if image_ref.ndim > 2:
    image_ref = image_ref[:,:,0]

fig, axes = plt.subplots( 1, 4, figsize=(12, 4) )
ax = axes.ravel()

texturedImage = texture(image,2)

ax[0].set_title('Image originelle')
ax[0].imshow( image, cmap='gray' )
ax[0].set_axis_off()

# ax[1].set_title('Image en niveau de texture')
# # print(binarization( image, -0.5, 1 ))
# ax[1].imshow( texturedImage, cmap='gray' )
# ax[1].set_axis_off()

#binarized = binarization( texturedImage, -0.45, 1 )
composed = (texturedImage + image) / 2

binarized = 1- binarization(composed,-0.39,1)

ax[1].set_title('Image composée \n(texture + originelle)')
ax[1].imshow( composed, cmap='gray' )
ax[1].set_axis_off()

ax[2].set_title('Image composée binarisée')
# print(binarization( image, -0.5, 1 ))
ax[2].imshow( binarized, cmap='gray' )
ax[2].set_axis_off()

ax[3].set_title('Image de réference')
ax[3].imshow( image_ref, cmap='gray' )
ax[3].set_axis_off()

# fig1 = plt.figure()
# ax1 = fig1.add_subplot(1,1,1)
# ax1.hist(composed)

# ax[3] = ax1

#plt.hist(composed,bins="auto") # Nous avons utilisés plt.hist à la place de numpy_histogram 

#plt.hist(np.log10(1+composed),bins="auto")
print(np.sum(image_ref == binarized)/ image_ref.size * 100)


plt.tight_layout()
plt.show()