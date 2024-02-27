import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_text(todos)


st.title("TO-DO App")
st.subheader("this is my first web app")
st.write("this is a daily planner app")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_text(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="add to-do", placeholder="enter here",
              on_change=add_todo, key="new_todo")

print("hello")