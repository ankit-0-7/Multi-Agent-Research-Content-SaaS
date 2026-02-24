<div align="center">
  <img src="https://img.shields.io/badge/Next.js-black?style=for-the-badge&logo=next.js&logoColor=white" alt="Next.js" />
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI" />
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/LangGraph-FF4F00?style=for-the-badge&logo=langchain&logoColor=white" alt="LangGraph" />
  <img src="https://img.shields.io/badge/Groq-8A2BE2?style=for-the-badge&logo=openai&logoColor=white" alt="Groq" />
</div>

<h1 align="center">AIRes ⚛️ <br> Autonomous Multi-Agent Research Engine</h1>

<p align="center">
  <strong>A full-stack AI SaaS that moves beyond standard prompting by utilizing an autonomous agent workflow to research, synthesize, and format live data from the web.</strong>
</p>

---

## 🚀 Overview

AIRes is a vertical AI SaaS application built to automate deep research and content creation. Unlike traditional LLM wrappers that rely on outdated training data, AIRes utilizes a Directed Acyclic Graph (DAG) Agentic Architecture. 

When given a topic, the system spins up specialized AI workers (Nodes) that autonomously search the live internet, read multiple sources, and compile the findings into a highly formatted, ready-to-publish Markdown document.

## 🧠 System Architecture



1. **The Interface (Next.js):** A modern, responsive React frontend styled with Tailwind CSS and react-markdown for rich text rendering.
2. **The Bridge (FastAPI):** A high-performance Python web server acting as the decoupled backend API.
3. **The Brain (LangGraph):** Manages state flow between specialized AI agents.
4. **The Tools (Tavily & Groq):** Provides the agents with real-time web access and lightning-fast Llama 3.3 reasoning capabilities.

---

## ✨ Key Features

* **Real-Time Web Access:** Bypasses standard LLM knowledge cutoffs using the Tavily Search API.
* **Agentic Workflow:** Tasks are divided between a Researcher agent and a Writer agent.
* **Ultra-Fast Inference:** Powered by Groq's LPU inference engine for near-instantaneous text generation.
* **Decoupled SaaS Architecture:** Clean separation of concerns between the React frontend and the Python backend.
* **Rich Markdown Rendering:** Outputs professional, formatted content with headings, lists, and bolding.

---

## 🛠️ Tech Stack

### Frontend
* **Framework:** Next.js (App Router)
* **Styling:** Tailwind CSS + Typography Plugin
* **Icons:** Lucide-React
* **Markdown:** React-Markdown

### Backend
* **API Framework:** FastAPI + Uvicorn
* **AI Orchestration:** LangGraph & LangChain
* **LLM:** Llama 3.3 (via Groq)
* **Search Engine:** Tavily API

---

## 💻 Local Installation & Setup

### Prerequisites
* Python 3.9+
* Node.js 18+
* Free API keys from Groq and Tavily

### 1. Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install langgraph langchain-groq langchain-tavily python-dotenv fastapi uvicorn pydantic
```
### 2. Create a .env file in the backend folder and add your keys:
```bash
cd backend
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
### 3. Start the FastAPI server:
```bash
cd backend
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```
### 4. Frontend Setup:
```bash
cd frontend
npm install
npm run dev
```
## ✨ Future Roadmap
1. **Implement MongoDB to save and retrieve user research history.**
2. **Add a Fact Checker agent node to the LangGraph workflow.** 
3. **PDF Export functionality for downloaded research briefs.**
4. **User authentication.**


<h4 align="center"> <br> Built with ❤️ to explore the future of Agentic AI.</h4>

