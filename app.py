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
from streamlit_vertical_slider import vertical_slider
from streamlit_extras.app_logo import add_logo

diamond = st.secrets["diamond"]["diamond"]

with open('frontend/styles.css') as f:
    css = f.read()

os.environ["OPENAI_API_BASE"] = "https://openrouter.ai/api/v1"
os.environ["ND_API_KEY"] = diamond

st.set_page_config(page_title="TerraGPT", initial_sidebar_state="expanded", layout='wide')
left_column, right_column = st.columns(2)

# Initialize session state variables if they don't exist
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = {}
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "energi" not in st.session_state:
    st.session_state.energi = 0

if "energi_percent" not in st.session_state:
    st.session_state.energi_percent = 0
st.markdown(footer, unsafe_allow_html=True)
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
st.markdown('<meta name="viewport" content="width=device-width, initial-scale=1.0">', unsafe_allow_html=True)

# Right side of screen
user_query = st.chat_input("Din besked")
client = NotDiamond(api_key="sk-9757bf097cf91c6727a251c97e278338a254c18d4f309020")

def energi_sparet(provider_model, model):
    deepseek_forskelle = {
        'sonar': 9.6,
        'Llama-3-8b-chat-hf': 48,
        'meta-llama-3-70b-instruct': 9.6,
        'codestral-latest': 21,
        "command-r-plus": 15
    }
    claude_forskelle = {
        'sonar': 2.5,
        'Llama-3-8b-chat-hf': 12.5,
        'meta-llama-3-70b-instruct': 2.5,
        'codestral-latest': 5.5,
        "command-r-plus": 5
    }
    Chat_GPT_forskelle = {
        'sonar': 2.3,
        'Llama-3-8b-chat-hf': 12.5,
        'meta-llama-3-70b-instruct': 2.5,
        'codestral-latest': 5.5,
        "command-r-plus": 5
    }

    # Choose the correct dictionary based on the model parameter
    if model == '🐋 Deepseek R1':
        forskelle = deepseek_forskelle
    elif model == '✺ Claude 3.5 Sonnet':
        forskelle = claude_forskelle
    elif model == '֍ ChatGPT 4o':
        forskelle = Chat_GPT_forskelle
    forskel = forskelle.get(provider_model)
    return forskel

if user_query:
    classification, _ = classify_diamond(user_query)
else:
    classification = None

if not st.session_state.chat_history:
    with st.chat_message("assistant", avatar="frontend/robot.svg"):
        st.markdown(
            """
            <style>
            h1 {
                font-size: 36px !important;
            }
            h2 {
                font-size: 28px !important;
            }
            </style>

            # Velkommen til Terra GPT!

            Terra GPT giver dig den bedste mulighed for at arbejde med AI på en energibevidst og effektiv måde.

            ## Energisparende ⚡

            Terra GPT anvender specialiserede AI-modeller til at besvare dine spørgsmål. Disse modeller er små og kræver mindre computerkraft.  Du kan derfor bruge Terra GPT med god samvittighed.

            ## Høj Ydeevne 💪🏿
           Med Terra GPT får du automatisk adgang til de nyeste og mest avancerede AI-modeller, der er skræddersyet til at løse dine specifikke opgaver.
           Uanset om du skal skrive en e-mail, lave en kort historie eller programmere, leverer Terra GPT bedre performance end ChatGPT-4o med et meget lavere klimaaftryk.
             
            ## Sikkerhed og Data 🔒
           Hos Terra GPT bliver din data ikke opbevaret af tredjeparter eller solgt videre til andre leverandører. 
            
            Terra GPT er klar til at hjælpe dig:)
            """,
            unsafe_allow_html=True
        )
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user", avatar="frontend/user.svg"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant", avatar="frontend/robot.svg"):
            st.markdown(message.content)

with st.sidebar.container():
    col1 = st.columns([1])[0]

    with col1:
        st.subheader("Tidligere samtaler")
        button1 = st.button('Start ny samtale')
    if button1:
        try:
            new_chat_history = {'key1': [{'content': 'Hello!'}], 'key2': [{'content': 'How are you?'}]}
            chat_to_conversation_history(new_chat_history)
        except Exception as e:
            st.error(f"Error updating conversation: {e}")

    buttons = []
    if st.session_state.conversation_history:
        for i in st.session_state.conversation_history.keys():
            if st.session_state.conversation_history[i] and len(st.session_state.conversation_history[i]) > 0:
                buttons.append(st.button(f"{st.session_state.conversation_history[i][0].content}"))

    for button in buttons:
        if button:
            st.write(f"Button clicked: {button}")
    option = st.selectbox("Sammenlignet med AI-model", options=['🐋 Deepseek R1', '֍ ChatGPT 4o', "✺ Claude 3.5 Sonnet"])

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
        final_label, model = classify_diamond(f"{user_query}")
        energi_forskel = energi_sparet(model, option)
        energi_forskel = 100/energi_forskel
        print(energi_forskel)
        energi_forskel = int(energi_forskel)
        st.session_state.energi = energi_forskel
        st.session_state.energi_percent = 100-energi_forskel
        response_placeholder.markdown(streamed_response)
    st.session_state.chat_history.append(AIMessage(content=streamed_response))

with st.sidebar.container():

    vertical_slider(
        label=f"🔋{st.session_state.energi_percent}% Energi sparet",
        height=200,
        step=1,
        min_value=0,
        max_value=100,
        track_color="#639c5f",
        thumb_color="grey",
        slider_color = ('#421713'),
        default_value = st.session_state.energi
    )


