import nest_asyncio
import gradio as gr
from src.agent import BrowserAgent

# Apply nest_asyncio for Jupyter/async compatibility
nest_asyncio.apply()


def main():
    """Launch the browser agent with Gradio interface."""
    agent = BrowserAgent()

    async def chat_interface(user_input: str, history):
        """Gradio chat interface handler."""
        response = await agent.chat(user_input, thread_id="gradio_session")
        return response

    # Launch Gradio interface
    interface = gr.ChatInterface(
        chat_interface,
        type="messages",
        title="LangGraph Browser Agent",
        description="AI agent with browser automation and push notifications",
    )

    interface.launch(share=False, server_name="0.0.0.0")


if __name__ == "__main__":
    main()
