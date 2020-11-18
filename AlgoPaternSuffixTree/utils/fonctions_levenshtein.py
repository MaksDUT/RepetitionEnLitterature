import numpy as np

ponct =[",",";","!","?",".",":","'","-"]

def deletPonctuation(phrase) :
    phrase=phrase.lower()
    resultat =""
    for element in phrase:
        if element not in ponct :
            resultat+=element
            
    return resultat

def levenshteinMatrix(seq1,seq2):
    ''' 
    levenshteinMatrix renvoie la matrice de levenshtein des deux chaines de caracteres 
    
    arguments : seq1 , seq2
        seq1 et seq2 sont deux chaines de caracteres
    
    
    Retourne une matrice
    '''
    
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y),dtype=int)
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    
    return matrix
    
def levenshteinMatrixFinal(seq1,seq2, nbErreur):
    
    '''
    arguments : seq1 , seq2
        seq1 et seq2 sont deux chaines de caracteres
     
    levenshteinMatrixFinal renvoie une liste [varBoolean,positionSeq1,positionSeq2,taille]
        
        -varBoolean : True si les deux sequences seq1 et seq2 ont un paterne en commun de taille > min(len(seq1),len(seq2))/divisionPhrase  False sinon.
        -positionSeq1 : tuple de la position du paterne (positionStart, positionEnd)
        -positionSeq2 : tuple de la position du paterne (positionStart, positionEnd)
        -taille : taille du paterne
     
    Retourne une liste 
    '''
    
    liste_final =[False,-1,-1,-1]
    divisionPhrase = 3
    
    size_i = len(seq1) + 1
    size_j = len(seq2) + 1
    
    if size_i <size_j :
        size_final=size_i//divisionPhrase
        
    else :
        size_final=size_j//divisionPhrase
        
        
    matrix = levenshteinMatrix4(seq1,seq2,size_final)
    
    
    for element in matrix:
        
        ti,tj=element.shape
        taille_i=size_i-ti
        taille_j=size_j-tj   
        liste = np.diagonal(element)
        liste = liste.tolist()
        
        liste_traitement = traitement(liste,size_final,nbErreur)
        if(liste_traitement[0]) :
            if liste_traitement[3]>liste_final[3]:
                
                liste_fin = [liste_traitement[0],(liste_traitement[1]+taille_i,liste_traitement[2]+taille_i),(liste_traitement[1]+taille_j,liste_traitement[2]+taille_j),liste_traitement[3]] 
                
                liste_final=liste_fin
    
    return liste_final

def traitement(liste,size_final,nbErreur ):
    '''
    arguments : liste , size_final
        liste : liste de int  ( diagonal de la matrice ) 
        size_final : int taille min du paterne
     
    traitement renvoie une liste [varBoolean,position_debut,position_fin,taille]
        
        -varBoolean : True si les deux sequences seq1 et seq2 ont un paterne en commun de taille > min(len(seq1),len(seq2))/divisionPhrase  False sinon.
        -position_debut : position du debut du parterne
        -position_fin : position de fin du parterne
        -taille : taille du paterne
     
    Retourne une liste 
    '''
    if nbErreur < 1 :
        nbErreur = 3
    
    vErreur = nbErreur
    
    
    position = 0
    position_debut=-1
    taille_fin = -1
    
    compteur = 0
    sauvegarde = -1
    valeur = 0
    erreur = 3
    taille = 0
    
    
    while(compteur<len(liste)) :
        if liste[compteur]!=valeur:
            if erreur ==vErreur :
                sauvegarde = compteur
            erreur+=-1
            valeur=liste[compteur]
        
        if erreur == 0 :
            if taille >= size_final:
                
                if(taille > taille_fin) :
                    
                    position_debut=position 
                    taille_fin = taille
            
            erreur = vErreur
            compteur =sauvegarde
            taille=0
            valeur=liste[sauvegarde]
            position = sauvegarde 
        
        compteur+=1
        taille+=1
    
    if taille >= size_final:
                
                if(taille > taille_fin) :
                    
                    position_debut=position 
                    taille_fin = taille  
    
    if position_debut!=-1 :
        position_fin = position_debut+taille_fin
        return [True,position_debut,position_fin,taille_fin]    
    return [False]    
    
def levenshteinMatrix4(seq1,seq2,size_final) :  
    
    '''
    arguments : seq1 , seq2 , size_final
        seq1 et seq2 sont deux chaines de caracteres
        size_final integer 
    
    levenshteinMatrix4 renvoie une liste de matrice 
        
    Retourne une liste 
    '''    

  
    size_i = len(seq1) + 1
    size_j = len(seq2) + 1
    
    listeMatrixe = []
    	
    for i in range(size_i-size_final):
        listeMatrixe.append(levenshteinMatrix(seq1[i:],seq2))
    for j in range(size_j-size_final):
        listeMatrixe.append(levenshteinMatrix(seq1,seq2[j:]))
   
    return listeMatrixe
  

#---------------------------------------------------------------------------------------------------

