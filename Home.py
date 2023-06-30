import streamlit
import streamlit as sl
import todosModule

todos = todosModule.getTodo()
def addTodo():
    todo = sl.session_state["new_todo"]
    print(todo)
    todos.append(todo+"\n")
    todosModule.addTodo(todos)

sl.set_page_config(layout="wide")

sl.title("Todos Today")
sl.subheader("Todos app")
sl.write("This app is to <b>increase</b> your <b>efficiency</b> and <b>productivity</b>",
         unsafe_allow_html=True)

sl.text_input(label="Enter a To do",placeholder="Add new todo ...",on_change=addTodo,key="new_todo")
for index,todo in enumerate(todos) :
    checkbox = sl.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        todosModule.addTodo(todos)
        del sl.session_state[todo]
        sl.experimental_rerun()

#sl.session_state








#for todo in todos :
#    sl.checkbox(todo)
#.streamlit.text_input(label="",placeholder="Enter todo ...",on_change=addTodo(),key='new_todo')

