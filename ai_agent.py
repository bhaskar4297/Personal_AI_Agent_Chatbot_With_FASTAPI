# ai_agent.py (Groq + minimal tools)

import os
import requests
from dotenv import load_dotenv

load_dotenv()

# API Keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")
# LLM
from langchain_groq import ChatGroq
from langchain_experimental.tools import PythonREPLTool

# Tavily Search
try:
    from langchain_tavily import TavilySearchResults
except ImportError:
    from langchain_community.tools.tavily_search import TavilySearchResults

# Wikipedia
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# Weather (custom tool)
from langchain_core.tools import Tool
def weather_lookup(city="London"):
    url = f"https://wttr.in/{city}?format=3"
    try:
        return requests.get(url, timeout=10).text
    except Exception as e:
        return f"Weather error: {e}"

# Agent framework
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


def get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider):
    if provider != "Groq":
        return {"error": "Currently only Groq provider is supported."}

    llm = ChatGroq(model=llm_id, api_key=GROQ_API_KEY)

    # Tools
    tools = [PythonREPLTool(), WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())]
    if allow_search and TAVILY_API_KEY:
        tools.append(TavilySearchResults(max_results=2, api_key=TAVILY_API_KEY))
    tools.append(Tool.from_function(weather_lookup, name="weather_lookup", description="Get weather for a city"))

    agent = create_react_agent(model=llm, tools=tools)

    # Build messages
    state = {"messages": [SystemMessage(content=system_prompt)]}
    for msg in query:
        state["messages"].append(HumanMessage(content=msg))

    # Run
    response = agent.invoke(state)
    messages = response.get("messages", [])
    ai_messages = [m.content for m in messages if isinstance(m, AIMessage)]
    return ai_messages[-1] if ai_messages else "No response from agent."
