
""" para regresar a la variable el contenido que hay en un txr usando with"""
from fileinput import close
FILEPATH = "todo.txt"

def get_todo(filepath=FILEPATH):
    with open(filepath, 'r') as file:
        todoLocal = file.readlines()
        return(todoLocal)


""" para agregar al txt contenido de la variable usando with"""
def set_todo(todoLocal, filepath=FILEPATH):
    with open(filepath, 'w') as file:
        file.writelines(todoLocal)


"""Para que se imprima solo cuando se ejecuta desde aqui , no desde otro py que lo llame."""
if __name__ == "__main__":
    print("Helo")
    print(get_todo())

