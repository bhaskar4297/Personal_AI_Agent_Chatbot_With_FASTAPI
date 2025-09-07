# 🤖 Personal Agentic AI Chatbot  
**GenAI Application (Production Ready)**  

LangGraph | FastAPI | Streamlit | OpenAI | Groq | Meta Llama | Mistral  

---

## 📌 Project Overview

This project is a **Personal Agentic AI Chatbot** that enables users to interact with different **LLM providers** (OpenAI, Groq, Llama, Mistral) through a unified interface.  

### 🎯 Purpose of the Project
While tools like **ChatGPT** already exist, they are limited to a single provider (OpenAI) and lack flexibility.  
This project was built to:  
- Allow **switching between multiple providers/models** (OpenAI, Groq, Llama, Mistral) at runtime.  
- Give developers and users the ability to **customize the chatbot’s behavior** with system prompts.  
- Integrate **web search** (via Tavily) to provide real-time, up-to-date knowledge beyond the model’s training data.  
- Serve as a **production-ready template** for building custom GenAI applications with a modular **backend + frontend** design.  

This makes the chatbot especially useful for:  
- **AI experimentation & research** (comparing model outputs across providers).  
- **Prototyping business-specific assistants** (customer support, research, knowledge management).  
- **Educational purposes** (learning FastAPI, LangGraph, and agent orchestration).  
- **Internal company tools** where flexibility and provider choice are important.  

### 🚀 What it demonstrates
It shows how to design, build, and run a **full-stack AI agent** with:  
- **Customizable prompts** (define chatbot personality/behavior)  
- **Multi-provider support** (choose model at runtime)  
- **Optional web search** (real-time knowledge via Tavily)  
- **Backend APIs** with validation (FastAPI + Pydantic)  
- **Frontend UI** for non-technical users (Streamlit)  

Unlike ChatGPT, this app is **provider-agnostic, customizable, and extensible**, making it ideal for **AI experimentation, prototyping, and internal tools**.  

---

## 🏗️ Project Layout
# 🚀 Project Setup Guide: Personal Agentic AI Chatbot  

This guide provides step-by-step instructions to set up your environment and run the project.  
It supports multiple options for virtual environments (**Pipenv, pip+venv, Conda**).  

---

## 🛠️ Setting Up a Python Virtual Environment  

### Using Pipenv
1. **Install Pipenv (if not already installed):**
   ```bash
   pip install pipenv

### **Phase 1 – AI Agent**
1. Setup API Keys for Groq, Tavily, OpenAI  
2. Configure LLMs & Tools  
3. Build AI Agent with optional search functionality  

### **Phase 2 – Backend (FastAPI)**
1. Define request schema with Pydantic  
2. Build `/chat` API endpoint for frontend → backend communication  
3. Run app & explore Swagger UI Docs at `/docs`  

### **Phase 3 – Frontend (Streamlit)**
1. Build UI (provider, model, system prompt, query input)  
2. Connect frontend to backend via REST API  

---

## 🛠️ Tools & Technologies

- **LangGraph** → ReAct agents for orchestration  
- **FastAPI** → Backend APIs & docs  
- **Groq & OpenAI** → LLM providers  
- **Streamlit** → Frontend UI  
- **LangChain** → Tool integrations (e.g. Tavily search)  
- **Pydantic** → Input validation  
- **Uvicorn** → ASGI server  
- **Python** → Core programming language  



