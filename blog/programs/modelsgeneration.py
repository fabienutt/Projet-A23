import base64
import time
from kittycad.client import Client
from typing import Any, List, Optional, Union
from kittycad.api.ai import create_text_to_cad
from kittycad.models import Error, TextToCad
from kittycad.models.file_export_format import FileExportFormat
from kittycad.models.text_to_cad_create_body import TextToCadCreateBody
from typing import Dict
from kittycad.api.ai import get_text_to_cad_model_for_user
from kittycad.client import Client
from kittycad.models.base64data import Base64Data
from kittycad.models.base64data import Base64Data
from kittycad.models.error import Error
from kittycad.types import Unset

def example_create_text_to_cad(text):
    # Create our client.
    client = Client(token="018cabf2-f724-7771-93b8-799d86d4923e")

    model_config = {'protected_namespaces': ()}
    result: Optional[Union[TextToCad, Error]] = create_text_to_cad.sync(
        client=client,
        output_format=FileExportFormat.GLTF,
        body=TextToCadCreateBody(
            prompt=text,
        ),
    )

    if isinstance(result, Error) or result == None:
        print(result)
        raise Exception("Error in response")

    body: TextToCad = result
    print(body.id)
    return body.id


# Fonction pour récupérer un modèle TextToCad pour un utilisateur
def example_get_text_to_cad_model_for_user(id1,name):
    # Créer le client avec votre jeton
    client = Client(token="018cabf2-f724-7771-93b8-799d86d4923e")

    # Appeler l'API pour récupérer le modèle TextToCad pour un utilisateur spécifique
    result: Optional[Union[TextToCad, Error]] = get_text_to_cad_model_for_user.sync(
        client=client,
        id=id1,
    )

    # Vérifier s'il y a une erreur dans la réponse
    if isinstance(result, Error) or result is None:
        print(result)
        raise Exception("Error in response")

    # Récupérer le corps de la réponse
    body: TextToCad = result
    print(body.outputs)
    
    #!/usr/bin/env python3

    fc: TextToCad = result

    print(f"File conversion id: {fc.id}")
    # Try adding your name by changing the text below to
    # print("<your-name>, congrats! Your STL conversion was successful:")
    print(f"File conversion status: {fc.status}")

    if isinstance(fc.outputs, Unset):
        raise Exception("Expected outputs to be set")

    outputs: Dict[str, Base64Data] = fc.outputs
    print(outputs)
    for _, output in outputs.items():
        output_file_path = f"C:/Users/FireF/OneDrive/Documents/GitHub/Projet-A23/Back/fichiers/{name}.gltf"
        print(f"Saving output to {output_file_path}")
        output_file = open(output_file_path, "wb")
        output_file.write(output.get_decoded())
        output_file.close()


def generation(name, text):
    id = example_create_text_to_cad(text)
    while True:
        
        try:
            
            time.sleep(2)
            print(text)
            print(name)
            example_get_text_to_cad_model_for_user(id, name)
            time.sleep(1)
            break  # Sort de la boucle si tout se passe bien
        except AttributeError:
            print("Erreur - Réessayer...")
            
            time.sleep(1)  


