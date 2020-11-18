def fonctionHTML(liste,info) :

    texte = """<html>
        
        <link rel="stylesheet"  href="/style.css">
        
        
        

        <head id ="Titre">
        
        <charset=utf-8" />

        <title>Algo</title>
        <h1>
        Résultat Algo de Paterne :
        </h1>
        
        </head>
        
        <div id = "table">
        
        <h3>Phrase avec paterne </h3>
        
        
        <h2> Options </h2>
        
        <p> NOM du text : """
    texte += str(info[2])
        
    texte +=""" <p> Taille N-gram : """
    texte += str(info[0])
    texte +="""</p> <p> taille Minimal de phrase : """
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
            
            valueStartSeq1 ,valueEndSeq1 = element[2]
            valueStartSeq2 ,valueEndSeq2 = element[3]
            texte+= """
                <li>
                """
            for i in range(len(seq1)) :
                if i==valueStartSeq1 :
                    texte+="""<span style="color:red">"""
                texte+=seq1[i]
                    
                if i==valueEndSeq1 :
                    texte+='''</span>'''
            texte+="""
                    </li>
                    <li>     
                    """
            for j in range(len(seq2)) :
                if j==valueStartSeq2 :
                    texte+="""<span style="color:red">"""
                texte+=seq2[j]
                
                if j==valueEndSeq2 :
                    texte+='''</span>'''
            texte+="""
                    </li>    
                    
                    </ul> 
            
                    <hr color="grey">
                """    
        
        

    texte+= """
        </div>

        </html>
        """ 



    x=open(str(info[2])+'-ngram-'+str(info[0])+'.html','w', encoding = "utf-8")

    x.write(texte)

    x.close()


if __name__ == '__main__':
    dico = {"test" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]],
            "toto" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]],
            "tutu" : [["Coucou c'est moi la phrase de test a plus","Je suis aussi la phrase de test salut ",(17,33),(14,31)]]}
    info =[0,50]
    fonctionHTML(dico,info );
