
""" Ceci est un programme qui a pour but de trouver des récurences dans un text donné en argument. 
    Le programme utilise un arbre de suffix, deja existant conçu par Kasrâ Vând lien GitHub( https://github.com/kasramvd/SuffixTree )
    On utilise le module pour créer l'arbre, et on c'est inspiré de fonctions deja existantes (print_dfs() et walk_dfs() ) pour le parcourir et récuperer les informations voulu (les fonctions crée sont : principal_repetition() et repetition() ). 
    
    Utilisation :
        
        AlgoPaternTree text.txt tailleMinAffiche nbErreur
        
        le programme neccecite trois arguments 
            - 'text.txt'            le text a tester
            - 'tailleMInAffiche'    la taille minimal des sequences recherchers 
            - 'nbErreur'            le nbErreur accepté entre les deux sequences trouvées 
"""

import sys
import re
import collections

from utils.testHtml import fonctionHTML
from SuffixTree.suffixtree import SuffixTree
from SuffixTree.modules import CheckSubString
from utils.fonctions_levenshtein import *

def usage() :
    print("Utilisation : \n \
        \n \
        nomProgramme text.txt tailleMinAffiche nbErreur \n \
        \n \
        le programme neccecite trois arguments \n \
            - 'text.txt'            le text a tester \n \
            - 'tailleMInAffiche'    la taille minimal des sequences recherchers \n \
            - 'nbErreur'            le nbErreur accepté entre les deux sequences trouvées ")


def dictSorted(dico):
    dicoFinal = collections.OrderedDict()
    
    for key in sorted(dico.keys(),reverse=True):
        dicoFinal[key] = dico[key]
    return dicoFinal

def concatenerText(phrase) :
    """ Fonction qui permet de rendre un text en une chaine de caractere sans ponctuation, et accent"""
    phrase=phrase.lower()
    resultat =""
    i = 0
    dico = {}
    for lettre in phrase:
        boo = False
        if ord(lettre)<97 or ord(lettre)>122: 
            
            if lettre == 'à' or lettre == 'â' or lettre == 'ä':
                resultat += 'a'
                boo =True
            elif lettre == 'é' or lettre == 'è' or lettre == 'ê' or lettre == 'ë':
                resultat += 'e'
                boo =True
            elif lettre == 'î' or lettre == 'ï':
                resultat += 'i'
                boo =True
            elif lettre == 'ö' or lettre == 'ô':
                resultat += 'o'
                boo =True
            elif lettre == 'ù' or lettre == 'ü' or lettre == 'û':
                resultat += 'u'
                boo =True
            elif lettre == 'ÿ':
                resultat += 'y'
                boo =True
            elif lettre == 'ç':
                resultat += 'c'
                boo =True
                
            if boo :
                if len(resultat) %1000 == 0 :
                    dico[len(resultat)] = i
        
        else :
            resultat += lettre
            if len(resultat)%1000 == 0 :
                    dico[len(resultat)] = i
        
        i=i+1
    
    return resultat , dico
    
def traitementLien(dico,text,pos) :
    """ le traitement qui permet de faire le lien entre le text principal et le text modifier en chaine de caractere """
    depart = pos//1000
    y = pos%1000
    
    compteur = 0
    
    for i in range(dico[depart*1000],len(text)) :
        if(compteur == y ) :
            return i
        
        lettre = text[i]
        boo = False
        if ord(lettre)<97 or ord(lettre)>122: 
            
            if lettre == 'à' or lettre == 'â' or lettre == 'ä':
                boo =True
            elif lettre == 'é' or lettre == 'è' or lettre == 'ê' or lettre == 'ë':
                boo =True
            elif lettre == 'î' or lettre == 'ï':
                boo =True
            elif lettre == 'ö' or lettre == 'ô':
                boo =True
            elif lettre == 'ù' or lettre == 'ü' or lettre == 'û':
                boo =True
            elif lettre == 'ÿ':
                boo =True
            elif lettre == 'ç':
                boo =True
            
            if boo :
                compteur += 1
                   
        
        else :
            compteur += 1
        

def lienText(text,dico,posDseq1 , posFseq1 , posDseq2, posFseq2) :
    
    """  """
    iposDseq1 = traitementLien(dico,text,posDseq1)
    iposDseq2 = traitementLien(dico,text,posDseq2)
    iposFseq1 = traitementLien(dico,text,posFseq1)
    iposFseq2 = traitementLien(dico,text,posFseq2)
    

    
    
    return text[iposDseq1:iposFseq1] , text[iposDseq2:iposFseq2] 
    

