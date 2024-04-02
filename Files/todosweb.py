import streamlit as st
import cfun

todos = cfun.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    cfun.write_todos(todos)



st.title("My Todo App")
st.subheader("")
st.write("")




for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Enter a todo",
              on_change=add_todo, key='new_todo')

st.session_state

