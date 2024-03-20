import cfun                            #Imports custom functions from a file
import time                            #Imports built in time functions



now = time.strftime("%b %d, %Y")
print("Today is", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()      #Removes leading and trailing spaces

    if user_action.startswith("add"):  # Looks for a string that "starts with" add

        todo = user_action[4:] + "\n"  # String stripping. Strips out the first 4 characters of the input
        todos = cfun.get_todos()            # Custom function to open todos.txt in read mode
        todos.append(todo)             # appends the input to the todos.txt file

        cfun.write_todos(todos)             #Custom function to open todos.txt in write mode

    elif user_action.startswith("show"):

        todos = cfun.get_todos()

        for index, item in enumerate(todos):  # /Access' the index number, and item in 'todos'
            item = item.strip('\n')  # /strips the extra carriage return from the printout
            row = f"{index + 1}-{item}"  # /Sets the list numbers starting from 1 instead of 0
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1
            todos = cfun.get_todos()

            new_todo = input("Enter a new todo: ")
            todos[number] = new_todo + ('\n')

            cfun.write_todos(todos)
        except ValueError:
            print("Command not valid")
            continue
        # error handling

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])  # strips the first 9 chars from the input

            todos = cfun.get_todos()  # custom read file function
            index = number - 1
            todos_complete = todos[index].strip('\n')  # Strips the leading and trailing spaces
            todos.pop(index)  # removes the item selected by user_action

            cfun.write_todos(todos)

            message = f"Removed {todos_complete} from the list."
            print(message)
        except IndexError:
            print("No item with that number")
            continue
        # error handling


    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid Command")

print("Goodbye!")
