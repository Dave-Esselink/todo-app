import cfun
import PySimpleGUI as sg                  #imports custom GUI modual. 3rd party library

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
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 10))
                   #Each set of brackets=Another horizontal row
while True:
#Keeps the window open
    event, values = window.read()
    #Multiple variables can be used with tuples. window.read outputs a dictonary.
    # #Event=Interface button, values=dictonary
    print(event)
    print(values)
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
            todo_edit = values['todo_items'][0]
            new_todo = values['todo'] + "\n"
            #todo=input box, todo_items=List window
            todos = cfun.get_todos()
            index = todos.index(todo_edit)
            #Locates the specified item in 'todo_items'
            todos[index] = new_todo
            #Updates the item in the todos list
            cfun.write_todos(todos)
            window["todo_items"].update(values=todos)
            #Updates the window after the item is edited
        case "Complete":
            todo_to_complete = values['todo_items'][0]
            todos = cfun.get_todos()
            # Gets a list from values, and grabs the todos.txt file
            todos.remove(todo_to_complete)
            cfun.write_todos(todos)
            #Removes the selected item from the todos_items list, writes the updated list to the file
            window['todo_items'].update(values=todos)
            window['todo'].update(value='')
            #Updates the item list window, and removes the item name from the input box

        case "Exit":
            break
        case "todo_items":
            window['todo'].update(value=values['todo_items'][0])
            #Displays the item in the input box when clicked
        case sg.WIN_CLOSED:
            #closes the window
            break

window.close()



