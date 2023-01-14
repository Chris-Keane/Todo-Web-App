import streamlit as st
import functions

def add_todo():
    todo = st.session_state["new_todo"] + "\n"

    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)

todos = functions.get_todos()

st.title("Todo App")
st.subheader("My Todo App")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=str(index))
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[str(index)]
        st.experimental_rerun()

st.text_input(label="Add Below", placeholder="Enter a task",
              on_change=add_todo, key="new_todo", label_visibility='hidden')