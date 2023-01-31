import streamlit as st
import functions

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)


st.title("My Todo App")


for idx, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=idx)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[idx]
        st.experimental_rerun()

st.text_input(label='', placeholder='Enter a todo here...', key="new_todo", on_change=add_todo )

