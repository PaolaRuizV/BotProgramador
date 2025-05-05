import subprocess
import pyautogui
import time
import webbrowser
import types
from AppOpener import open

# La clase para contener las acciones que puede realizar el bot
class Accion:
    def __init__(self, nombre_: str, descripcion_: str, funcion_: types.FunctionType):
        self.nombre = nombre_           # Esto es el nombre de la accion
        self.descripcion = descripcion_ # Esto explica de que se trata esta accion
        self.funcion = funcion_         # Esto es la funcion que va ejecutar la accion
        pass

def abrir_notepad():
    subprocess.Popen(['notepad.exe'])
    time.sleep(0.5)  # Espera a que se abra
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

    # pyautogui.write('Hola mundo', interval=0.1)
    # pyautogui.press('enter')
    # time.sleep(5)

    # pyautogui.moveTo(350, 350)
    # pyautogui.click()

    #pyautogui.press('tab', presses=4, interval=0.3)  # Ir al primer video
    #pyautogui.press('enter')  # Reproducir


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


LISTA_ACCIONES = [
    Accion(
        nombre_= "Abrir Notepad",
        descripcion_= "Abre la aplicacion Notepad o Bloc de Notas de Windows",
        funcion_= abrir_notepad
    ),
    Accion(
        nombre_="Abrir Paint",
        descripcion_="Abre Microsoft Paint y dibuja un cuadrado automáticamente",
        funcion_=abrir_paint
    ),
    Accion(
        nombre_="Tomar captura de pantalla",
        descripcion_="Realiza una captura de pantalla y la guarda como 'captura_pantalla.png'",
        funcion_=tomar_captura
    ),
    Accion(
        nombre_="Buscar en Google",
        descripcion_="Abre Google en el navegador y busca 'Cae zoom a nivel mundial'",
        funcion_=buscar_en_google
    ),
    Accion(
        nombre_="Abrir YouTube",
        descripcion_="Abre YouTube en el navegador y se posiciona en el buscador",
        funcion_=reproducir_youtube
    ),
    Accion(
        nombre_="Abrir Spotify",
        descripcion_="Abre Spotify y reproduce música automáticamente",
        funcion_=abrirSpotify
    ),
    Accion(
        nombre_="Pasar canción en Spotify",
        descripcion_="Pasa a la siguiente canción en Spotify",
        funcion_=pasarDeCancionSpotify
    ),
    Accion(
        nombre_="Retroceder canción en Spotify",
        descripcion_="Regresa a la canción anterior en Spotify",
        funcion_=retrocederCancionSpotify
    ),
    Accion(
        nombre_="Abrir WhatsApp",
        descripcion_="Abre la aplicación de WhatsApp",
        funcion_=abrirWhatsapp
    )
    # Agregar mas funciones

]

ACCION_ERROR = Accion(
        nombre_ = "Error al entender",
        descripcion_ = "Esta funcion se ejecuta cuando no se ha entendido el prompt que dijo el usuario",
        funcion_ = lambda: print("No entendi lo que me pediste")
    )




if __name__ == "__main__":
     #abrir_notepad()       
     #abrir_paint()                                                                         
     #tomar_captura()
     #buscar_en_google()             
     
     reproducir_youtube()
     #abrirSpotify()
     #abrirWhatsapp()