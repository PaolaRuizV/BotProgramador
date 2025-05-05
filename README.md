# Proyecto BotProgramador

## Qué es

Este es un asistente de voz simple desarrollado en Python que reconoce comandos hablados y ejecuta acciones específicas como:
* Abrir Aplicaciones de escritorio: Spotify, Bloc de Notas, VSCode, WhatsApp, Paint
* Interacción con Spotify -> Abre la app de Spotify y ayuda a poder retroceder, pausar , reproducir o avanzar de canción.
* Abrir sitios web (Google, Youtube, )
* Hacer captura de pantalla

Para la parte de Speech Recognition, transcribir audio en tiempo real, utiliza la API de Google Speech Recognition por defecto. Es posible cambiar este modelo al de OpenAI-Whisper cambiando la variable ```RECOGNIZER```

## Cómo funciona
El programa lo que hace es escuchar continuamente a través del micrófono, este lo transcribe por medio de una API de SpeechRecognition de Google, luego se pasa por un modelo de similitud semántica en HuggingFace para elegir la acción con mejor similitud a la frase que pide el usuario, finalmente se ejecuta la función relacionada a dicha accion.

<br>

El modelo de similitud usado se encuentra en el siguiente enlace:
https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2

<br>


El bot consume de la lista ```LISTA_ACCIONES```, definida en el archivo funciones.py. Cada operación posible por el bot están contenidas en una "Accion".
* Nombre: es el nombre de la accion
* Descripcion: explicación de la acción que será enviada al modelo
* Funcion: Esta es la funcion de python que se va ejecutar
Se puede añadir acciones nuevas a dicha lista para aumentar el alcance del bot.

EL bot solo reacciona a los comandos que incluyan la palabra "computadora".  




## Motivación
Este proyecto nació de manera espontánea entre un grupo de compañeros de la universidad, simplemente con las ganas de crear algo divertido.
Nuestra idea era construir un pequeño asistente por comando de voz que pudiera interactuar con programas y navegadores, haciendo más fácil algunas tareas del día a día. La idea era explorar el uso de reconocimiento de voz en automatización de tareas diarias.

Más allá del resultado final, el proyecto fue una oportunidad para aprender, experimentar y sobre todo, disfrutar del proceso de trabajar en equipo y llevar una idea desde cero hasta verla funcionando.

Además, sirve como base para proyectos más grandes como asistentes personales, bots o sistemas de accesibilidad.


## Anotaciones para la ejecución
* Es necesario crearse una cuenta de HuggingFace y crear un TOKEN read \
el token debe ser colocarse en un archivo .env (existe el archivo example.env de referencia)

* El LLM que utiliza el bot no puede recibir oraciones demasiado largas, ademas que realiza una comparacion de semantica entre el prompt y la descripcion de la funcion, por ende -> oraciones muy largas o muy complejas puede que no las interprete correctamente

* El bot, siempre va elegir la funcionalidad con mayor similitud a lo que solicitas. Se puede definir un minimo valor de aceptacion al ejecutar la funcion de ```buscar_funcion_correspondiente()``` modificando el argumento ```threshold```.

Participantes:
* Dennis Andre Ceballos Manrique
* Paola Rosmery Ruiz Victorio
<br>
<br>
<br>
Este proyecto fue promovido por la IniciativaPMP