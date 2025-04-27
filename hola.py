#!/usr/bin/env python3

import time
import speech_recognition as sr
import keyboard  # Necesitarás instalarlo con: pip install keyboard
from funciones import *

# Esta función se llama desde el hilo en segundo plano
def callback(recognizer: sr.Recognizer, audio):
    try:
        texto = recognizer.recognize_whisper(audio, model="tiny.en") # Modelos (somehow se instalan solos en la primer ejecucion) 'tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large']
        print("Google Speech Recognition thinks you said:", texto)
        
        #TODO Implementacion de IA para interpretar el msg
        if ( texto.find("Google") != -1 ):
            buscar_en_google()

    except sr.UnknownValueError:
        print("No se entendió el audio")
    except sr.RequestError as e:
        print("Error al comunicarse con el servicio de Google:", e)

# Inicializamos el reconocedor y el micrófono
r = sr.Recognizer()
r.energy_threshold = 45
m = sr.Microphone()

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
        if keyboard.is_pressed('q'):
            print("Deteniendo escucha...")
            stop_listening(wait_for_stop=False)
            break
        a = input()
        b = input()
        if a.upper() == "Q" or b.upper() == "Q": break
        print(f"Suma: {int(a)+int(b)}")
        time.sleep(3)
except KeyboardInterrupt:
    stop_listening(wait_for_stop=False)
    print("Interrupción manual detectada. Finalizando...")
