import streamlit as st
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder


load_dotenv()


st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="wide")

st.title("🤖 AI Chatbot - Powered by Llama 3")


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a coding assistant. You will do assignments and write efficient human-like code to avoid plagiarism."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])


llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
memory = ConversationBufferMemory(return_messages=True)

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input field
user_input = st.chat_input("Type your message here...")

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    response = conversation.invoke({"input": user_input})["response"]
    st.session_state.messages.append({"role": "assistant", "content": response})


    with st.chat_message("assistant"):
        st.markdown(response)
