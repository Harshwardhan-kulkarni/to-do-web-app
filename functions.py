FILEPATH = "C:/Users/Harshwardhankulkarni/OneDrive/python/Project1-webapp/todos.txt"


def get_todos(filepath=FILEPATH):
    """ read a text file and return the items
    existing items in list form """

    with open(filepath, 'r') as file_local:
        texts_local = file_local.readlines()
    return texts_local


def write_text(texts_arg, filepath=FILEPATH):
    """ opens a text file and write to-do items in it"""
    with open(filepath, "w") as file:
        file.writelines(texts_arg)
