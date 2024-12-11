from cgitb import enable

import streamlit as st
from streamlit import text_input

import functions
from functions import get_todo

def addTodo():
    newTodo = st.session_state["tbNewTodo"] + "\n"
    if newTodo in todo:
        st.session_state["tbNewTodo"] = value = ""
        st.error("You already have this listed")
    else:
        todo.append(newTodo)
        functions.set_todo(todo)
        st.session_state["tbNewTodo"] = value=""



todo = functions.get_todo()


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("this app increase your productivity")

for index, i in enumerate(todo):
    checkbox = st.checkbox(i, key=i)
    if checkbox:
        todo.pop(index)
        functions.set_todo(todo)
        del st.session_state[i]
        st.rerun()



st.text_input(label="", placeholder="Enter a todo: ", on_change=addTodo, key="tbNewTodo")
