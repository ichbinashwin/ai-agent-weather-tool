# agent.py (no deprecation)

import os
import re
import logging
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from tools.weather_tool import get_weather
from tools.common_tool import is_running_in_docker

# Load env
load_dotenv()

# === Enable DEBUG mode if DEBUG=1 in .env ===
if os.getenv("DEBUG") == "1":
    # Logging setup
    logging.basicConfig(level=logging.DEBUG)
    logging.getLogger("httpx").setLevel(logging.DEBUG)
    logging.getLogger("langchain").setLevel(logging.DEBUG)
    logging.getLogger("langchain_ollama").setLevel(logging.DEBUG)

#os.environ["OLLAMA_HOST"] = "http://localhost:11434"

# Dynamically set OLLAMA_HOST
if is_running_in_docker():
    os.environ["OLLAMA_HOST"] = "http://host.docker.internal:11434"
    os.environ["OLLAMA_HOST"] = "http://localhost:11434"
else:
    os.environ["OLLAMA_HOST"] = "http://localhost:11434"

# LLM setup
llm = ChatOllama(model="openhermes", timeout=30)

# Prompt
template = """
You are a helpful assistant that can access weather information.
You are a strict weather assistant.
You are ONLY allowed to respond using the 'get_weather' tool.
If a user asks anything not related to weather, respond: 
'I can only help with weather-related questions.'

If the user asks for the weather, respond ONLY like this:
CALL get_weather(city="CityName")

Otherwise, answer normally.

User: {input}
Assistant:"""

prompt = PromptTemplate.from_template(template)

# New: Runnable sequence instead of deprecated LLMChain
chain = prompt | llm

def run():
    print("🌦️ Weather AI Agent is running with Ollama. Type 'exit' to quit.\nTry: What's the weather in Berlin?")
    while True:
        query = input("You: ")
        if query.lower() in ("exit", "quit"):
            print("👋 Goodbye!")
            break

        try:
            print("⚙️ Sending prompt to Ollama...")
            llm_output = chain.invoke({"input": query})
            print("✅ Response received.")
            print(f"\n🔍 Raw Output:\n{llm_output.content}\n")

            match = re.search(r'CALL get_weather\(city="(.*?)"\)', llm_output.content)
            if match:
                city = match.group(1)
                result = get_weather(city)
                print(f"🌤️ {result}\n")
            else:
                print(f"🧠 {llm_output.content}\n")

        except Exception as e:
            print(f"❌ Error during LLM call: {e}")

if __name__ == "__main__":
    run()

