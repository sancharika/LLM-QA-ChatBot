---
title: LLM QA ChatBot
emoji: 💻
colorFrom: purple
colorTo: blue
sdk: streamlit
sdk_version: 1.31.1
app_file: app.py
pinned: false
---

# Conversational Q&A Chatbot

This is a conversational Q&A chatbot built using Streamlit. The chatbot interacts with users by answering questions related to financial analysis of IPOs for startup companies.

## Setup and Usage

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/sancharika/LLM-QA-ChatBot.git
    ```

2. Navigate to the project directory:

    ```bash
    cd LLM-QA-ChatBot
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

5. Once the app is running, you can interact with the chatbot by typing your questions in the provided text input field and clicking the "Ask" button.

## Project Structure

- **app.py**: This is the main Python script containing the Streamlit UI code and the logic for interacting with the chatbot.
- **langchain**: This directory contains the schema for defining different types of messages (HumanMessage, SystemMessage, AIMessage).
- **langchain_openai**: This directory contains the code for interacting with the OpenAI GPT-3 model for generating responses to user questions.
- **.env**: This file contains environment variables used in the application (not included in this example).

## Dependencies

- Streamlit
- langchain
- langchain_openai
- python-dotenv

## How It Works

1. Users interact with the chatbot by typing questions related to financial analysis of IPOs for startup companies into the text input field.
2. The chatbot processes the user's question and generates a response using the OpenAI GPT-3 model.
3. The response is displayed to the user in the Streamlit app interface.

## Note

Make sure to set up your environment variables properly, especially if you're using any API keys or sensitive information.

## Contributors

- [Sancharika Debnath](https://github.com/sancharika)

Feel free to contribute to this project by submitting pull requests or reporting issues. Happy chatting! 🤖💬
