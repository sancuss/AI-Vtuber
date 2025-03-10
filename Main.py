import time
import asyncio
from Chat_reader import read_chat_youtube, read_chat_twitch
from tts_engine import init_tts

def main():
    init_tts()
    print("\n\nRunning!\n\n")
    while True:
        read_chat_youtube()
        # asyncio.run(read_chat_twitch())  # Uncomment if needed
        print("\n\nReset!\n\n")
        time.sleep(2)

if __name__ == "__main__":
    main()
