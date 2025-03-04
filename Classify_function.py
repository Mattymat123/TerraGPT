from notdiamond import NotDiamond
import streamlit as st
diamond = st.secrets["diamond"]["diamond"]
client = NotDiamond(api_key=f"{diamond}")
def classify_diamond(prompt):
    session_id, provider = client.chat.completions.model_select(
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        model=[
            "perplexity/sonar",
            "togetherai/Llama-3-8b-chat-hf",
            "replicate/meta-llama-3-70b-instruct",
            "mistral/codestral-latest",
            "cohere/command-r-plus"
        ], tradeoff= "cost"
    )
    model_to_label = {
        "sonar": "web-search",
        "meta-llama-3-70b-instruct": "instruction",
        "codestral-latest": "coding",
        "Llama-3-8b-chat-hf": "conversation",
        "command-r-plus": "creative_writing"
    }
    final_label = model_to_label.get(provider.model)
    model = provider.model
    #print("Final label:", final_label, "Provider model:", provider.model)
    return final_label, model