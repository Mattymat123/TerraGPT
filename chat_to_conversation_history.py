import streamlit as st
import uuid

def chat_to_conversation_history(chat_history):
    key = uuid.uuid4().hex
    if st.session_state.chat_history != None:
        value = st.session_state.chat_history
    else:
        value = None
    st.session_state.conversation_history.update({key: value})
    st.session_state.chat_history = []

