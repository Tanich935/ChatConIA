import google.generativeai as genai
import pyttsx3

class Procesador:
    def __init__(self):
        self.model = None
        self.chat_session = None
        self.tts = pyttsx3.init()
        self.tts.setProperty('rate', 150)
        self.activarTTS = False 

    def darApiKey(self, apikey):
        genai.configure(api_key=apikey)
        self.model = genai.GenerativeModel(model_name="gemini-2.5-flash") 
        self.chat_session = self.model.start_chat()

    def activarVoz(self):
        self.activarTTS = True
        
    def desactivarVoz(self):
        self.activarTTS = False

    def _interpretar_gramatica(self, texto):
        if ":" not in texto:
            return None, None
        
        instruccionesDivididas = texto.split(":", 1) 
        instruccion = instruccionesDivididas[0].strip().upper() 
        texto = instruccionesDivididas[1].strip()       
        return instruccion, texto

    def enviarMensaje(self, texto):
        if self.chat_session is None:
            return "La API KEY no esta establecida."

        instruccion, texto = self._interpretar_gramatica(texto)

        if instruccion is None:
            return "Porfavor usa correctamente el formato -> 'INSTRUCCION : Texto'"

        promptFinal = "Tu instruccion es: " + instruccion + " ,el siguiente texto de forma clara y directa, sin hacer ningun saludo: " + texto
        
        respuesta = self.chat_session.send_message(promptFinal)
        respuestaFinal = respuesta.text

        if self.activarTTS == True:
            self.tts.say(respuestaFinal)
            self.tts.runAndWait()

        return respuestaFinal