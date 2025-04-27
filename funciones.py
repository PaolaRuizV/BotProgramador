import subprocess
import pyautogui
import time
import webbrowser
import types

# La clase para contener las acciones que puede realizar el bot
class Acciones:
    def __init__(self, nombre_: str, descripcion_: str, funcion_: types.FunctionType):
        self.nombre = nombre_           # Esto es el nombre de la accion
        self.descripcion = descripcion_ # Esto explica de que se trata esta accion
        self.funcion = funcion_         # Esto es la funcion que va ejecutar la accion
        pass
    
from AppOpener import open

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

def reproducir_youtube():
    webbrowser.open('https://www.youtube.com')
    time.sleep(5)

    pyautogui.press('tab', presses=4, interval=0.2)  # navegar hasta el campo de búsqueda
    pyautogui.press('enter')
    time.sleep(1)

    pyautogui.write('Hola mundo', interval=0.1)
    pyautogui.press('enter')
    time.sleep(5)

    pyautogui.moveTo(350, 350)
    pyautogui.click()

    #pyautogui.press('tab', presses=4, interval=0.3)  # Ir al primer video
    #pyautogui.press('enter')  # Reproducir


LISTA_ACCIONES = [
    Acciones(
        nombre_= "Abrir Notepad",
        descripcion_= "La funcion abre NotePad en Windows",
        funcion_= abrir_notepad
    )
    # Agregar mas funciones

]



def abrirSpotify():
    open('spotify') 
    time.sleep(5)

    pyautogui.press('tab', presses=17, interval=0.5) 
    pyautogui.press('enter')
    time.sleep(1)

def pasarDeCancionSpotify():
    open('spotify') 
    time.sleep(5)

    pyautogui.press('tab', presses=18, interval=0.5) 
    pyautogui.press('enter')
    time.sleep(1)

def retrocederCancionSpotify():
    open('spotify') 
    time.sleep(5)

    pyautogui.press('tab', presses=16, interval=0.5) 
    pyautogui.press('enter')
    time.sleep(1)

def abrirWhatsapp():
     open('whatsapp')


if __name__ == "__main__":
     #abrir_notepad()       
     #abrir_paint()                                                                         
     #tomar_captura()
     #buscar_en_google()             
     
     reproducir_youtube()
     #abrirSpotify()
     #abrirWhatsapp()