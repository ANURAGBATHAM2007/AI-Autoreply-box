import streamlit as st
from 01_get_cursor import some_function   # change with actual function name
from 02_openai import openai_function     # change with actual function name
from 03_bot import bot_function           # change with actual function name

st.title("My Streamlit Bot")

# Example usage
if st.button("Run Bot"):
    cursor = some_function()
    response = openai_function(cursor)
    result = bot_function(response)
    st.write(result)

