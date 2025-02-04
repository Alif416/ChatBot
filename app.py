from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

# Define custom prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You will answer at bangla"),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

# Initialize components
llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0.7)
memory = ConversationBufferMemory(return_messages=True)  # Add return_messages=True

# Create conversation chain WITH CUSTOM PROMPT
conversation = ConversationChain(
    llm=llm,
    memory=memory,
    prompt=prompt,  # Now using your custom prompt
    verbose=False
)

# Chat interface
print("Chatbot: Hello! How can I help you today? (Type 'exit' to quit)")
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit", "ok bye then","bye"]:
        print("Chatbot: Goodbye!")
        break
    response = conversation.invoke({"input": user_input})
    print(f"Chatbot: {response['response']}")