import time
import asyncio
from Scripts.Chat_Reader import read_chat_youtube,read_chat_twitch
from Scripts.TTS_Engine import init_tts
from Scripts.Config_Loader import load_config

def main():
    load_config()
    init_tts()
    print("\n\nRunning!\n\n")
    while True:
        read_chat_youtube()
        # asyncio.run(read_chat_twitch())  # Uncomment if needed
        print("\n\nReset!\n\n")
        time.sleep(2)

if __name__ == "__main__":
    main()
