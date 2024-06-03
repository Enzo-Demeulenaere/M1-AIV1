1. 

Pour avoir l'histogramme correct, il faut donner la valeur 255 à nbins

résultats: 

image i:  0
nBins =  10
kurtosis:  -1.5452954474050586
entropy:  1.9206050286755547
- - - - -
nBins =  100
kurtosis:  -1.1628715754682706
entropy:  4.157628728009508
- - - - -
nBins =  255
kurtosis:  -1.4675330471277057
entropy:  5.112119551287489
- - - - -
=============
image i:  1
nBins =  10
kurtosis:  -0.788338946968179
entropy:  2.0974111703467946
- - - - -
nBins =  100
kurtosis:  3.544755943070159
entropy:  4.280727052355772
- - - - -
nBins =  255
kurtosis:  1.9338504650704689
entropy:  5.1677936851928905
- - - - -
=============
image i:  2
nBins =  10
kurtosis:  -0.7488494200586575
entropy:  2.209261925999927
- - - - -
nBins =  100
kurtosis:  -0.2975595395917514
entropy:  4.467912723280916
- - - - -
nBins =  255
kurtosis:  -0.9924752126529981
entropy:  5.422590694090031
- - - - -
=============
image i:  3
nBins =  10
kurtosis:  -0.41049643518071877
entropy:  2.1515421489696522
- - - - -
nBins =  100
kurtosis:  0.9942196799215175
entropy:  4.41046248384594
- - - - -
nBins =  255
kurtosis:  0.46323841986858527
entropy:  5.364206839446041
- - - - -
=============
image i:  4
nBins =  10
kurtosis:  0.166936961788811
entropy:  1.9930370509452469
- - - - -
nBins =  100
kurtosis:  1.792169881273808
entropy:  4.267452759646375
- - - - -
nBins =  255
kurtosis:  0.7975328463083531
entropy:  5.219562594378294
- - - - -
=============
image i:  5
nBins =  10
kurtosis:  4.6071033109002135
entropy:  1.5404056419835388
- - - - -
nBins =  100
kurtosis:  27.921793322118866
entropy:  3.6637814206869033
- - - - -
nBins =  255
kurtosis:  24.444155111156824
entropy:  4.605320227474955
- - - - -
=============

Kurtosis correspond plus ou moins à "l'applatissement" de l'histogramme, on remarque que lorsque le nombre de bins varie entre 10,100 et 255, le kurtosis est le plus grand pour nBins = 100, et ce pour chacune des textures.

L'entropie correspond à la quantité d'informations récupérées, on s'attend à ce que cet attribut augmente lorsque le nombre de bins augmente, car étant donné un plus grand nombre de bins, chaque pixel peut être codé sur une plus grande plage de valeurs. Cela s'avère se verifier pour chacune des texture où cet attribut augmente en même temps que le nombre de bins