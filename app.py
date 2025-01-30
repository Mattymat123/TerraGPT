import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os

st.set_page_config(page_title="TerraGPT")
st.header("TerraGPT")
st.subheader("Dine spørgsmål bruger en 30 gange mindre AI-model end chatGPT 🍃🍃🍃 \n ")

st.markdown("""
    <style>
        .top-right-box {
            position: fixed;
            bottom: 70px;
            left: 10px;
            background-color: #052802;
            color: white;
            font-size:20px;
            padding: 20px;
            border-radius: 10px;
            z-index: 1000;
        }
    </style>
""", unsafe_allow_html=True)

# Display content inside the box


TOKEN = "super-secret-token"
os.environ["OPENAI_API_BASE"] = "https://mattymat123--modal-first-deploy-serve.modal.run/v1"
os.environ["OPENAI_API_KEY"] = f"{TOKEN}"

# Make sure to store conversation in session_state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def get_response(user_query, chat_history):
    template = """You are a helpful and  polite chatbot speaking both english and danish. Answer the user helpfully in whatever language they input based on the User question and the Chat history.  User question og Chat history:
    Chat history: {chat_history}

    User question: {user_question}
    """
    prompt = ChatPromptTemplate.from_template(template)
    llm = ChatOpenAI(
        model_name="Meta-Llama-3.1-8B-Instruct-quantized.w4a16",
        streaming=False,
        temperature=0.8,
    )
    chain = prompt | llm | StrOutputParser()
    # chain.stream(...) returns a generator
    return chain.stream(
        {
            "chat_history": chat_history,
            "user_question": user_query
        }
    )


# 1) Capture the new user query via Streamlit's chat input
user_query = st.chat_input("Din besked")




# 2) Display all past messages from session_state.
#    *Do not* call get_response here. We already have the stored AI text in session_state.
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.markdown(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(message.content)

# 3) If there's a new user query, we now:
#    - append that query to session_state
#    - call get_response(...) and stream the output
#    - store the streamed output in session_state as an AIMessage
if user_query:
    # a) Store the user query in chat_history
    st.session_state.chat_history.append(HumanMessage(content=user_query))

    # b) Display the user's message right away
    with st.chat_message("user"):
        st.markdown(user_query)

    # c) Stream the LLM's response
    streamed_response = ""  # accumulate response chunks here
    with st.chat_message("assistant"):
        # Create a placeholder to update in a loop
        response_placeholder = st.empty()

        # get_response(...) returns a generator
        for chunk in get_response(user_query, st.session_state.chat_history):
            streamed_response += chunk
            response_placeholder.markdown(streamed_response + "▌")  # "▌" to show streaming

        # Once done, replace the trailing cursor symbol
        response_placeholder.markdown(streamed_response)

    # d) Save the final AI response back to session_state
    st.session_state.chat_history.append(AIMessage(content=streamed_response))
