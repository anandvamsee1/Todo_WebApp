FILEPATH = "todo_lst.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of todo_items
    """
    with open(filepath, 'r') as file_local:
        todo_lst_local = file_local.readlines()
    return todo_lst_local


def write_todos(todo_item, filepath=FILEPATH):
    """
    Write the list of items to a text file
    """
    with open(filepath, 'w') as filewrite_local:
        filewrite_local.writelines(todo_item)


print(type(__name__))
print(__name__)

if __name__ == "__main__":
    print("Executed only when the functions script is executed directly")
    print(get_todos())
