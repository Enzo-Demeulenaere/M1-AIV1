1. 
Le code prends une image et la binarise simplement, en plus d'afficher le résultat et l'image inverse également. La fonction binarization indique simplement si un pixel se trouve au delà d'un seuil b0, le paramètre b1 semble en théorie présent uniquement pour permettre de mettre un facteur positif ou négatif et ainsi inverser l'image.
Par défaut, b0 valant -0.5 et b1 valant 1, l'on va distribuer les valeurs sur l'intervalle [-0.5,0.5]  

2.
texture 0: 0.5
1: 0.55
2: ~0.4
3: ~0.4
4: pas de seuil visible sur histogramme

Lorsqu'on essaie de visualiser les textures avec notre seuil empirique, on remarque une distinction des formes de moins en moins précise. Pour la dernière texture, n'ayant pas reussi à définir reellement de seuil à cause de son histogramme, nous avons essayé un seuil variant entre 0.4 et 0.6, valeurs autour de l'unique pic de l'histogramme en 0.5.

Ainsi, nous pouvons dire que determiner un seuil à l'aide de l'histogramme permets une bonne binairisation lorsque l'histogramme présente 2 groupes très distincts de valeurs. En revanche cette méthode est limitée lorsque l'histogramme est un peu plus "homogène" 

3.

Cette fonction 'texture' calcule la variance locale autour d'un point en utilisant un masque moyenneur sur le voisinnage de ce point, ce masque est créé grâce à la fonction 'mask', puis appliqué dans la fonction 'average' pour avoir la moyenne du voisinnage d'un point, moyenne permettant de calculer la variance au sein du code de 'texture'

image texture 0: seuil 0.45
1 : 0.3
2: 0.4
3: 0.27
4: 0.26

Excepté dans l'image 0 où nous obtenons des cercles plutot que des disques, il semblerait que l'image en niveau de texture nous permette d'avoir un histogramme plus exploitable, où l'on arrive plus facilement à determiner un seuil de binarisation. Une fois ce seuil défini, on remarque que la binarisation est en effet plutôt reussie.

Pour ce qui est de l'apparition des cercles, cela pourrait peut-être venir du fait que le bruit sur l'image semble assez faible et que par conséquent seuls les contours de chaque disque sont reconnus par l'algorithme

Lorsqu'on compare les image en texture binaire et l'image de referrence :

taux de similitude :
image 0 : 56% (taux bas en raison des cercles)
1: 90%
2: 93% (meilleur taux que 1 malgré l'aspect un peu incorrect)
3: 95%
4: 95%

On peut semblerait-il affirmer que le niveau de texture soit un attribut très interessant pour la binarisation, en revanche cela ne peut constituer le seul attribut car selon certains cas, il se peut qu'il ne soit pas entierement fiable. Nous pensons que certains facteurs peuvent causer une fiabilité partielle de cette technique, notamment l'intensité du bruit d'une image qui peut impacter le calcul de la variance locale, la dimension choisie pour le voisinnage peut également être un facteur dans le résultat de la variance locale.

En comparant les histogrammes avec et sans échelle logarithmique nous remarquons qu'ils sont similaires et possèdent la même "forme"
à la différence de l'echelle, on pourrait donc supposement recuperer le seuil de binarisation depuis la représentation avec echelle logarithmique, à condition biensur de calculer le seuil en utilisant la fonction exponentielle.
On remarque tout de même que les différentes valeurs des pixels semblent avoir été affectées par la fonction log mais que les valeurs d'occurence semblent également être affectées, legerement certes, d'où notre commentaire sur la forme similaire des histogrammes mais nous ne savons pas expliquer ce phénomène

Nous n'avons malheureusement pas compris quel était le but de la fonction binarize2d ainsi que comment l'implementer, il semblerait qu'il nous faille determiner un seuil à l'aide d'une droite, droite que nous supposons être verticale et d'équation x= k avec k un seuil, nous ne comprenons pas alors quels sont les 3 paramètres de cette droite que nous devons utiliser. Pour la suite du tp, nous determinons donc un seuil de manière empirique en observant l'histogramme conjoint de chaque image, de la même manière que pour les 2 attributs précédents

similitude composée:
0 : 81% (seuil 0.4)
1 : 93% (seuil 0.6)
2 : 96% (seuil 0.39)
3 : 96% (seuil 0.35)
4 : 94% (seuil 0.39)

Nous pouvons observer de très bons résultats de binarization, la majorité des résultats étant équivalents aux résultats obtenus avec les  images en texture, nous remarquons une amélioration dans le résultat de la première image en comparaison avec la dernière technique utilisée. Nous pouvons donc assumer que l'utilisation d'un classifieur 2D semble être de grand interet pour ce type d'images car il semble mettre en avant un résultat interessant de reconnaissance lorsque l'un des attribut semble s'averer très efficace. Notons tout de même que ce type de classifieur n'est potentiellement pas interessant pour d'autres types d'images qui n'ont pas été étudiés dans ce tp

