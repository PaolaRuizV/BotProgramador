import requests
import os
from dotenv import load_dotenv


# if name main para solo en caso se ejecute este archivo solo
if __name__ == "__main__":
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
    actions = ["volume up", "volume down", "next song", "pause", "search song"]

    # Definir el "input del usuario"
    prompt = "stop the music"

    # Obtener los scores de similaridad
    similarity_scores = query_similarity(prompt, actions)

    # Encontrar el valor mayor entre todos los de la lista
    best_idx = int(max( range(len(similarity_scores)), key=lambda i: similarity_scores[i]) )

    # Salida del codigo
    print(f"Best match: '{actions[best_idx]}' with confidence {round(similarity_scores[best_idx], 2)}")
    print("All actions and scores:", list(zip(actions, [round(s, 2) for s in similarity_scores])))