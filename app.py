from typing import Generator

from ollama import chat
import gradio as gr


# Specify the model used for the chatbot.
# Ensure that the model is compatible with Ollama and is downloaded
# locally using `ollama pull <model_name>`.
MODEL = "gemma3:latest"


def get_response(message: str, history: list[dict]) -> Generator:
    """
    Generates a streaming response from the LLM.

    This function takes the latest user message and a history of previous
    messages and then stream the chatbot's response incrementally as it is
    generated.

    Arguments:
        message (str): The latest user message.
        history (list[dict]): The list of previous chat messages, where each
            message is represented as a dict with the keys 'role' and
            'content'.

    Yields:
        str: The progressively generated chatbot response.
    """

    messages = history + [{"role": "user", "content": message}]

    stream = chat(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.message.content
        yield response


# Create a Gradio chat interface to allow interaction with the chatbot.
demo = gr.ChatInterface(
    fn=get_response,
    type="messages",
    title="Travel Chatbot",
)


if __name__ == "__main__":
    demo.launch()
