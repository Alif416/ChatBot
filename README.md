

````markdown
# 🤖 AI Chatbot - Powered by LLaMA 3 (LangChain + Groq + Streamlit)

This is an interactive **AI Chatbot web app** built using [Streamlit](https://streamlit.io/), [LangChain](https://www.langchain.com/), and [Groq](https://groq.com/) models like **LLaMA 3 (70B)**. The assistant is tailored to help users with coding assignments and write **efficient, human-like code** that avoids plagiarism.

---

## 🚀 Features

- 💬 Conversational memory to preserve context
- ⚡ Powered by **LLaMA 3 70B** via Groq for high performance
- 📚 Uses LangChain's conversation chaining & memory
- 🧠 Designed as a smart coding assistant
- 🌐 Runs on a modern, responsive Streamlit interface

---

## 🧰 Tech Stack

- **Streamlit** – for building the frontend chat UI
- **LangChain** – for prompt templates, memory, and chains
- **Groq** – for connecting to LLaMA 3 models
- **Python-dotenv** – for environment variable management

---

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/llama3-ai-chatbot.git
   cd llama3-ai-chatbot
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**

   Create a `.env` file in the root directory with your **Groq API key**:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

---

## 🧠 How It Works

* The chatbot uses a **ChatPromptTemplate** with a defined role as a coding assistant.
* It stores conversational history using `ConversationBufferMemory`.
* `ConversationChain` handles dynamic, context-aware conversations.
* Messages are displayed and updated live using `st.chat_input()` and `st.chat_message()`.

---

## 🖥️ Run the App

```bash
streamlit run app.py
```

Then open the provided `localhost` URL in your browser.

---

## 📁 File Structure

```
llama3-ai-chatbot/
├── app.py               # Main Streamlit chatbot application
├── .env                 # Your API keys (not included in version control)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

## 📌 Example Prompt

```
User: Can you write a Python program to sort a list of numbers?
AI: Sure! Here's a simple Python code using the built-in sorted() function...
```

---

## 🤝 Contribution

Feel free to open issues or pull requests. If you find this project useful, give it a ⭐ on GitHub!

---

## 📬 Contact

Developed by \[Your Name]
📧 [your.email@example.com](mailto:labibalif2001@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/labibul-ahsan-alif-b70974291/?originalSubdomain=bd)

---

## 📜 License

This project is licensed under the MIT License.


