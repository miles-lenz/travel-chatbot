# Travel Chatbot

This is a user-friendly chatbot developed for Fit Reisen, designed to assist users with various travel-related tasks.

The chatbot utilizes models from [Ollama](https://ollama.com/) and features an intuitive user interface built with [Gradio](https://www.gradio.app/).

## Installation

1. Install [Ollama](https://ollama.com/) and execute `ollama run gemma3` in a terminal.

2. Clone this repository with `git clone https://github.com/miles-lenz/travel-chatbot.git`

3. (Optional, but recommended) Create and activate a virtual environment.
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

4. Install required packages with `pip install -r requirements.txt`

## Usage

Run the command `python app.py` in a terminal. This will start the chatbot and provide a web link. Note that this may take some time.

## Demo

You can view a video demonstrating an example interaction with the chatbot on [my Google Drive](https://drive.google.com/file/d/1l_LEtIyc0-5chyn9qzpIwCw217_igBNo/view?usp=sharing).
The image below provides a snapshot from the video.

![thumbnail](https://github.com/miles-lenz/travel-chatbot/blob/main/thumbnail.png)

## Limitations

The models from Ollama are free to use but may not be state-of-the-art. While they offer decent accuracy, their capabilities are somewhat limited.
This is why the chatbot is in English, as most Ollama models appear to perform best in English, likely due to being primarily trained on English-language data.
Additionally, since they run locally on the machine, performance is also dependent on the machine's resources.

## Future Improvements

- Implementing Retrieval-Augmented Generation (RAG) can provide the chatbot with access to domain-specific knowledge, improving the accuracy of its responses.
- Integrating LangGraph could help guide and optimize the chatbot's behavior based on the user's request.
- Monitoring input size and message history will help prevent errors caused by exceeding the context window size.
- Upgrading to a more advanced model would enhance the overall performance and capabilities of the chatbot.
