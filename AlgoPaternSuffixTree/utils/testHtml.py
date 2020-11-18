def fonctionHTML(liste,info) :
    
    """fonctionHTLM permet de créer une page html pour le programme de repetition avec arbre de suffix """
    
    

    texte = """<html>
        
        <link rel="stylesheet"  href="/style.css">
        
        
        

        <head id ="Titre">
        
        <charset=utf-8" />

        <title>Algo Patern SuffixTree </title>
        <h1>
        Résultat Algo de Paterne par Arbre des suffix :
        </h1>
        
        </head>
        
        <div id = "table">
        
        <h3> Contenue créé pour un projet scolaire à l'université de Marne la Vallée </h3>
        
        
        <h2> Options </h2>
        
        <p> NOM du text : """
    texte += str(info[2])
        
    texte +=""" <p> Taille Minimal de phrase : """
    texte += str(info[0])
    texte +="""</p> <p> nombre d'erreur acceptée : """
    texte +=str(info[1])
    texte +="""</p> """
     

        
        
        
        #developement des phrases 

          
    for liste in liste.values() :
        for element in liste :
            texte+="""
                <hr color="grey">
                
                <ul style="list-style-type:disc;">
                """
                
            seq1 = element[0]
            seq2 = element[1]
            
            
            texte+= """
                    <li>
                    """
            texte+=seq1
            texte+="""
                    </li>
                    <li>     
                    """
            texte+=seq2

            texte+="""
                    </li>    
                    
                    </ul> 
            
                    <hr color="grey">
                    """    
        
        

    texte+= """
        </div>

        </html>
        """ 



    x=open(str(info[2])+'--'+str(info[0])+'.html','w', encoding = "utf-8")

    x.write(texte)

    x.close()


if __name__ == '__main__':
    dico = {"test" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]],
            "toto" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]],
            "tutu" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]]}
    info =[0,50]
    fonctionHTML(dico,info );
