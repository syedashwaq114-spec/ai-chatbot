import streamlit as st
from openai import OpenAI

st.title("AI Chatbot (Free Version) 🤖")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        try:
            response = client.chat.completions.create(
                model="meta-llama/llama-3-8b-instruct",
                messages=st.session_state.messages
            )
            reply = response.choices[0].message.content
        except Exception as e:
            reply = f"Error: {e}"

        st.markdown(reply)

        st.session_state.messages.append(
            {"role": "assistant", "content": reply}
        )