def fonctionTree(posDseq1, posFseq1, posDseq2, posFseq2, text ) :
    
    '''
        retourn les positions de debut et de fin des deux sequences avec les ajouts (nbErreur)  
    '''
    
    global nbErreur
    
    taille = (posFseq1 - posDseq1) *3
    
    tailleMaxText =len(text)
    
    posFinseq1 = posFseq1 + taille
    posFinseq2 = posFseq2 + taille
   
    
    
    if posFinseq1 > tailleMaxText :
        posFinseq1 = tailleMaxText
    
    if posFinseq2 > tailleMaxText :
        posFinseq2 = tailleMaxText
    
    
    sq1 = text[posDseq1:posFinseq1 ]
    sq2 = text[posDseq2:posFinseq2 ]
    
    
    result1 =fonctionLevenshteinTree(sq1,sq2,nbErreur)
    
    posDebseq1 = posDseq1 - taille
    posDebseq2 = posDseq2 - taille
    
    if posDebseq1 < 0 :
        posDebseq1 = 0
    
    if posDebseq2 < 0 :
        posDebseq2 = 0
    
    sq1 = text[posDebseq1:posFseq1 ]
    sq2 = text[posDebseq2:posFseq2 ]
    
    result2 =fonctionLevenshteinTree(sq1[::-1], sq2[::-1], nbErreur)
    
    
    if (result1 > result2) :
        posFinseq1 = posDseq1 + result1
        posFinseq2 = posDseq2 + result1
        
        return posDseq1 , posFinseq1 , posDseq2 , posFinseq2
    
    posDebseq1 = posFseq1 -result2
    posDebseq2 = posFseq2 -result2
    
    return posDebseq1 , posFseq1 , posDebseq2 , posFseq2





if __name__ == '__main__':
    
    
    #take args 
    
    argv = sys.argv[1:]
    if len(argv)>0 :
        
        if argv[0] == "--help" or argv == "-h" :
            usage()
            sys.exit(2)
    
    
    if len(argv)!= 3 :
        usage()
        sys.exit(2)
    
    
    textFile = argv[0]
    tailleMInAffiche = int(argv[1])
    nbErreur = int(argv[2])
    tailleMinPatern = 20
    listeText =[]
    

    with open(textFile,"r",encoding="utf-8") as file:
        

        #on "nettoie" le texte puis on réunit les mots
        text = file.read()
        textTraiter,listeText = concatenerText(text)
    
    tree4 = SuffixTree(textTraiter)
    tree4.build_suffix_tree()
    
    print("-----------------------------------------------------")
    
    dicoRepet,dicoInfo = tree4.principal_repetition(tailleMinPatern)
    
    sys.getrefcount(tree4)
    del tree4
    
    dicoResultat ={}
    listeRepet =[]
    
    for key in dicoRepet.keys() :
        
        
        if(len(dicoInfo[key]) == 2):
            
            positionText1Debut,positionText1Fin = dicoInfo[key][0]
                    
            positionText2Debut,positionText2Fin = dicoInfo[key][1]
                    
            posDseq1 , posFseq1 , posDseq2 , posFseq2 =fonctionTree(positionText1Debut, positionText1Fin, positionText2Debut, positionText2Fin, textTraiter)
            
            if (posDseq1 , posFseq1) not in listeRepet :
            
                seq1 = posFseq1 - posDseq1 
               
                
                
                if (seq1 >= tailleMInAffiche) :
                    
                    dicoKey = seq1 
                    
                    if (dicoKey in dicoResultat ):
                        dicoResultat[dicoKey].append(lienText(text,listeText,posDseq1 , posFseq1 , posDseq2, posFseq2))
                    
                    else :
                        dicoResultat[dicoKey] = list()
                        dicoResultat[dicoKey].append(lienText(text,listeText,posDseq1 , posFseq1 , posDseq2, posFseq2))
                    
                    listeRepet.append((posDseq1 , posFseq1))
               
    option = [tailleMInAffiche,nbErreur,textFile]
    dicoResultat=dictSorted(dicoResultat)
    fonctionHTML(dicoResultat,option)

