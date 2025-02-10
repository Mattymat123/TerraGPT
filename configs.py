TOKEN_Qwen = "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"
Token_Gemini = "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"
TOKEN_Phi = "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"

MODEL_CONFIG = {
    "coding": {
        "model_name": "qwen/qwen-2.5-coder-32b-instruct",
        "api_key": TOKEN_Qwen,
        "template": (
            "You are an expert programmer and debugging assistant. Provide clear, concise "
            "coding solutions and explanations. Answer in the language of the user's input (Danish or English).\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    },
    "ifeval": {
        "model_name": "meta-llama/llama-3.1-70b-instruct",
        "api_key": Token_Gemini,
        "template": (
            "You are a helpful assistant skilled in reasoning and problem solving. Provide thoughtful, "
            "detailed explanations for instructive or evaluative queries. Answer in the language of the user's input (Danish not swedish or English) Keep the responses short and concise.\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    },
    "mmlu": {
        "model_name": "microsoft/phi-4",  # Replace with the actual Phi model name
        "api_key": TOKEN_Phi,
        "template": (
            "You are an academic expert with broad knowledge. Provide well-reasoned, accurate answers "
            "to general knowledge and reasoning questions. Answer in the language of the user's input (Danish or English).\n\n"
            "Chat history: {chat_history}\n\nUser question: {user_question}"
        )
    }
}

