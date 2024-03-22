import cfun
import PySimpleGUI as sg                  #imports custom GUI modual. 3rd party library

label = sg.Text("Type in a to-do")        #App user prompt
input_box = sg.InputText(tooltip="Enter todo", key="todo")
#Input text box. key=The dictonary key in window.read()
add_button = sg.Button("Add")

window = sg.Window('To-Do App',
                   layout=[[label],
                           [input_box, add_button]],
                   font=('Helvetica', 10))
                   #Each set of brackets=Another horizontal row
while True:
#Keeps the window open
    event, values = window.read()
    #Multiple variables can be used with tuples. window.read outputs a dictonary. Event=user input, values=dictonary
    print(event)
    print(values)
    match event:
        case "Add":
            todos = cfun.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            cfun.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()