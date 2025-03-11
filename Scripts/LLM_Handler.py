import groq
import ollama
from openai import OpenAI
from Scripts.Config_Loader import GROQ, OLLAMA,OPENROUTER

user_chat_history = {}

def llm_groq(username, message):
    global user_chat_history
    client = groq.Client(api_key=GROQ.key)
    if username not in user_chat_history:
        user_chat_history[username] = []
    user_chat_history[username].append({"role": "user", "content": message})
    if len(user_chat_history[username]) > 5:
        user_chat_history[username].pop(0)
    messages = [{"role": "system", "content": GROQ.prompt}] + user_chat_history[username]
    response = client.chat.completions.create(
        model=GROQ.model,
        messages=messages,
        temperature=GROQ.temperature,
        max_completion_tokens=GROQ.max_tokens,
        top_p=GROQ.top_p,
        frequency_penalty=GROQ.frequency_penalty,
        presence_penalty=GROQ.presence_penalty,
        stream=True
    )
    response_text = ""
    for chunk in response:
        if chunk.choices and chunk.choices[0].delta.content:
            response_text += chunk.choices[0].delta.content

    user_chat_history[username].append({"role": "assistant", "content": response_text})
    return response_text

def llm_ollama(username, message):
    global user_chat_history
    if username not in user_chat_history:
        user_chat_history[username] = []
    user_chat_history[username].append({"role": "user", "content": message})
    if len(user_chat_history[username]) > 5:
        user_chat_history[username].pop(0)
    messages = [{"role": "system", "content": OLLAMA.prompt}] + user_chat_history[username]
    response = ollama.chat(
        model=OLLAMA.model,
        messages=messages,
        options={
            "temperature": OLLAMA.temperature,
            "max_tokens": OLLAMA.max_tokens,
            "top_p": OLLAMA.top_p,
            "frequency_penalty": OLLAMA.frequency_penalty,
            "presence_penalty": OLLAMA.presence_penalty
        }
    )
    return response["message"]["content"]

def llm_openrouter(username, message):
    global user_chat_history
    if username not in user_chat_history:
        user_chat_history[username] = []
    user_chat_history[username].append({"role": "user", "content": message})
    if len(user_chat_history[username]) > 5:
        user_chat_history[username].pop(0)

    messages = [{"role": "system", "content": OPENROUTER.prompt}] + user_chat_history[username]

    # Create a new OpenAI client
    client = OpenAI(
        api_key=OPENROUTER.key,
        base_url="https://openrouter.ai/api/v1"  # Ensure this is correct for OpenRouter
    )

    response = client.chat.completions.create(
        model=OPENROUTER.model,  # Example: "gpt-4"
        messages=messages,
        temperature=OPENROUTER.temperature,
        max_tokens=OPENROUTER.max_tokens,
        top_p=OPENROUTER.top_p,
        frequency_penalty=OPENROUTER.frequency_penalty,
        presence_penalty=OPENROUTER.presence_penalty
    )

    response_text = response.choices[0].message.content
    user_chat_history[username].append({"role": "assistant", "content": response_text})
    return response_text
