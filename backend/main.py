from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agents.graph import graph_app # This is your LangGraph brain

app = FastAPI()

# 1. Setup CORS (Crucial for Codespaces)
# We allow everything ["*"] for development, but in production, you'd be specific.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 2. Define what the incoming request looks like
class ResearchRequest(BaseModel):
    topic: str

@app.get("/")
def read_root():
    return {"status": "AI Agent is Online"}

@app.post("/research")
async def run_research(request: ResearchRequest):
    # This is where the magic happens!
    # We take the topic from the frontend and hand it to your LangGraph.
    inputs = {"topic": request.topic}
    result = graph_app.invoke(inputs)
    
    # Send the final content back to Next.js
    return {"content_draft": result["content_draft"]}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)