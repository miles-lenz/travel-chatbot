from typing import Generator

from ollama import chat
import gradio as gr


SYSTEM_PROMPT = open("prompt.txt", encoding="utf-8").read().strip()

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

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        *history,
        {"role": "user", "content": message}
    ]

    stream = chat(model=MODEL, messages=messages, stream=True)

    response = ""
    for chunk in stream:
        response += chunk.message.content
        yield response


# Create an initial welcome message by generating the response with no input
# or history and just the system prompt.
init_message = ""
for chunk in get_response("", []):
    init_message = chunk

# Create a custom gradio chatbot with the initial messages.
chatbot = gr.Chatbot(
    type="messages",
    scale=1,
    height=400,
    value=[{"role": "assistant", "content": init_message}]
)

# Create a Gradio chat interface to allow interaction with the chatbot.
demo = gr.ChatInterface(
    fn=get_response,
    chatbot=chatbot,
    type="messages",
    title="Travel Chatbot",
)


if __name__ == "__main__":
    demo.launch()
