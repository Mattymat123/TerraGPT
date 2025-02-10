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
from get_response import get_response
from chat_to_conversation_history import chat_to_conversation_history

diamond = st.secrets["diamond"]["diamond"]

with open('frontend/styles.css') as f:
    css = f.read()

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["ND_API_KEY"] = diamond

st.set_page_config(page_title="TerraGPT", initial_sidebar_state="expanded", layout = 'wide')
left_column, right_column = st.columns(2)

if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown(footer, unsafe_allow_html=True)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)


#right side of screen.
user_query = st.chat_input("Din besked")
client = NotDiamond(api_key="sk-9757bf097cf91c6727a251c97e278338a254c18d4f309020")
final_label, model = classify_diamond("Your prompt here")
print(final_label)
def energi_sparet(provider_model):
    deepseek_forskelle = {
        'llama-3.1-sonar-large-128k-online': 48,
        'Llama-3-8b-chat-hf': 48,
        'meta-llama-3-70b-instruct': 9.6,
        'codestral-latest': 21
    }
    deepseek_forskel = deepseek_forskelle.get(provider_model)
    print(provider_model)
    return deepseek_forskel



if user_query:
    classification, _ = classify_diamond(user_query)
else:
    classification = None

if not st.session_state.chat_history:
    with st.chat_message("assistant", avatar="frontend/robot.svg"):
        st.markdown(
            """
            <font size="5" >Velkommen til Terra GPT! </font><br>  
            Med Terra GPT bruger du kunstig intelligens mere energisparsomt.
            Jeg er klar til dine spørgsmål og opgaver:) 
            """, unsafe_allow_html=True
        )
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="frontend/user.svg"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="frontend/robot.svg"):
            st.markdown(message.content)

energi = 0
if user_query:
    st.session_state.chat_history.append(HumanMessage(content=user_query))
    with st.chat_message("user", avatar="frontend/user.svg"):
        st.markdown(user_query)
    streamed_response = ""
    with st.chat_message("assistant", avatar="frontend/robot.svg"):
        response_placeholder = st.empty()
        for chunk in get_response(user_query, st.session_state.chat_history, classification):
            streamed_response += chunk
            response_placeholder.markdown(streamed_response + "▌")
        energi = energi_sparet(model)
        print(energi)
        response_placeholder.markdown(streamed_response)
    st.session_state.chat_history.append(AIMessage(content=streamed_response))


#Left side of screen
with st.sidebar:
    if energi:
        st.markdown(f"🐋 bruger {energi} mere energi!")
    button1 = st.button('New chat')
    if button1:
        chat_to_conversation_history(st.session_state.chat_history)
        #print(st.session_state.conversation_history)
        for i in st.session_state.conversation_history.keys():
            st.button(f"{st.session_state.conversation_history[i][0].content}")




