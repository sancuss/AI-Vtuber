import pyttsx3
import os
import subprocess
import time
from gradio_client import Client

gr_client = Client("http://localhost:8888/")

def init_tts():
    global engine

    engine = pyttsx3.init()
    engine.setProperty('rate', 180)
    engine.setProperty('volume', 1)
    voice = engine.getProperty('voices')
    engine.setProperty('voice', voice[1].id)

def tts_controller(message, tts_type="pyttsx3"):
    if tts_type == "pyttsx3":
        pyttsx3_tts(message)
    elif tts_type == "melotts":
        melotts_tts(message)

def pyttsx3_tts(message):
    engine.say(message)
    engine.runAndWait()

def melotts_tts(message):
    result = gr_client.predict(
        text=message,
        speaker="EN-US",
        speed=1,
        language="EN",
        api_name="/synthesize"
    )
    
    if os.path.exists(result):
        try:
            temp_audio_path = result + "_converted.mp3"
            subprocess.run(["ffmpeg", "-y", "-i", result, "-ar", "22050", "-ac", "2", "-b:a", "192k", temp_audio_path], check=True)
            subprocess.run(["ffplay", "-nodisp", "-autoexit", temp_audio_path])
        except Exception as e:
            print(f"Error playing local audio file: {e}")
        finally:
            time.sleep(10)
            os.remove(result)
            os.remove(temp_audio_path)
