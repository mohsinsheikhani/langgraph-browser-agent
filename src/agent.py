from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI

from src.config import Config
from src.tools import get_push_tool


class State(TypedDict):
    messages: Annotated[list, add_messages]


class BrowserAgent:
    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=Config.MODEL_NAME,
            api_key=Config.GOOGLE_API_KEY,
            temperature=0,
        )
        self.tools = self._setup_tools()
        self.graph = self._build_graph()

    def _setup_tools(self):
        """Initialize tools for the agent."""
        push_tool = get_push_tool()
        return [push_tool]

    def _build_graph(self):
        """Build the LangGraph workflow."""
        llm_with_tools = self.llm.bind_tools(self.tools)

        def chatbot(state: State):
            return {"messages": [llm_with_tools.invoke(state["messages"])]}

        graph_builder = StateGraph(State)

        graph_builder.add_node("chatbot", chatbot)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))

        graph_builder.add_edge(START, "chatbot")
        graph_builder.add_conditional_edges("chatbot", tools_condition, "tools")
        graph_builder.add_edge("tools", "chatbot")

        memory = MemorySaver()
        return graph_builder.compile(checkpointer=memory)

    async def chat(self, user_input: str, thread_id: str = "default"):
        """Process user input and return agent response."""
        config = {"configurable": {"thread_id": thread_id}}

        result = await self.graph.ainvoke(
            {"messages": [{"role": "user", "content": user_input}]}, config=config
        )
        return result["messages"][-1].content
