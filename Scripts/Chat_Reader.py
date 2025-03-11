import pytchat
import time
import websockets
import asyncio
import re
from Scripts.Config_Loader import YOUTUBE, TWITCH
from Scripts.TTS_Engine import tts_controller
from Scripts.LLM_Handler import llm_groq,llm_openrouter

def remove_asterisk_text(text):
    return re.sub(r'\*.*?\*|\(.*?\)', '', text)

def read_chat_youtube():
    chat = pytchat.create(video_id=YOUTUBE.VIDEO_ID)
    while chat.is_alive():
        for c in chat.get().sync_items():
            print(f"\n{c.datetime} [{c.author.name}]- {c.message}\n")
            response = llm_groq(c.author.name, c.message)
            #response = llm_openrouter(c.author.name, c.message)
            clean_text = remove_asterisk_text(response)

            print(c.author.name + " " + response)
            tts_controller(c.author.name + " " + clean_text,"melotts")
            time.sleep(1)

async def read_chat_twitch():
    async with websockets.connect(TWITCH.TWITCH_WS_URL) as websocket:
        await websocket.send(f"PASS {TWITCH.OAUTH_TOKEN}")
        await websocket.send(f"NICK {TWITCH.USER}")
        await websocket.send(f"JOIN #{TWITCH.CHANNEL}")
        print(f"Connected to Twitch chat: #{TWITCH.CHANNEL}")
        while True:
            try:
                message = await websocket.recv()
                match = re.search(r":(\w+)!\w+@\w+\.tmi\.twitch\.tv PRIVMSG #\w+ :(.+)", message)
                if match:
                    username = match.group(1)
                    chat_message = match.group(2)
                    print(f"\n{username}: {chat_message}\n")
                    response = llm_groq(username, chat_message)
                    print(f"\nAI Response: {username + ' ' + response}")
                    tts_controller(username + " " + response,"melotts")
                    time.sleep(1)
            except websockets.exceptions.ConnectionClosed:
                print("Disconnected, reconnecting...")
                break
