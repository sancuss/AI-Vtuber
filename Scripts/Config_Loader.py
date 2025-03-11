import json

def load_config():
    try:
        with open("Configs/config.json", "r") as json_file:
            data = json.load(json_file)
        return data
    except Exception as e:
        print(f"Error loading config: {e}")
        exit()

data = load_config()

# Define configuration classes
class TWITCH:
    TWITCH_WS_URL = data["Twitch"][0]["twitch_ws_url"]
    OAUTH_TOKEN = data["Twitch"][0]["oauth_token"]
    USER = data["Twitch"][0]["user"]
    CHANNEL = data["Twitch"][0]["channel"]

class YOUTUBE:
    VIDEO_ID = data["YouTube"][0]["video_id"]

class OAI:
    key = data["keys"][0]["OAI_key"]
    model = data["OAI_data"][0]["model"]
    prompt = data["OAI_data"][0]["prompt"]
    temperature = data["OAI_data"][0]["temperature"]
    max_tokens = data["OAI_data"][0]["max_tokens"]
    top_p = data["OAI_data"][0]["top_p"]
    frequency_penalty = data["OAI_data"][0]["frequency_penalty"]
    presence_penalty = data["OAI_data"][0]["presence_penalty"]

class EL:
    key = data["keys"][0]["EL_key"]
    voice = data["EL_data"][0]["voice"]

class GROQ:
    key = data["keys"][0]["GROQ_key"]
    model = data["GROQ_data"][0]["model"]
    prompt = data["GROQ_data"][0]["prompt"]
    temperature = data["GROQ_data"][0]["temperature"]
    max_tokens = data["GROQ_data"][0]["max_tokens"]
    top_p = data["GROQ_data"][0]["top_p"]
    frequency_penalty = data["GROQ_data"][0]["frequency_penalty"]
    presence_penalty = data["GROQ_data"][0]["presence_penalty"]

class OLLAMA:
    model = data["Ollama_data"][0]["model"]
    prompt = data["Ollama_data"][0]["prompt"]
    temperature = data["Ollama_data"][0]["temperature"]
    max_tokens = data["Ollama_data"][0]["max_tokens"]
    top_p = data["Ollama_data"][0]["top_p"]
    frequency_penalty = data["Ollama_data"][0]["frequency_penalty"]
    presence_penalty = data["Ollama_data"][0]["presence_penalty"]

class OPENROUTER:
    key = data["keys"][0]["OPENROUTER_key"]
    model = data["OPENROUTER_data"][0]["model"]
    prompt = data["OPENROUTER_data"][0]["prompt"]
    temperature = data["OPENROUTER_data"][0]["temperature"]
    max_tokens = data["OPENROUTER_data"][0]["max_tokens"]
    top_p = data["OPENROUTER_data"][0]["top_p"]
    frequency_penalty = data["OPENROUTER_data"][0]["frequency_penalty"]
    presence_penalty = data["OPENROUTER_data"][0]["presence_penalty"]
