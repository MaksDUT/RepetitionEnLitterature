## Readme pour le deuxieme algorithme créer pour la reconaissance de patern dans un text.


Tout le projet sur la recherche de patern dans un text est disponible sur le git suivant : https://github.com/MaksDUT/ProjetTutore


Le programme utilise un arbre de suffix, deja existant conçu par Kasrâ Vând. lien GitHub( https://github.com/kasramvd/SuffixTree )

On utilise le module pour créer l'arbre. On c'est inspiré de fonctions déja existantes *print_dfs()* et *walk_dfs()*  pour le parcourir et récuperer les informations voulu (les fonctions crée sont : *principal_repetition()* et *repetition()* ). 


### Utilisation du programme :

Le programme s'utilise avec python fait bien attention à l'avoir lancer avec la commande python. (en ligne de commande )        

```  
python algoPaternTree.py text.txt tailleMinAffiche nbErreur
```

le programme nécessite trois arguments :

* **text.txt**            le text à tester 
* **tailleMinAffiche**    la taille minimale des sequences recherchers 
* **nbErreur**            le nbErreur accepté entre les deux sequences trouvées 

les arguments -h et --help existent pour rappeler comment utilisé le programme 