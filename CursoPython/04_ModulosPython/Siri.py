import pyttsx3  # Importa la biblioteca para convertir texto a voz
from MO4D4PY.api import API  # Importa la clase API de MO4D4PY
from MO4D4PY.exceptions import APIError  # Importa la excepción APIError

# Inicializa el motor de texto a voz y la API una vez
engine = pyttsx3.init()
api_key = '7b561ca48ffb14079256817934f51ebf2b265bb0ddec1c8bba5590b4f9e3412a'
api = API(api_key, '')

def get_response_from_api(prompt):
    try:
        response = api.request('CodeAssist', payload={'prompt': prompt}, timeout=10)
        return response.get('response')
    except (APIError, TimeoutError) as e:
        return f"Se produjo un error: {e}"

def speak_and_display_response():
    while True:
        # Solicita al usuario que ingrese un texto
        user_input = input("Escribe tu pregunta: ")
        print("Tu pregunta: ", user_input)
        
        # Obtiene la respuesta de la API
        response_text = get_response_from_api(user_input)
        
        # Muestra la respuesta en pantalla y la dice en voz alta
        print("Respuesta de la IA: ", response_text)
        engine.say(response_text)
        engine.runAndWait()
        
        # Pregunta si el usuario quiere saber algo más
        more_input = input("¿Quieres saber algo más? (sí/no): ").strip().lower()
        if more_input != 'sí':
            print("Proceso finalizado.")
            break

# Llama a la función
speak_and_display_response()