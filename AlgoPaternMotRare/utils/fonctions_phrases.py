import re
import string


def initEnsMots():
    """
    Initialise un ensemble avec tous les mots
    """
    fichier = open('liste_abrev.txt','r')
    ensemble = set()
    for line in fichier:
        ensemble.add(line[:-1])
    fichier.close()
    return ensemble

def tolower(mot):
    if mot == isAsciiLower(mot):
        return mot
    new_mot = ''
    for lettre in mot:
        if ord(lettre)>=65 and ord(lettre)<=90:
            new_mot += lettre.lower()
        if ord(lettre)<97 or ord(lettre)>122:
            if lettre == 'à' or lettre == 'â' or lettre == 'ä':
                new_mot += 'a'
            if lettre == 'é' or lettre == 'è' or lettre == 'ê' or lettre == 'ë':
                new_mot += 'e'
            if lettre == 'î' or lettre == 'ï':
                new_mot += 'i'
            if lettre == 'ö' or lettre == 'ô':
                new_mot += 'o'
            if lettre == 'ù' or lettre == 'ü' or lettre == 'û':
                new_mot += 'u'
            if lettre == 'ÿ':
                new_mot += 'y'
            if lettre == 'ç':
                new_mot += 'c'
        else :
            new_mot += lettre
    return new_mot


def isAsciiLower(mot):
    for lettre in mot:
        if ord(lettre)<97 or ord(lettre)>122:
            return False
    return True

def isAbreviation(ensemble, mot):
    """
    Retourne true si abréviation, false sinon
    """
    temp_mot = mot
    if len(mot)>=2:
        if mot[1]=="\'":
            temp_mot = mot[2:]
    if tolower(temp_mot) not in ensemble:
        return False
    return True

def filtered_list(lst, item):
    return [i for i in lst if i != item]



def ListePhrase(text):
    '''Cette fonction prend en argument un string, et renvoie une liste de tout les phrases du text'''
    
    ponct = ["!","?","."]
    resultat = list()
    tailleT=len(text)
    phrase=''   
    ens = initEnsMots() 
    
    for i in range(0,len(text)) :
        #permet de retirer les titres 
        if text[i-1] ==" " and text[i]==" ": 
             phrase=""
             
             
        #regarde si le caractere est une ponctuation ( ! ? . )
        if text[i] in ponct :
            
            if i==tailleT-2 or i==tailleT-1 :
                resultat.append(phrase)
                phrase=""
               
            elif i<len(text)-2 and text[i+1]==" " and re.search("[A-Z \- «]",text[i+2]):
                tempList = phrase.split(" ")
                tempWord = tempList[-1]
                if text[i-1]==text[i-2]=='.':
                    tempWord = tempWord[:-2]
                if isAbreviation(ens,tempWord):
                    #print(' abrev : ',tempWord,' : ',phrase) #afficher le mot considéré comme une abréviation et la phrase jusqu'à ce mot
                    phrase+=text[i]
                else:
                    resultat.append(phrase)
                    phrase=""
               
            else:
                phrase+=text[i]
               
        #sinon on ecrit sans retour à la ligne 
        else : 
            phrase+=text[i]
           
    return resultat 

def reducPhraseByLenWord(phrase,taille):
    
    phrase=phrase.lower()
    phrase=phrase.replace(",","").replace("'"," ").replace("--","").replace("\"","")
    
    phrase=phrase.split()
    i=0
    resultat = ""
    while i in range(len(phrase)) :
        
        if len(phrase[i]) <= taille  :
            i+=1
        else:
            resultat+=phrase[i]+" "
            i+=1
            
    
    return resultat[:-1]
    
def reducPhraseByList(phrase):
    
    phrase=phrase.lower()
    phrase=phrase.replace(",","").replace("'"," ").replace("--","").replace("\"","")
    liste = ["le","la","les","des","de","l","du","d","et","pour","à","un","on","ne","pas","m","n","une","qu","s","sur","son","aux","cette","en","au","que","ça","me","se","bon","comme","c","je","tu","il","elle","nous","vous","ils","elles","ah","j","ce","sa","mon","pas","eux","a","sans","dieu"]
    phrase=phrase.split()
    i=0
    resultat = ""
    while i in range(len(phrase)) :
        
        if phrase[i]  in liste :
            i+=1
        else:
            resultat+=phrase[i]+" "
            i+=1
            
    
    return resultat[:-1]
