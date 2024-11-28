import streamlit as st
import google.generativeai as genai

# Configure Generative AI API
genai.configure(api_key="AIzaSyBz6g-XUefQQ_TABX13P6K6TrJ6rOQQtF0")  # Replace with your actual API key

# Initialize session state for chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Predefined answers for common questions
predefined_answers = {
    "What is photosynthesis?": "Photosynthesis is the process by which green plants use sunlight to synthesize food from carbon dioxide and water. It primarily occurs in the chloroplasts of plant cells.",
    "What is Newton's First Law?": "Newton's First Law states that an object at rest will remain at rest, and an object in motion will continue in motion unless acted upon by an external force.",
    # Add more predefined questions and answers here
}

# Function to get chatbot response
def get_response(user_input):
    if user_input in predefined_answers:
        return predefined_answers[user_input]
    else:
        prompt = f"""
        You are a knowledgeable assistant designed to help users with their study notes and academic concepts.
        Provide clear, concise, and informative answers relevant to study material or general educational topics.

        Question from user:
        {user_input}

        Your response should be:
        - Informative and straightforward.
        - Relevant to typical study notes or academic subjects.
        - Concise, with examples or key points if applicable.
        """
        
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text


# Styling and layout
st.markdown(
    f"""
    <style>
    .chat-container {{
        background-color: #FFB703;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }}
    .user-message {{
        background-color: #219EBC;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
        color: white;
        font-weight: bold;
    }}
    .bot-message {{
        background-color: #FB8500;
        padding: 10px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
    }}
    .input-box {{
        background-color: #fff;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #023047;
        margin-bottom: 10px;
    }}
    .title {{
        text-align: center;
        font-size: 2.5em;
        color: #023047;
        font-weight: bold;
    }}
    footer {{
        text-align: center;
        font-size: 0.9em;
        margin-top: 30px;
        color: #023047;
    }}
    hr {{
        border: 1px solid #023047;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# App title
st.markdown('<div class="title">📚 CourseCapsule Chatbot</div>', unsafe_allow_html=True)
st.write("Ask any academic question, and the chatbot will provide relevant information!")

# User input
user_input = st.text_input(
    "Ask a question:", 
    placeholder="Type your question here...", 
    label_visibility="hidden"
)

# Handle user input
if user_input:
    bot_response = get_response(user_input)
    st.session_state["history"].append({"user": user_input, "bot": bot_response})

# Chat history display
for chat in st.session_state["history"]:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="user-message">You: {chat["user"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="bot-message">Bot: {chat["bot"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer styling
st.markdown(
    """
    <footer>
        <hr>
        <p>✨ Powered by CourseCapsule & Generative AI ✨</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
