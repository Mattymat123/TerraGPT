import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from notdiamond import NotDiamond
import os
from Classify_function import classify_diamond
from footer import footer
from configs import MODEL_CONFIG
import uuid

def get_response(user_query, chat_history, classification):
    config = MODEL_CONFIG.get(classification)
    if not config:
        fallback_message = f"No model configured for classification '{classification}'"
        print(classification)
        return iter([fallback_message])
    template_str = config.get("template")
    prompt = ChatPromptTemplate.from_template(template_str)
    llm = ChatOpenAI(
        model_name=config["model_name"],
        openai_api_key=config["api_key"],
        openai_api_base=os.environ.get("OPENAI_API_BASE"),
        streaming=True,
        temperature=0.8,
    )

    print(llm.model_name)
    chain = prompt | llm | StrOutputParser()
    return chain.stream({
        "chat_history": chat_history,
        "user_question": user_query
    })