# ChatConIA 🤖🔊

**ChatConIA** es una librería en Python diseñada para facilitar la interacción con modelos de lenguaje de última generación (**Gemini 2.5 Flash**) mediante el uso de gramáticas personalizadas y síntesis de voz en tiempo real.

## ✨ Características principales

- **Interpretación de Gramática:** Procesa comandos mediante el formato `INSTRUCCION : Texto`.
- **Inteligencia Artificial:** Integración directa con la API de Google Generative AI.
- **Respuesta por Voz:** Implementación de Text-to-Speech (TTS) con hilos (`threading`) para evitar el bloqueo de la ejecución.
- **Estandarización:** Limpieza automática de datos (espacios y mayúsculas) para mayor robustez.

## 🚀 Instalación

Asegúrate de tener instaladas las dependencias necesarias:

```bash
pip install google-generativeai pyttsx3 SpeechRecognition PyAudio Pillow
