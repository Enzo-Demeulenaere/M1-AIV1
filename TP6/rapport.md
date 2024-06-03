1.

Les principales personnalités sont de lire une image et dessiner ses contours , ainsi que d'afficher une image en fonction de ses coutours qui sont récupérés depuis un fichier csv.

2.
Le descripteur Z0 correspond au barycentre de la forme.

On remarque que lorsque l'on additionne une constante complexe au descripteur Z0, la forme s'est déplacée sur l'axe y, c'est donc bien le barycentre qui s'est déplacé 

3. Lorsqu'on change la valeur du ratio de descripteurs non annulés l'on se rend compte que notre forme de carré est plus détaillée si ce ratio est grand et inversement, en effet si le ratio est trop bas, le peu de descripteurs retenus permettent de simplement afficher un cercle (voire un simple point si plus aucun descripteurs retenus)

Lorsqu'on étudie ces changements sur la force de cercle nous remarquons que ce cercle ne se modifie pas qu'importe son ratio de descripteurs retenus au delà de 0.03, autrement dit un ratio plus faible correspondrait à un nombre de descripteurs retenus nul soit un point une fois affichésoh , cela s'explique par le fait qu'un nombre très faible de descripteurs permet de dessiner un cercle comme on a pu l'observer pour le carré


Derniere partie. Pour L'instant nous n'arrivons pas à calculer les contours d'une image et en faire une compréhension cohérente, notre incohérence semble apparaitre seulement lors de l'appel à keepratio, or celle-ci fonctionne parfaitement sur les données du csv, j'ai remarqué que les coordoonnées du carré telles que calculées depuis l'image tracent le carré dans le "sens horaire" tandis que celles depuis les fichiers csv se tracent dans le sens trigonométrique mais cela n'explique pas le problème éventuel avec keep ratio.
Nous avons testé ce problème sur les autres formes également et il se reporte bien sur celles-ci [voir images "BROKEN"]  

Nous pensons avoir trouvé une solution qui consiste à non plus garder un ratio r des premiers descripteurs mais à ne garder que le ratio 1-r des premiers descripteurs et nous obtenons alors un résultat satisfaisant [images "GOOD"].

En essayant avec un ratio de 0.9 pour chaque image qui semble être un ratio de compression assez faible dans lequel l'on va garder une majorité des descripteurs, l'on remarque déjà que beaucoup de forment ne sont pas très bien reconstitués, et un ratio plus grand pour ces images reviendrait à effectuer une compression presque "négligeable" et donc inintéressante. En revanche, l'on peut remarquer que pour le trèfle ainsi que pour le patatoïde, les compressions parviennent à reconstituer des images très satisfaisantes et ce sont les formes qui possèdent le plus de "courbes" dans notre panel, peut-être que la méthode des descripteurs de Fourier est plus sensible à celles-ci et a plus de mal lorsqu'il s'agit de formes aux arrêtes plus "plates", d'où l'aspect un peu "gonflé" observé sur les formes basiques.

Cela se confirme lorsqu'on applique un ratio de compression de 0.2 sur le trèfle où on reconnait encore très bien la forme, observation plus minime sur le patatoïde où la forme abstraite est plus difficilement reconnaissable même avec un ratio de 0.5, remarquons que la "queue" qui parait très droite est la première chose à disparaitre lorsqu'on applique la compression, preuve que les contours droits ne sont pas bien reconnus et reconstitués dans cette méthode

