import streamlit as st
import cfun

todos = cfun.get_todos()


st.title("My Todo App")
st.subheader("")
st.write("")




for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo")

