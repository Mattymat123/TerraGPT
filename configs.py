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
        ),
        "data_collection": "deny"
    },
    "instruction": {
        "model_name": "meta-llama/llama-3.1-70b-instruct",
        "api_key": Gemini,
        "template": (
            "You are a helpful assistant skilled in reasoning and problem solving. Provide thoughtful, "
            "detailed explanations for instructive or evaluative queries. Answer in the language of the user's input (Danish not swedish or English) Keep the responses short and concise.\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        ),
        "data_collection": "deny"
    },
    "conversation": {
        "model_name": "microsoft/phi-4",  # Replace with the actual Phi model name
        "api_key": Gemini,
        "template": (
            "You are an academic expert with broad knowledge. Provide well-reasoned, accurate answers "
            "to general knowledge and reasoning questions. Answer in the language of the user's input .\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        ),
        "data_collection": "deny"
    },
    "creative_writing": {
        "model_name": "sao10k/l3.3-euryale-70b",  # Replace with the actual Phi model name
        "api_key": Gemini,
        "template": (
            "you are a well meaning role-playing and creative witing model. "
            "Answer in the role and style you've been assigned by the user.\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        ),
        "data_collection": "deny"
    },
    "web-search": {
        "model_name": "perplexity/llama-3.1-sonar-small-128k-online",  # Replace with the actual Phi model name
        "api_key": Gemini,
        "plugins": [
            {
                "id": "web",
                "max_results": 2
            }
        ],
        "template": (
            "You are an academic expert with broad knowledge. Provide well-reasoned, accurate answers "
            "If you don't know the answer state it clearly. Answer in the language of the user's input (Danish or English).\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        ),
        "data_collection": "deny"
    },
}