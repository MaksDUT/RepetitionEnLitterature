
def ngramDico(phrase,n):

    phrase = phrase.split(" ")
    dico = {}
    ngram = ""
    for i in range(len(phrase)-(n-1)):
        for j in range(0,n):
            ngram += phrase[i+j]+" "
        
        if ngram in dico.keys():
            dico[ngram[:-1]]+=1
        else:
            dico[ngram[:-1]] = 1
        ngram = ""
    return dico

def ngramList(phrase,n):

    phrase = phrase.split(" ")
    liste = list()
    ngram = ""
    for i in range(len(phrase)-(n-1)):
        for j in range(0,n):
            ngram += phrase[i+j]+" "
        liste.append(ngram[:-1])
        ngram = ""
    return liste
