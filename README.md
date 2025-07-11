# 🌦️ Weather Tool API with AI Agent (Ollama + LangChain)

---

## 📖 Overview

This project demonstrates building an AI-powered Weather Tool API that integrates:

- **Artificial Intelligence (AI)**: Machines simulating human intelligence tasks like understanding language and reasoning.

- **AI Agent**: A specialized AI system that performs tasks autonomously by processing inputs, invoking tools, and generating outputs. Here, the AI agent processes user queries about weather and calls the weather tool to fetch live data.

- **LangChain**: A Python framework that simplifies building AI applications by connecting Large Language Models (LLMs) with other components like prompts, tools, memory, and agents.

- **LangChain Tools**: Modular pieces of functionality (e.g., Weather API, BMI calculator) that agents can invoke based on user requests to fetch data or perform calculations.

- **Architecture**: This project runs an AI agent powered by Ollama (a local LLM host) connected with LangChain tooling and a REST API for external interaction.

---

## 🚀 Prerequisites

### Hardware & OS
- Linux or macOS recommended (Docker runs best here; Windows WSL2 also possible)
- Minimum 8GB RAM recommended

### Software

- **Docker**  
  Install Docker Engine and Docker Compose  
  [Docker Installation Guide](https://docs.docker.com/get-docker/)

- **Ollama** (Local LLM Host)  
  - Download and install Ollama from [https://ollama.com/](https://ollama.com/)  
  - Pull required models like `openhermes`, `llama3`  
    ```bash
    ollama pull openhermes
    ollama pull llama3
    ```  
  - Run Ollama server locally:  
    ```bash
    ollama serve
    ```

- **Python 3.10+**  
  - Create virtual environment  
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```  
  - Install dependencies:  
    ```bash
    pip install -r requirements.txt
    ```

- **OpenWeatherMap API Key**  
  - Sign up at [https://openweathermap.org/api](https://openweathermap.org/api)  
  - Get your free API key and set it in `.env`

---

## 📂 Project Structure
```
weather-tool-ai-agent/
├── api.py # FastAPI main application file
├── tools/
│ └── weather_tool.py # Weather Tool implementation calling OpenWeatherMap API
├── agent.py # AI Agent setup with LangChain and Ollama
├── Dockerfile # Dockerfile for containerizing the API
├── build.sh # Script to build the Docker image
├── requirements.txt # Python dependencies
├── .env # Environment variables (API keys, configs)
└── README.md # This file
```
---

---

## 🏗️ How It Works

1. **User sends a query** to the FastAPI REST endpoint (e.g., "What's the weather in London?")

2. The API can optionally forward this to an **AI Agent** built with LangChain, which:
   - Interprets the query using an LLM (like `openhermes` from Ollama)
   - Identifies which tool to call (e.g., Weather Tool)
   - Calls the tool with required inputs (city name)

3. The **tool fetches live data** from the OpenWeatherMap API

4. The AI agent processes the result, **generates a natural language response**, and returns it

5. The REST API sends the response back to the user

---

## 🔧 Components

| Component       | Description                                                                                              |
|-----------------|----------------------------------------------------------------------------------------------------------|
| **Ollama**      | A local LLM host running AI models like `llama3`, `openhermes`, etc., without cloud dependency            |
| **LangChain**   | Framework to build chains, agents, tools, and manage prompt logic connecting LLMs with external APIs      |
| **FastAPI**     | Python web framework serving the API endpoints                                                           |
| **Weather Tool**| A custom LangChain Tool that fetches weather info from OpenWeatherMap API                                |
| **Agent**       | LangChain Agent using Ollama LLM and invoking tools based on user query                                  |
| **Docker**      | Containerization for easy deployment and environment consistency                                         |

---

## 🏛️ AI Agent Architecture
```
┌────────────┐      ┌───────────────┐       ┌─────────────┐
│ User Query ├────▶│ FastAPI REST  ├──────▶│ LangChain   │
│ (HTTP API) │      │ API Endpoint  │       │ Agent       │
└────────────┘      └───────────────┘       │             │
                                            │  Ollama LLM │
                                            │             │
                                            └──────┬──────┘
                                                   │ Calls tools
                         ┌─────────────────────────┴─────────────────────────┐
                         │                                                   │
             ┌───────────────────┐                         ┌─────────────────────────┐
             │ Weather Tool API  │                         │ Other Tools (BMI, etc.) │
             └───────────────────┘                         └─────────────────────────┘
```

---

## 🛠️ LangChain Tools Explained

- Tools in LangChain are self-contained units of functionality an AI agent can invoke.

- Example: `weather_tool` queries OpenWeatherMap for weather data.

- AI Agents decide which tool to call based on user input context.

- Tools make AI agents *extensible* and *safe*, restricting actions to predefined capabilities.

---

## 🔒 Why Use Ollama?

- Ollama runs LLM models locally, no data sent to third-party cloud.

- Ensures **privacy, security**, and offline capability.

- Supports models like `llama3`, `openhermes`, `mistral`.

- LangChain integrates with Ollama easily using `langchain_ollama`.

---

## 🎯 Benefits of This Architecture

- **Modular**: Easily add new tools (BMI calculator, Microbiome tool) without changing core AI logic

- **Secure**: Limit tool access to only approved APIs

- **Flexible**: Swap AI models or tooling with minimal code changes

- **Local-first**: No dependency on expensive or privacy-sensitive cloud LLM services

---

## ⚙️ Running Locally

1. Clone the repo:
    ```bash
    git clone https://github.com/yourusername/weather-tool-ai-agent.git
    cd weather-tool-ai-agent
    ```

2. Create and activate Python virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up `.env` file with:
    ```
    OPENWEATHER_API_KEY=your_openweathermap_api_key_here
    ```

5. Start Ollama server (in separate terminal):
    ```bash
    ollama serve
    ```

6. Run the FastAPI server:
    ```bash
    uvicorn api:app --reload
    ```

7. Open your browser at [http://localhost:8000/docs](http://localhost:8000/docs) to see Swagger UI.

---

## 🐳 Using Docker

1. Build the Docker image:
    ```bash
    ./build.sh
    ```

2. Run the container (make sure `.env` is configured):
    ```bash
    docker run --env-file .env -p 8000:8000 weather-tool-ai-agent:latest
    ```

3. Access API at [http://localhost:8000](http://localhost:8000)

---

## 🔜 Next Steps

- Add new LangChain tools and register with the AI agent

- Implement API key management and authentication layers

- Extend REST API to expose AI agent conversational interface

- Add persistent memory for agent context and session management

---

## 🙏 Acknowledgments

- [Ollama](https://ollama.com/) for local LLM hosting

- [LangChain](https://langchain.com/) for the AI framework

- [FastAPI](https://fastapi.tiangolo.com/) for the API server

- [OpenWeatherMap](https://openweathermap.org/api) for weather data

---

## 📄 License

MIT License

---

*Feel free to contribute or raise issues!*

