import time
import speech_recognition as sr
from funciones import *
from parteIA import buscar_funcion_correspondiente

RECOGNIZER = "google" # o puede remplazarlo por "google" o "whisper"

# Esta función se llama desde el hilo en segundo plano
def callback(recognizer: sr.Recognizer, audio):
    try:
        if RECOGNIZER == "whisper":
            texto = recognizer.recognize_whisper(audio, model="tiny") # Modelos (somehow se instalan solos en la primer ejecucion) 'tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large']
            print("Speech Recognition escucha esto:", texto)
        elif RECOGNIZER == "google":
            texto = recognizer.recognize_google(audio, language="es_PE")
            print("Google Speech Recognition escucha esto:", texto)
        
        # La funcion retorna una ACCION, por lo cual solo se ejecuta la funcion
        opcion = buscar_funcion_correspondiente()
        opcion.funcion()

    except sr.UnknownValueError:
        print("No se entendió el audio")
    except sr.RequestError as e:
        print("Error al comunicarse con el servicio de Google:", e)

# Inicializamos el reconocedor y el micrófono
r = sr.Recognizer()
r.energy_threshold = 45
m = sr.Microphone()

#Inicializar IA


# Calibrar ruido ambiental
with m as source:
    print("Ajustando al ruido ambiental, espere un momento...")
    r.adjust_for_ambient_noise(source)
    print("Listo. Comenzando a escuchar...")

# Empezar a escuchar en segundo plano
stop_listening = r.listen_in_background(m, callback)

# Bucle principal, se detiene si se presiona la tecla "q"
print("Presiona 'q' para salir del programa.")

try:
    while True:
        a = input()
        if a.upper() == "Q":
            stop_listening(wait_for_stop=False)
            break
        time.sleep(3)
        
except KeyboardInterrupt:
    stop_listening(wait_for_stop=False)
    print("Interrupción manual detectada. Finalizando...")
