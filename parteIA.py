import requests
import os
from dotenv import load_dotenv
from funciones import *

load_dotenv()
API_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://router.huggingface.co/hf-inference/pipeline/sentence-similarity/sentence-transformers/all-MiniLM-L6-v2"

headers = {
    "Authorization": f"Bearer {API_TOKEN}",
}

# Funcion para devolver la accion que mejor corresponde a un prompt ingresado
def buscar_funcion_correspondiente(prompt: str, threshold: float = 0) -> Accion:
    
    listaOpciones = list( acciones.descripcion for acciones in LISTA_ACCIONES ) # solo conserva las descripciones de la lista de funciones
    
    # preparar data para enviar a la IA
    payload = {
        "inputs": {
            "source_sentence": prompt,
            "sentences": listaOpciones
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    similarity_scores = response.json()

    # Codigo para checar errores desde la solicitud API
    if isinstance(similarity_scores, dict) and "error" in similarity_scores:
        print( Exception(f"API Error: {similarity_scores['error']}") )
        return ACCION_ERROR
    
    # Se obtiene el indice de la mejor opcion similar
    best_idx = int(max( range(len(similarity_scores)), key=lambda i: similarity_scores[i]) )

    # ? OPTIONAL - en caso la mejor opcion tenga una similitud menor al threshold, entonces no se considera
    if similarity_scores[best_idx] < threshold:
        return ACCION_ERROR

    return LISTA_ACCIONES[best_idx]  # Esto es una lista con los valores de similaridad

# if name main para solo en caso se ejecute este archivo solo
if __name__ == "__main__":

    # *
    # * FUNCIONAMIENTO DE EJEMPLO 
    # *
    load_dotenv()

    API_TOKEN = os.getenv("HF_API_TOKEN")
    API_URL = "https://router.huggingface.co/hf-inference/pipeline/sentence-similarity/sentence-transformers/all-MiniLM-L6-v2"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
    }

    def query_similarity(source_sentence, target_sentences):
        payload = {
            "inputs": {
                "source_sentence": source_sentence,
                "sentences": target_sentences
            }
        }
        response = requests.post(API_URL, headers=headers, json=payload)
        data = response.json()

        # Codigo para checar errores desde la solicitud API
        if isinstance(data, dict) and "error" in data:
            raise Exception(f"API Error: {data['error']}")
        
        return data  # Esto es una lista con los valores de similaridad

    # Definir la lista de acciones
    actions = ["raises the volume up", "lowers the volume down", "jumps to next song", "stop the song", "search for a song"]
    actions = ["aumenta el volumen del sonido", "baja el volumen de sonido", "pasa a la siguiente cancion", "hace pausa en la cancion que este sonando", "busca por una cancion especifica"]

    # Definir el "input del usuario"
    prompt = "please low the music, it is too loud"
    prompt = "low the music"

    # Obtener los scores de similaridad
    similarity_scores = query_similarity(prompt, actions)

    # Encontrar el valor mayor entre todos los de la lista
    best_idx = int(max( range(len(similarity_scores)), key=lambda i: similarity_scores[i]) )

    # Salida del codigo
    print(f"Best match: '{actions[best_idx]}' with confidence {round(similarity_scores[best_idx], 2)}")
    print("All actions and scores:", list(zip(actions, [round(s, 2) for s in similarity_scores])))