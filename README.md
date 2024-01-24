# MathGPT
![image](https://github.com/javi22020/MathGPT/assets/90896750/5dcfeac0-5eff-4c65-8aaa-9849a837d47e)

## Resumen
MathGPT es un chatbot que emplea GPT-3.5-Turbo (opcionalmente GPT-4-Turbo y en el futuro modelos de lenguaje locales) y programación en Python para devolver respuestas a problemas matemáticos relativamente simples.
## Características y objetivos
✅ Cálculo real de problemas
❌ Devolución de los pasos intermedios
❌ Inferencia mediante modelos locales
## Instalación
Para instalarlo, necesitarás tener:
- Python > 3.10 (recuerda marcar la casilla "Añadir al PATH" durante la instalación)
- Las dependencias indicadas en `requirements.txt`, puedes instalarlas con el siguiente comando:
```bash
pip install -r requirements.txt
```
- Actualmente, es necesaria una clave de API de OpenAI para poder usar el modelo de lenguaje (aunque esto puede cambiar con la implementación de modelos de código abierto), y añadirla al PATH con el comando:
```bash
setx OPENAI_API_KEY "TU-CLAVE-AQUÍ"
```
- Por ejemplo:
```bash
setx OPENAI_API_KEY "sk-..."
```
## Problemas y mejoras
Para preguntar sobre problemas o contribuir al proyecto con ideas o código, ve a la pestaña "Issues" dentro de este repositorio.
