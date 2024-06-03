Pour le 8, cela se remarque surtout sur la composante 2 

Pour le 42, c'est la composante 1
Pour le 16 c'est sur la composante 2

Pour une image décomposée avec PCA, nous obtenons un total de 3 composantes C0, C1, C2. Chacune représente une donnée statistique de variation de répartition des couleurs selon leurs valeurs RGB dans un plan en 3 dimensions. C0 représente la répartition des pixels si on les rapporte sur l'axe représentant la première plus grande variation, C1 pour la seconde plus grande variation et C2 la troisieme plus grande variation.

De manière générale la composante C0 représente la luminance car la plus grande variation se trouve généralement entre un pixel considéré lumineux et un pixel considéré sombre. Les 2 autres composantes décrivent alors les variations entre les autres couleurs et représentent donc la chrominance d'une image.

Nous apportons par la suite des captures d'écran de la modélisation 3D de la répartition des pixels de chaque image, nous sommes conscients qu'une fois rapportés en 2 dimensions ces modélisations peuvent être confuses et essaieront de réduire au maximum ces confusions de part nos explications. 

Pour la suite de nos observations nous ne prendront pas en compte les pixels blancs aux coins de chaque image lorsque nous évoqueront des clusters de pixels.
Nous tentons de représenter les axes C0 en noir, C1 en blanc et C2 en bleu. de plus, la première modélisation représentera aussi fidèlement que possible les axes C0 et C1 tandis que la seconde permettra une meilleure perception de l'axe C2.

Commençons par le chiffre 8, nous pouvons observons 2 groupes de couleurs, du vert et du rouge orangé, afin d'extraire le chiffre clairement, il va falloir trouver laquelle des 2 composantes C1 ou C2 permets de séparer les 2 clusters de couleurs

[inserer l'image cas4 dalton8 originale]
[inserer les images cas4 dalton8: C0_C1 d'abord C2 ensuite]

Dans ces images nous avons délimité les clusters vert et orange.
La première image montre surtout que les axes C0 et C1 ne permettent pas de séparer les clusters alors que sur la seconde, l'axe C2 donne un résultat plus satisfaisant, ainsi c'est à travers la composante C2 que nous arriverons le mieux à extraire le chiffre

[inserer les images de C0 C1 et C2 pour le cas4 dalton8]

En ce qui concerne le nombre 16, nous retrouvons un cas de figure similaire excepté l'échange des couleurs entre le fond et le nombre, nous pouvons donc faire les mêmes remarques que pour le chiffre 8 et affirmer que la composante C2 sera celle qui nous aidera pour cette image.

[inserer les images cas2 dalton16: C0_C1 d'abord C2 ensuite]
[inserer les images de C0 C1 et C2 pour le cas2 dalton16]

Pour le nombre 42 les observations sont légerement differentes. En effet sur l'image originale nous pouvons observer 3 groupes principaux de couleur, du gris pour le fond, du rouge sur le 4 et du violet sur le 2.

[inserer les images cas1 dalton42: C0_C1 d'abord C2 ensuite]

Lorsqu'on observe la modélisation 3D de cette image, l'on remarque que l'axe C1 permet déjà de séparer les clusters principaux, de plus, l'axe C2 permets une autre séparation cette fois-ci en écartant le cluster violet des 2 autres, c'est pourquoi nous arrivons à observer le chiffre 2 dans l'image résultat de la composante C2

[inserer les images de C0 C1 et C2 pour le cas1 dalton42]