def hola1():
    print("hola")
    print("D:")

def hola3():
    print("hola3")
    print("aaaaaaaa")

import subprocess
import pyautogui
import time
import webbrowser

def abrir_notepad():
    subprocess.Popen(['notepad.exe'])
    time.sleep(1)  # Espera a que se abra
    pyautogui.write('Hola :D', interval=0.1)

def abrir_paint():
    subprocess.Popen(['mspaint.exe'])
    time.sleep(3)  # Espera a que Paint esté listo

    pyautogui.moveTo(400, 400)
    pyautogui.dragRel(200, 0, duration=0.5)   # derecha
    pyautogui.dragRel(0, 200, duration=0.5)   # abajo
    pyautogui.dragRel(-200, 0, duration=0.5)  # izquierda
    pyautogui.dragRel(0, -200, duration=0.5)  # arriba

def tomar_captura():
    screenshot = pyautogui.screenshot()
    screenshot.save('captura_pantalla.png')
    print("¡Captura tomada y guardada como 'captura_pantalla.png'!")

def buscar_en_google():
    webbrowser.open('https://www.google.com')
    time.sleep(3)
    pyautogui.write('Cae zoom a nivel mundial', interval=0.1)
    pyautogui.press('enter')


# abrir_notepad()
# abrir_paint()
# tomar_captura()
buscar_en_google()
