import streamlit as st
import requests

# Set page title and style
st.set_page_config(page_title="Random Joke Generator", layout="wide", page_icon=":joy:")

# Set background color and text color
page_bg = """
<style>
body {
background-color: #FFD700;
color: #333333;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Set title and header style
st.title("Random Joke Generator")
st.markdown("---")

# Fetch a random joke from an API
response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke_data = response.json()

# Display the joke
st.write(f"**Category:** {joke_data['type']}")
st.markdown(f"<h1 style='font-size: 36px;'>{joke_data['setup']}</h1>", unsafe_allow_html=True)
st.markdown(f"**Punchline:** {joke_data['punchline']}")

# Button to fetch a new joke
if st.button("Get Another Joke"):
    response = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke_data = response.json()
    st.write(f"**Category:** {joke_data['type']}")
    st.markdown(f"<h1 style='font-size: 36px;'>{joke_data['setup']}</h1>", unsafe_allow_html=True)
    st.markdown(f"**Punchline:** {joke_data['punchline']}")
