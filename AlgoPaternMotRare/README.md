## Readme premier algorithme créer pour la reconaissance de patern dans un text.


Tout le projet sur la recherche de patern dans un text est disponible sur le git suivant : https://github.com/MaksDUT/ProjetTutore


Le but de ce programme et de retrouver des paterne par l'utilisation de *mot rare*.

le programme découpe le text en phrases pour ensuite découper les phrases par des groupes de *mots rares*.

les mots rares sont découper par un algo de découpe de n-gramme  (explication de ce qu'est un n-gramme [ici](https://fr.wikipedia.org/wiki/N-gramme "n-gramme wikipedia"))





### Utilisation du programme :

Le programme s'utilise avec python faite bien attention à l'avoir lancer avec la commande python. (en ligne de commande ) 

 ```
 python AlgoPaternMotRare.py Text.txt nbNgram tailleMinPatern nbErreur
 ```

 L'algorithme de partene neccesite 4 arguments au lancement : 

* **Text.txt**            le nom du fichier que l'on veut verifier 
* **nbNgram**             le nombre de mot par Ngrame (ex Ngram = 3 alors la decoupe des ressemblance se fera par group de mot de 3 : 'Je suis la ', 'Maison bleu ciel' ) 
* **tailleMinPatern**     le nombre de caractere minimal pour la comparaison de patern  
* **nbErreur**            nombre de caractere de diference entre deux patern accepter  ( si nbErreur < 1 prends la valeur par default de 3 ) 
Par default une page html sera créé dans le repertoire courant du programme