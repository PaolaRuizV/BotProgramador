# BotProgramador

*Que es*

Este es un asistente de voz simple desarrollado en Python que reconoce comandos hablados y ejecuta acciones específicas, como abrir Google o YouTube, entre otros. Utiliza la API de Google Speech Recognition para transcribir audio en tiempo real.


*Cómo funciona*

Cómo funciona

El programa lo que hace es poder interactuar con programas que normalmente recurrimos, pero a traves de instrucciones por comando de voz, este lo transcribe y se pasa por una IA para que limpie la instrucción y ejecute la función o acción que desea el usuario.
1. El programa escucha continuamente a través del micrófono.
2. Cuando identifica una palabra clave en el audio (por ejemplo, "Google" o "YouTube"), llama a una función que realiza una acción específica.


Descripción de funcionalidades
    Abrir youtube
    Abrir google
    Interacción con Spotify -> Abre la app de Spotify y ayuda a poder retroceder, pausar , reproducir o avanzar de canción.
    fnaiksf
    fasf


Motivación (por qué se hizo)git

Este proyecto nació de manera espontánea entre un grupo de compañeros de la universidad, simplemente con las ganas de crear algo divertido.
Nuestra idea era construir un pequeño asistente por comando de voz que no solo se limitara a responder preguntas, sino que también pudiera 
interactuar con programas y navegadores, haciendo más fácil algunas tareas del día a día.
Más allá del resultado final, el proyecto fue una oportunidad para aprender, experimentar y sobre todo, disfrutar del proceso de trabajar en equipo y llevar una idea desde cero hasta verla funcionando.
*Motivación (por qué se hizo)*

La motivación principal de este proyecto fue explorar el uso de reconocimiento de voz en automatización de tareas diarias.
Además, sirve como base para proyectos más grandes como asistentes personales, bots o sistemas de accesibilidad.


\
\
\
!! Consumimos de este LLM en HuggingFace para hacer lo de la comparacion de oraciones


## Anotaciones para la ejecución
* Es necesario crearse una cuenta de HuggingFace y crear un TOKEN read \
el token debe ser colocarse en un archivo .env (existe el archivo example.env de referencia)

* El LLM que utiliza el bot no puede recibir oraciones demasiado largas, ademas que realiza una comparacion de semantica entre el prompt y la descripcion de la funcion, por ende > oraciones muy largas o muy complejas puede que no las interprete correctamente

* El bot, siempre va elegir la funcionalidad con mayor similitud a lo que solicitas. Se puede definir un minimo valor de aceptacion al ejecutar la funcion de ```buscar_funcion_correspondiente()```
