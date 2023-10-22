#Traitement des données : 
    # Mots clés à récupérer dans le texte et enregistrer le texte dans un repertoire une fois validé pour pouvoir avoir un corpus à fournir à la base de données
    # Algo a faire dans une autre fonction
    # Retourner les resultats du choix des composants / modele 3D / le reste 
from datetime import datetime

def getdate():
    # Récupération de la date et de l'heure actuelles
    now = datetime.now()
    # Conversion en string avec le format souhaité
    formatted_date = now.strftime('%Y%m%d%H%M%S')
    return formatted_date

def process_data(data):
    result=data
    liste=result.split(" ")
    for elt in liste:
        if len(elt)<4:
            liste.remove(elt)
    result=""
    for elt in liste:
        result+=elt+'; '
    #sauvegarde du prompt
    with open('blog/programs/datas/'+getdate()+'.txt','w' )as file :
        file.write(result)
    return result

      
    
