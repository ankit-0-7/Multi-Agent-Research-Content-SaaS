from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from .nodes import researcher_node, writer_node

# 1. Define the 'Shared Notebook' (State)
# This dictates what data flows between the nodes.
class AgentState(TypedDict):
    topic: str
    research_notes: str
    content_draft: str

# 2. Initialize the Graph
# We pass our state schema so the graph knows what data to expect.
workflow = StateGraph(AgentState)

# 3. Add our agents as 'Nodes'
# This tells LangGraph which functions to execute.
workflow.add_node("researcher", researcher_node)
workflow.add_node("writer", writer_node)

# 4. Set the Flow (Edges)
# Start -> Research -> Write -> End
workflow.add_edge(START, "researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

# 5. Compile the Graph
# This turns our design into an executable application.
graph_app = workflow.compile()