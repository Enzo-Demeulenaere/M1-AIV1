import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.stats as sst

name0 = 'stained-wall1'
name1 = 'stained-wall2'
name2 = 'black-stone-tile-wall1'
name3 = 'black-stone-tile-wall2'
name4 = 'metal_with_dust_scratches2'
name5 = 'metal-with-dust-scratches1'

names =[name0,name1,name2,name3,name4,name5] 

for i in range(6):
    name = names[i] 

    image = plt.imread( 'images/' + name + '.jpg' )
    if image.ndim > 2:
        image = image[:,:,0]

    #plt.imshow(image, cmap='gray' )
    print('image i: ',i)
    possibleBins = [10,100,255] 
    for j in range(3):

        nbins = possibleBins[j] 
        counts, bin_edges = np.histogram( np.asarray( image.ravel() ), bins=nbins )
        counts = np.divide(counts,np.amax(counts))
        print("nBins = ",nbins)
        
        mean = np.dot(bin_edges[1:],counts)/np.sum(counts)

        print("moyenne : ",mean)

        variance = np.var(counts)

        print("variance : ",variance)

        kurtosis = sst.kurtosis(counts,axis=None)
        
        print("kurtosis: ",kurtosis)

        entropy = sst.entropy(counts,axis=None)

        print("entropy: ",entropy)
        print("- - - - -")
    print("=============")

# plt.bar(bin_edges[:-1], counts, width = 1)
# plt.xlim(min(bin_edges), max(bin_edges))
#plt.show() 

# counts, bin_edges = np.histogram( np.asarray( c11_n.ravel() ), bins='auto' )

# ny, nx = c11_n.shape
# variance = np.dot(bin_edges[1:],np.power(counts,2)) - np.power(np.dot(bin_edges[1:],counts),2)