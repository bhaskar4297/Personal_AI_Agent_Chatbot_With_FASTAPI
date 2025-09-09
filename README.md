# 🤖 Personal Agentic AI Chatbot  
**GenAI Application (Production Ready)**  

LangGraph | FastAPI | Streamlit | Groq | DeepSeek |LangChain  

---

## 📌 Project Overview  

This project is a **Personal Agentic AI Chatbot** that enables users to interact with different **LLM providers** (DeepSeek, Groq models with extendable support for Llama/Mistral) through a unified interface.  

Unlike ChatGPT, which is tied to a single provider, this chatbot is **provider-agnostic, customizable, and tool-augmented**, making it ideal for **AI experimentation, prototyping and practical AI applications**.  

---

## 🎯 Purpose of the Project  

While tools like **ChatGPT** already exist, they are tied to a **single provider** (OpenAI) and lack flexibility.  
This project was built to:  

- ✅ Allow **switching between different models/providers** at runtime  
- ✅ Enable developers and users to **customize the chatbot’s behavior** with system prompts  
- ✅ Integrate **real-time knowledge** via Tavily search, Wikipedia, and live Weather API  
- ✅ Support **reasoning and calculations** with a Python REPL tool  
- ✅ Serve as a **production-ready template** for building GenAI applications with a modular **backend + frontend**  

**Use Cases:**  
- AI experimentation & research → compare outputs across models  
- Prototyping business-specific assistants → customer support, research, knowledge management  
- Education → learning FastAPI, LangGraph, LangChain orchestration  
- Internal company tools → flexible assistants with custom providers and tools  

---

## 🚀 What it Demonstrates  

- **Customizable prompts** → define chatbot personality/behavior  
- **Multi-provider support** → Groq (extendable to OpenAI, Llama, Mistral)  
- **Tool integrations** → Tavily search, Wikipedia lookup, Weather info, Calculator  
- **Backend APIs** → FastAPI + Pydantic validation  
- **Frontend UI** → Streamlit for non-technical users  
- **Swagger UI** → auto-generated API docs at `/docs`  

Unlike ChatGPT, this app is **provider-agnostic, tool-augmented and extensible**, making it ideal for **AI experimentation, prototyping and internal tools**.  

---

## 🏗️ Project Layout  

# 🚀 Project Setup Guide: Personal Agentic AI Chatbot  

This guide provides step-by-step instructions to set up your environment and run the project.  
It supports multiple options for virtual environments (**Pipenv, pip+venv, Conda**).  

---

### **Phase 1 – AI Agent**  
1. Setup API Keys for Groq, Tavily  
2. Configure LLMs & Tools (Calculator, Wikipedia, Weather, Tavily)  
3. Build AI Agent with optional tool-augmented responses  

---

### **Phase 2 – Backend (FastAPI)**  
1. Define request schema with Pydantic  
2. Build `/chat` API endpoint for frontend ↔ backend communication  
3. Run app & explore **Swagger UI Docs** at `/docs`  

---

### **Phase 3 – Frontend (Streamlit)**  
1. Build UI (provider, model, system prompt, query input)  
2. Connect frontend to backend via REST API  

---

## 🛠️ Tools & Technologies  

- **LangGraph** → ReAct agent orchestration  
- **LangChain** → Integrations (Tavily, Wikipedia, Weather, Calculator)  
- **FastAPI** → Backend APIs & Swagger docs  
- **Streamlit** → Frontend web app  
- **Groq** → LLM provider (free & fast)  
- **Pydantic** → Request schema validation  
- **Uvicorn** → ASGI server  
- **Python** → Core programming language  

---

## 🐳 Deployment with Docker

To make this chatbot easy to run anywhere, I containerized both the **backend (FastAPI)** and **frontend (Streamlit)** into Docker images.  
This means anyone can launch the app with a few commands—no need to install Python or dependencies manually.  

## ⚙️ CI/CD with GitHub Actions

This repo is integrated with GitHub Actions for continuous integration & deployment.

On every push to main, GitHub automatically:

Builds fresh Docker images for backend & frontend.

Tags them as latest and with the short commit SHA.

Pushes them to Docker Hub → dockerhub.com/u/bhaskar4297
.
---

### 🚀 Run with Docker Compose (recommended)

1. **Clone the repo**
   ```bash
   git clone https://github.com/bhaskar4297/Personal_AI_Agent_Chatbot_With_FASTAPI.git
   cd C:\Users\sinha\OneDrive\Documents\Agentic AI fast API\Deploy_with_docker

   **Create .env file (do NOT commit .env)**
   ```bash
   cp .env.example .env

   **Open .env and paste your keys:**
   **Start both backend + frontend**
   docker compose up -d

   **Access in browser**

   Backend API → http://localhost:9999/docs

   Frontend UI → http://localhost:8501
