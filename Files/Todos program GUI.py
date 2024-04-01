import cfun
import PySimpleGUI as sg                  #imports custom GUI modual. 3rd party library
from typing import Any
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass
#Checks for todos file, if not present, file is created

sg.theme("Topanga")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")        #App user prompt
input_box = sg.InputText(tooltip="Enter todo", key="todo")
#Input text box. key=The dictonary key in window.read(). Key= is used to access the input box's contents in other code
add_button = sg.Button("Add")
list_box = sg.Listbox(values=cfun.get_todos(), key='todo_items', enable_events=True, size=[45, 10])
#Creates a list box and populates it with todos.txt. key=Used to access the contents of the list
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('To-Do App',
                   layout=[[clock],
                            [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))
                   #Each set of brackets=Another horizontal row
while True:
#Keeps the window open
    event, values = window.read(timeout=600)
    #Timeout is for the clock refresh
    window["clock"].update(value=time.strftime("%b %d, %Y"))
    #Multiple variables can be used with tuples. window.read outputs a dictonary.
    # #Event=Interface button, values=dictonary

    match event:
    #Maps the buttons to a function
        case "Add":
        #Add button functionality
            todos = cfun.get_todos()
            new_todo = values['todo'] + "\n"
            #selects the dictonary key 'todo' from the input_box.
            todos.append(new_todo)
            #appends the user input to todos as a dictonary from new_todo
            cfun.write_todos(todos)
            #writes the data to a file
            window["todo_items"].update(values=todos)
            #Updates the window after the item is added to the list
        case "Edit":
            popup_layout = [
                        [sg.Text("Enter new todo:")],
                        [sg.InputText(key='new_todo')],
                        [sg.Button('OK'), sg.Button('Cancel')]
                                                            ]
            popup_window: sg.Window = sg.Window('Edit Todo', popup_layout) # type: Any
            #Added popup window when clicking Edit
            todo_items = values['todo_items'] if 'todo_items' in values else []
            if todo_items:                 # Check if todo_items is not empty
                todo_edit = todo_items[0]  # Extract the first item from the list

                popup_event, popup_values = popup_window.read()

                if popup_event == 'OK':

                    new_todo = popup_values['new_todo'] + "\n"
                    #todo=input box, todo_items=List window
                    todos = cfun.get_todos()
                    index = todos.index(todo_edit)
                    #Locates the specified item in 'todo_items'
                    todos[index] = new_todo
                    #Updates the item in the todos list
                    cfun.write_todos(todos)
                    window["todo_items"].update(values=todos)
                    #Updates the window after the item is edited
                    popup_window.close()
                elif popup_event == 'Cancel':
                    popup_window.close()
                    pass
            else:
                sg.popup("Please select a todo item to edit.", font=("Helvetica", 12))


        case "Complete":
            try:
                todo_to_complete = values['todo_items'][0]
                todos = cfun.get_todos()
                # Gets a list from values, and grabs the todos.txt file
                todos.remove(todo_to_complete)
                cfun.write_todos(todos)
                #Removes the selected item from the todos_items list, writes the updated list to the file
                window['todo_items'].update(values=todos)
                window['todo'].update(value='')
                #Updates the item list window, and removes the item name from the input box
            except IndexError:
                sg.popup("Please select a todo item to complete.", font=("Helvetica", 12))
        case "Exit":
            break
        case "todo_items":
            window['todo'].update(value=values['todo_items'][0])
            #Displays the item in the input box when clicked
        case sg.WIN_CLOSED:
            #closes the window
            break

window.close()



