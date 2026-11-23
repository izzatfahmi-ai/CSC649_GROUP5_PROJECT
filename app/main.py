import streamlit as st

st.set_page_config(page_title="VolleyBot", page_icon="🏐", layout="centered")

st.title("🏐 VolleyBot")
st.caption("Your Volleyball Rules, Scoring & Tips Assistant")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! I'm VolleyBot. Ask me anything about volleyball rules, scoring, positions, or fouls."
        }
    ]

# Display existing chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handle user input
if prompt := st.chat_input("Ask a volleyball question..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Placeholder reply until backend (src/) is connected
    response = (
        f"You asked: **{prompt}**\n\n"
        "*(Backend is not connected yet. Once `src/` is ready, VolleyBot will answer using our volleyball dataset and LLM.)*"
    )

    # Show assistant reply
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
