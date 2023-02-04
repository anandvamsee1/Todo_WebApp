import streamlit as st
import functions
st.set_page_config(layout="wide")

todos = functions.get_todos()
def add_todo():
    todo = st.session_state["new_todo"]
    todos.append(todo+"\n")
    functions.write_todos(todos)


st.title("My Todo App")
st.write("This app is to increase your <b>Productivity</b>", unsafe_allow_html=True)
st.text_input(label='', placeholder='Enter a todo here...', key="new_todo", on_change=add_todo)
for idx, todo in enumerate(todos):
    checkbox = st.checkbox(label=todo, key=idx)
    if checkbox:
        todos.remove(todo)
        functions.write_todos(todos)
        del st.session_state[idx]
        st.experimental_rerun()



