
""" L'algorithme de partene neccesite 4 arguments au lancement : \n \
        'AlgoPaternMotRare.py Text.txt nbNgram tailleMinPatern nbErreur' \n  \n \
        Text.txt            le nom du fichier que l'on veut verifier \n \
        nbNgram             le nombre de mot par Ngrame (ex Ngram = 3 alors la decoupe des ressemblance se fera par group de mot de 3 : 'Je suis la ', 'Maison bleu ciel' ) \n \
        tailleMinPatern     le nombre de caractere minimal pour la comparaison de patern  \n \
        nbErreur            nombre de caractere de diference entre deux patern accepter  ( si nbErreur < 1 prends la valeur par default de 3 ) \n \n \
    Par default une page html sera créé dans le repertoire courant du programme
"""


import collections
import time
import sys
from progress.bar import ChargingBar

import sys
#--------------------------import fonctions Créer----------------------------------

from utils.testHtml import *
from utils.fonctions_phrases import *
from utils.fonctions_ngram import *
from utils.fonctions_levenshtein import *

#----------------------------------------------------------------------------------

def dictSorted(dico):
    dicoFinal = collections.OrderedDict()
    
    for key in sorted(dico.keys(),reverse=True):
        dicoFinal[key] = dico[key]
    return dicoFinal
    

def usage() :
    print("\n L'algorithme de partene neccesite 4 arguments au lancement : \n \
        'AlgoPaternMotRare.py Text.txt nbNgram tailleMinPatern nbErreur' \n  \n \
        Text.txt            le nom du fichier que l'on veut verifier \n \
        nbNgram             le nombre de mot par Ngrame (ex Ngram = 3 alors la decoupe des ressemblance se fera par group de mot de 3 : 'Je suis la ', 'Maison bleu ciel' ) \n \
        tailleMinPatern     le nombre de caractere minimal pour la comparaison de patern  \n \
        nbErreur            nombre de caractere de diference entre deux patern accepter  ( si nbErreur < 1 prends la valeur par default de 3 ) \n \n \
Par default une page html sera créé dans le repertoire courant du programme")
        
        

if __name__ == '__main__':
    
    
    #take args 
    
    argv = sys.argv[1:]
    if len(argv)>0 :
        
        if argv[0] == "--help" or argv == "-h" :
            usage()
            sys.exit(2)
    
    
    if len(argv)!= 4 :
        usage()
        sys.exit(2)
    
    
    textFile = argv[0]
    ngramArg = int(argv[1])
    valMinPatern = int(argv[2])
    nbErreur = int(argv[3])
    
    
    print("Ouverture Fichier")
        
        
    
    with open(textFile,"r",encoding="utf-8") as file:
        #on "nettoie" le texte puis on réunit les mots
        text = file.read().replace("\n"," ").replace("...."," ").replace("..."," ").replace("\"","")
    text=re.sub("\s{1,20} "," ",text)
        
    print("Fermeture Fichier")
    
    valueRecherche=2
        
    dico = {}
        
        
    print("Traitement Ngram ... ")
        
    #on parcour phrase par phrase tout les ngram que l'on met dans deux dico un pour le lier a la phrase et un pour le nombre de répetition  
    #---------------------------------------------------------------------------
    dico2 = {}
    test=ListePhrase(text)
    liste = list()
    
    for element in test: 
        phraseReduc=reducPhraseByList(element)
        liste=ngramList(phraseReduc,ngramArg)
        
        for el in liste:
            if el in dico.keys():
                dico[el]+=1
            else:
                dico[el]=1
            
            if el in dico2.keys():
                dico2[el].append(element)
                
            else:
                dico2[el]=list()
                dico2[el].append(element)
        liste[:]=[]       
    
    
    
    
    #affichage 
    
    #print(dico2)
    
    print("######################################################## N GRAMME ################################################################")
    
    toto= [k for k, v in dico.items() if v == valueRecherche]
    print("keys : "+str(toto))
    print(len(toto))
    total = len(toto)
    print("###################################################################################################################################")
    
    del dico
    
    i = 0
    listeValueAfterLevenshtein = []
    listeValueTraiter = []
    
    dico_fin=dict()
    compteur = 1
    
    # Debut du decompte du temps
    
    start_time = time.time()
    
    bar = ChargingBar("Processing", max=total,suffix='%(percent)d%%')
    
    for element in toto :
        bar.next()
        compteur +=1
        traitement = False
        
        seq1 = dico2[element][0]
        seq2 = dico2[element][1]
        
        if  (len(seq1) > valMinPatern and len(seq2) > valMinPatern ):
            for ngram in listeValueTraiter :
                if ((dico2[ngram][0] == seq1) and (dico2[ngram][1] == seq2 )):
                    traitement=True
        
                    break
            if not traitement :  
                liste_result_final=levenshteinMatrixtoto(seq1,seq2,nbErreur)  
                if (liste_result_final[0]) :
                    
                    dico_key = liste_result_final[3]
                    
                    if (dico_key in dico_fin ):
                        dico_fin[dico_key].append([seq1,seq2,liste_result_final[1],liste_result_final[2]])
                    else :
                        dico_fin[dico_key] = list()
                        dico_fin[dico_key].append([seq1,seq2,liste_result_final[1],liste_result_final[2]])
                   
                   
        listeValueTraiter.append(element)
        
    dico_fin=dictSorted(dico_fin)
    bar.finish()
    
    # Affichage du temps d execution
    print("Temps d execution pour",len(toto)," fonction levenshteinMatrixFinal lancé : %s secondes ---" % (time.time() - start_time))
    
   
    option = [ngramArg,valMinPatern,textFile]    
    
    fonctionHTML(dico_fin,option)
