import os
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Initialize the AI Brain and the Search Tool
# We use Llama 3.3 via Groq for high-speed inference
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)
search_tool = TavilySearchResults(max_results=3)

def researcher_node(state):
    """
    This agent searches the web for live data.
    """
    print("--- 🔍 AGENT: RESEARCHER IS SEARCHING THE WEB ---")
    topic = state['topic']
    
    # Perform a web search using Tavily
    results = search_tool.invoke({"query": f"latest news and facts about {topic} 2026"})
    
    # Combine the search results into a single string
    context = "\n".join([res['content'] for res in results])
    
    # Update the state with the raw notes
    return {"research_notes": context}

def writer_node(state):
    """
    This agent takes the research notes and formats them into content.
    """
    print("--- ✍️ AGENT: WRITER IS COMPOSING ---")
    notes = state['research_notes']
    topic = state['topic']
    
    # Give the AI its persona and task
    prompt = f"""
    You are an expert content creator. 
    Topic: {topic}
    Research Notes: {notes}  
    
    Write a short, engaging LinkedIn post about this topic using Markdown. 
    Include emojis and a 'Key Takeaways' section.
    """
    
    response = llm.invoke(prompt)
    
    # Update the state with the final draft
    return {"content_draft": response.content}