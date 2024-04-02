FILEPATH = "files/todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of
    todo items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the todo items list into the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)



if __name__ == "__main__":
    print(get_todos())
#Executes code only if the script is run directly.
#Will not run if this script is imported into another file