import secrets
import streamlit as st
Gemini = st.secrets["Gemini"]["Gemini"]
MODEL_CONFIG = {
    "coding": {
        "model_name": "qwen/qwen-2.5-coder-32b-instruct",
        "api_key": Gemini,
        "template": (
            "You are an expert programmer and debugging assistant. Provide clear, concise "
            "coding solutions and explanations. Answer in the language of the user's input (Danish or English).\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    },
    "ifeval": {
        "model_name": "meta-llama/llama-3.1-70b-instruct",
        "api_key": Gemini,
        "template": (
            "You are a helpful assistant skilled in reasoning and problem solving. Provide thoughtful, "
            "detailed explanations for instructive or evaluative queries. Answer in the language of the user's input (Danish not swedish or English) Keep the responses short and concise.\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    },
    "mmlu": {
        "model_name": "microsoft/phi-4",  # Replace with the actual Phi model name
        "api_key": Gemini,
        "template": (
            "You are an academic expert with broad knowledge. Provide well-reasoned, accurate answers "
            "to general knowledge and reasoning questions. Answer in the language of the user's input (Danish or English).\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    }
}