def levenshteinMatrixtoto(seq1,seq2 ,nbErreur) :  
    
    '''
    arguments : seq1 , seq2 , size_final
        seq1 et seq2 sont deux chaines de caracteres
        size_final integer 
    
    levenshteinMatrix4 renvoie une liste de matrice 
        
    Retourne une liste 
    '''    

    liste_final =[False,-1,-1,-1]
    divisionPhrase = 3
    
    size_i = len(seq1) + 1
    size_j = len(seq2) + 1
    
    if size_i <size_j :
        size_final=size_i//divisionPhrase
        
    else :
        size_final=size_j//divisionPhrase
    
	
    for i in range(size_i-size_final):
        matrix =levenshteinMatrix(seq1[i:],seq2)
        fonctionTest(matrix,liste_final,size_final,nbErreur, size_i , size_j)
    
        
    
    for j in range(size_j-size_final):
        matrix =levenshteinMatrix(seq1,seq2[j:])
        liste_final =fonctionTest(matrix,liste_final,size_final,nbErreur, size_i , size_j)
    
    del matrix
    
    
    return liste_final



def fonctionTest(matrix,liste_final, size_final, nbErreur, size_i , size_j) :
    
    ti,tj=matrix.shape
    taille_i=size_i-ti
    taille_j=size_j-tj   
    liste = np.diagonal(matrix)
    liste = liste.tolist()
    
    liste_traitement = traitement(liste,size_final,nbErreur)
    
    if(liste_traitement[0]) :
            if liste_traitement[3]>liste_final[3]:
                
                liste_final = [liste_traitement[0],(liste_traitement[1]+taille_i,liste_traitement[2]+taille_i),(liste_traitement[1]+taille_j,liste_traitement[2]+taille_j),liste_traitement[3]] 
                
                
                
    return liste_final


#--------------------------------------------------------------------------------------------------------

  
  
def levenshteinTest(seq1,seq2) :
    ''' fonction qui renvoie True si une portion des deux phrases sont identique  '''
    seq1 = deletPonctuation(seq1)
    seq2 = deletPonctuation(seq2)
    
    seq1 = seq1.replace(" ","")
    seq2 = seq2.replace(" ","")
  
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    
    if size_x <size_y :
        size_final=size_x//3
    else :
        size_final=size_y//3
     
    matrix = levenshteinMatrix(seq1,seq2)
    
    if(size_x<size_y):
        lonR=size_x
    else:
        lonR=size_y
    liste=[]
    for i in range(lonR):
        liste.append(int(matrix[i,i]))
    
    compteur = 0
    sauvegarde = -1
    valeur = 0
    erreur = 3
    taille = 0
    
    while(compteur<len(liste)) :
        if liste[compteur]!=valeur:
            if erreur ==3 :
                sauvegarde = compteur
            erreur+=-1
            valeur=liste[compteur]
        
        if erreur == 0 :
            if taille >= size_final:
                
                return True 
            
            erreur = 3
            compteur =sauvegarde
            taille=0
            valeur=liste[sauvegarde]
        
        compteur+=1
        taille+=1
        
            
    return False
    

def levenshteinPhraseByWord(seq1, seq2):
    '''fonction levenshtein pour les phrases : compares chaque phrases mots par mots '''
    seq1 = deletPonctuation(seq1)
    seq2 = deletPonctuation(seq2)
    
    seq1 = seq1.split()
    seq2 = seq2.split()
    
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    
    matrix = levenshteinMatrix(seq1,seq2)
    
    return (matrix[size_x - 1, size_y - 1])
    
def levenshteinPhraseByCara(seq1, seq2):
    '''fonction levenshtein pour les phrases : compares chaque phrases caractere par caractere '''
    
    seq1 = deletPonctuation(seq1)
    seq2 = deletPonctuation(seq2)
    
    seq1 = seq1.replace(" ","")
    seq2 = seq2.replace(" ","")
    
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
        
    matrix = levenshteinMatrix(seq1,seq2)
    
    return (matrix[size_x - 1, size_y - 1])

def nlevenveshteinPhrase(seq1, seq2) :
    ''' fonction qui donne le ratio de ressemblance entre deux phrases'''
    test1 = seq1.lower()
    test2 = seq2.lower()
    
    long1 = len(test1)
    long2 = len(test2)
    
    
    
    if(long1 < long2):
        result = long2
    else :
        result = long1
        
    levensh = levenshteinPhraseByCara(seq1,seq2)
   
    return  levensh/result
    
 

def traitementListTree(liste , nbErreur) :
    
    if nbErreur < 1 :
        nbErreur = 10
    
    vErreur = nbErreur
    compteur = 0
    valeur = 0
    erreur = 3

    
    
    while(compteur<len(liste)) :
        
        if liste[compteur]!=valeur:
            erreur+=-1
            valeur=liste[compteur]
        
        if erreur == 0 :
            
            return compteur
        
        compteur+=1

    
    
    return compteur 
    
    
def fonctionLevenshteinTree(seq1 , seq2 , nbErreur) :
    
    matrix = levenshteinMatrix(seq1,seq2)
    liste = np.diagonal(matrix)
    
    del matrix
    resultat = traitementListTree(liste, nbErreur)
    
    seq1 = seq1[:resultat]
    seq2 = seq2[:resultat]
    
    return resultat


