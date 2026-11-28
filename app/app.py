import streamlit as st

st.set_page_config(page_title="VolleyBot", page_icon="🏐", layout="centered")

WELCOME_MESSAGE = {
    "role": "assistant",
    "content": (
        "Hi! I'm **VolleyBot**. Ask me anything about volleyball rules, "
        "scoring, rotations, positions, basic tactics, drills, or court etiquette."
    ),
    "context": None,
}

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [WELCOME_MESSAGE]

# Sidebar: scope info + Clear Chat button
with st.sidebar:
    st.header("🏐 About VolleyBot")
    st.markdown(
        "**VolleyBot** is a domain-specific assistant built strictly for "
        "**Volleyball**.\n\n"
        "**What I can help with:**\n"
        "- Official rules & scoring\n"
        "- Rotations & player positions\n"
        "- Basic tactics & training drills\n"
        "- Court etiquette & common fouls\n\n"
        "**Out of scope:**\n"
        "Non-volleyball topics, live referee rulings, and medical/injury advice."
    )
    st.divider()
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = [WELCOME_MESSAGE]
        st.rerun()

st.title("🏐 VolleyBot")
st.caption("Your Volleyball Rules, Scoring & Tips Assistant")

# Render chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and message.get("context"):
            with st.expander("Retrieved Dataset Context"):
                st.markdown(message["context"])

# Handle new user input
if raw_prompt := st.chat_input("Ask a volleyball question..."):
    prompt = raw_prompt.strip()

    # Handle blank/whitespace-only inputs gracefully
    if not prompt:
        st.warning("Please enter a volleyball question before sending.")
    else:
        st.session_state.messages.append(
            {"role": "user", "content": prompt, "context": None}
        )
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                with st.spinner("Thinking..."):
                    # Temporary fallback until VolleyBotEngine is pushed to src/
                    reply = (
                        f"You asked: **{prompt}**\n\n"
                        "*(Waiting for `VolleyBotEngine` in `src/` to be merged. "
                        "Once connected, this will return the live LLM answer.)*"
                    )
                    retrieved_context = (
                        "No dataset rows retrieved yet (`src/` backend not connected)."
                    )

                st.markdown(reply)
                with st.expander("Retrieved Dataset Context"):
                    st.markdown(retrieved_context)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": reply,
                        "context": retrieved_context,
                    }
                )
            except Exception as e:
                error_msg = f"Sorry, something went wrong while generating a response: {e}"
                st.error(error_msg)
                st.session_state.messages.append(
                    {"role": "assistant", "content": error_msg, "context": None}
                )