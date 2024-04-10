import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import time

# Load the environment variables from the .env file
load_dotenv()

# Get the API key and assistant id from the environment variables
api_key = os.getenv("API_KEY")
asst_id = os.getenv("ASST_ID")

# Set your OpenAI API key
client = OpenAI(api_key=api_key)
my_assistant = client.beta.assistants.retrieve(assistant_id=asst_id)

st.title("Personalized Assistant")

# Function to get or create the current thread
def get_or_create_thread():
    # verify if there is an existing thread
    existing_thread_id = st.session_state.get("thread_id", None)

    if existing_thread_id:
        # If exists, retrieve the thread
        return client.beta.threads.retrieve(thread_id=existing_thread_id)
    else:
        # If not exists, create a new thread
        new_thread = client.beta.threads.create()
        # Save the new thread id in the session state 
        st.session_state.thread_id = new_thread.id
        return new_thread


# get or create the current thread
thread = get_or_create_thread()

# Get the user query
message_content = st.text_input("Write a question:")


# Button to send the user message
if st.button("Send"):
    with st.spinner("Waiting for assistant response..."):
        # Create a new thread or get the existing one
        thread = get_or_create_thread()

        # Send the user message to the assistant thread
        user_message = client.beta.threads.messages.create(
            thread_id=thread.id, role="user", content=message_content
        )

        # Start the assistant
        run = client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=my_assistant.id,
        )

        # Wait for the assistant to complete
        run_status = None
        while run_status != "completed":
            run = client.beta.threads.runs.retrieve(
                thread_id=thread.id, run_id=run.id)
            run_status = run.status
            time.sleep(5)  # wait 5 seconds

        # Get assistant messages
        messages = client.beta.threads.messages.list(thread_id=thread.id)

        # Show assistant messages in the UI
        for msg in messages.data:
            if msg.role == "user":
                user_content = msg.content[0].text.value
                st.write(f"User: {user_content}")
            elif msg.role == "assistant":
                assistant_content = msg.content[0].text.value
                st.write(f"Assistant: {assistant_content}")
