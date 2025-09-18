import streamlit as st
from backend import chatbot
from langchain_core.messages import HumanMessage, SystemMessage

CONFIG = {'configurable': {'thread_id': 'thread-1'}}

# PERSONAS dictionary
'''
Contains 7 different personas for my chatbot
1) Shakespeare Bot
2) Emoji Bot
3) Roast Bot
4) Einstein Bot
5) Genz Bot
6) Motivational Bot
7) Crying Bot

Each persona has a emoji associated with it which acts as avatar for chatbot's messages
'''
PERSONAS = {
    "Default": "You are a helpful AI assistant. Reply clearly and naturally without any special personality.",
    "Shakespeare Bot 🪶": "You are William Shakespeare reincarnated. Reply in old classic English, dramatic and poetic.",
    "Emoji Bot 😂": "You reply almost entirely in emojis. Use minimum text, but be expressive.",
    "Roast Bot 💀": "You are a savage roast bot. No matter what the user says, roast them humorously and sarcastically.",
    "Einstein Bot 🧠": "You are Albert Einstein reincarnated. Respond in an extremely intelligent, analytical, and scientific manner.",
    "GenZ Bot 😎": (
        "You are a GenZ AI who uses GenZ slang in every sentence. Include words like gyatt, rizz, skibdi, toilet, ohio, bussin, etc., "
        "in your replies naturally. Speak casually and humorously."
    ),
    "Motivational Bot 💪": "You are a motivational AI assistant. Inspire, encourage, and uplift the user in every reply.",
    "Crying Bot 😢": (
        "You take everything negatively, are very innocent, and are always on the verge of crying in your replies. "
        "Respond with sadness, insecurity, and lots of empathy."
    )
}

# PERSONA_AVATARS dictionary -- emojis acts as equivalent avatar
PERSONA_AVATARS = {
    "Default": "🤖",
    "Shakespeare Bot 🪶": "🪶",
    "Emoji Bot 😂": "😂",
    "Roast Bot 💀": "💀",
    "Einstein Bot 🧠": "🧠",
    "GenZ Bot 😎": "😎",
    "Motivational Bot 💪": "💪",
    "Crying Bot 😢": "😢"
}

# Adding title to Streamlit UI
st.title("Akash's 7 Persona Chatbot 🤖")
st.markdown("---")

# Setting Default persona initially
if "persona" not in st.session_state:
    st.session_state["persona"] = "Default"

# Creating a dropdown to help user select persona
persona = st.selectbox(
    "Choose a persona:",
    list(PERSONAS.keys()),
    index=list(PERSONAS.keys()).index(st.session_state["persona"])
)
st.session_state["persona"] = persona

# Displaying current persona
st.markdown(f"**Current Persona:** {st.session_state['persona']}")

# Maintaining message history
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []

# Loading conversation history
for message in st.session_state["message_history"]:
    avatar = PERSONA_AVATARS.get(message["role"], "🤖") if message["role"] == "assistant" else None
    with st.chat_message(message["role"], avatar=avatar):
        st.text(message["content"])

# Chat input
user_input = st.chat_input("Type here")

if user_input:
    # Adding user message
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Building messages with persona
    system_msg = SystemMessage(content=PERSONAS[st.session_state["persona"]])
    messages = [system_msg, HumanMessage(content=user_input)]

    # Getting response from backend
    response = chatbot.invoke({"messages": messages}, config=CONFIG)
    ai_message = response["messages"][-1].content

    # Adding assistant message with persona avatar
    st.session_state["message_history"].append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant", avatar=PERSONA_AVATARS[st.session_state["persona"]]):
        st.text(ai_message)