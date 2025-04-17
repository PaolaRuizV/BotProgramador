#!/usr/bin/env python3

import time
import speech_recognition as sr
import keyboard  # Necesitarás instalarlo con: pip install keyboard

# Esta función se llama desde el hilo en segundo plano
def callback(recognizer, audio):
    try:
        texto = recognizer.recognize_google(audio, language="es_PE")
        print("Google Speech Recognition thinks you said:", texto)
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
        time.sleep(0.1)
except KeyboardInterrupt:
    stop_listening(wait_for_stop=False)
    print("Interrupción manual detectada. Finalizando...")
