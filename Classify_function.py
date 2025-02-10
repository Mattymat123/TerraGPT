from notdiamond import NotDiamond

client = NotDiamond(api_key="sk-9757bf097cf91c6727a251c97e278338a254c18d4f309020")
def classify_diamond(prompt):
    session_id, provider = client.chat.completions.model_select(
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": prompt}
        ],
        model=[
            "perplexity/llama-3.1-sonar-large-128k-online",
            "togetherai/Llama-3-8b-chat-hf",
            "replicate/meta-llama-3-70b-instruct",
            "mistral/codestral-latest"
        ],
        tradeoff="cost"
    )
    model_to_label = {
        "llama-3.1-sonar-large-128k-online": "mmlu",
        "meta-llama-3-70b-instruct": "ifeval",
        "codestral-latest": "coding",
        "Llama-3-8b-chat-hf": "mmlu"
    }
    final_label = model_to_label.get(provider.model)
    model = provider.model
    #print("Final label:", final_label, "Provider model:", provider.model)
    return final_label, model