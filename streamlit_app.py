import streamlit as st

st.title("My First Streamlit App")
st.write("This app was deployed using Streamlit Cloud!")

# Text input section
user_text = st.text_input("Type something:")

# Display typed text
if user_text:
    st.write("You typed:", user_text)
