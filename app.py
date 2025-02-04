from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)


memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=False  # Set to True to see internal steps
)

print("Chatbot: Hello! How can I help you today? (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Chatbot: Goodbye!")
        break
    response = conversation.predict(input=user_input)
    print(f"Chatbot: {response}")
