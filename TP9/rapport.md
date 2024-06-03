1.

matrice seuil à 125:
[[4636  964]
 [  75 4325]]
135:
[[5208  392]
 [ 215 4185]]
145:
[[5466  134]
 [ 602 3798]]

seuillage automatique : [4.054097] 138

3classes : [81.16309] 89 151

matrice 3 classes : 
[[5302  298    0]
 [ 432 3772  196]
 [   0   90 5510]]

On utilise donc les 2 images w1 et w2 du chiffre 0 pour segmenter l'image du chiffre 0 et on obtient un résultat très satisfaisant avec tout de même quelques pixels inexacts

On peut exploiter ce seuil trouvé pour segmenter l'image du chiffre 1 et on obtient un résultat aussi satisfaisant avec certains pixels inexacts mais on peut commenter sur l'efficacité de cette technique qui est très satisfaisante malgrè un nombre très leger d'erreurs