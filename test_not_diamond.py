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
        ],
    )
    model_to_label = {
        "llama-3.1-sonar-large-128k-online": "web-søgning",
        "meta-llama-3-70b-instruct": "instruktion",
        "codestral-latest": "kodning",
        "Llama-3-8b-chat-hf": "samtale",
        "command-r-plus": "kreativ-fritext"
    }
    final_label = model_to_label.get(provider.model)
    model = provider.model
    #print("Final label:", final_label, "Provider model:", provider.model)
    return final_label, model

label, model = classify_diamond("how are you?")
print(label, model)