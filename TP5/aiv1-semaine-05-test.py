# -----------------------------------------------------------------------
# Extraction d'attributs de forme,
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
import csv

def moment( im, p, q ):
    ny, nx = image.shape
    x = np.arange( nx )
    y = np.arange( ny )
    xp = np.power( x, p )
    yq = np.power( y, q )
    return np.dot( yq, np.dot( im, xp ) )

name = 'aiv1-triangle-10-60deg'

image = plt.imread( 'images/' + name + '.png' )
if image.ndim > 2:
    image = image[:,:,0]

m00 = moment( image, 0, 0 )
m10 = moment( image, 1, 0 )
m01 = moment( image, 0, 1 )


def moment_centre(image,p,q):

    barX = m10/m00
    barY = m01/m00

    ny, nx = image.shape
    x = np.arange( nx )
    y = np.arange( ny )
    xp = np.power( x-barX, p )
    yq = np.power( y-barY, q )
    return np.dot( yq, np.dot( image, xp ) )

def moment_centre_normalise(image,p,q):
    upq = moment_centre(image,p,q)
    u00 = moment_centre(image,0,0)
    u00p = np.power(u00,1+((p+q)/2))

    return upq/u00p


def matrice(image):

    u20 = moment_centre(image,2,0)
    u02 = moment_centre(image,0,2)
    u11 = moment_centre(image,1,1)

    array = np.array([[u20,u11],[u11,u02]])
    return np.asmatrix(array)

valeursPropres, vecteursPropres = np.linalg.eig(matrice(image))
orientations = np.arctan2(vecteursPropres[0::2],vecteursPropres[1::2])

matriceI = matrice(image)
matriceP = np.asmatrix(vecteursPropres)
matriceP1 = np.linalg.inv(matriceP)

n20 = moment_centre_normalise(image,2,0)
n02 = moment_centre_normalise(image,0,2)

newMatrice = np.dot(np.dot(matriceP1,matriceI),matriceP)

print("Vecteurs propres: ",vecteursPropres)
print("valeurs propres: ",valeursPropres)
print("orientations: ",orientations)
print("normalisés: ",n20,n02)
print("===========")
newValeursPropres, newVecteursPropres = np.linalg.eig(newMatrice)
print("nouveaux vecteurs propres: ",newVecteursPropres)
print("nouvelles valeurs propres: ",newValeursPropres)

imgplot = plt.imshow( image, cmap='gray' )
plt.show()

with open( name + '.csv', 'w', newline='' ) as csvfile:
    csvwriter = csv.writer( csvfile, delimiter=';' )
    csvwriter.writerow( ['surface', 'x', 'y'] )
    csvwriter.writerow( [m00, m10 / m00, m01 / m00] )

