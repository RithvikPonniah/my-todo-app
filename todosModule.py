def writeToFile(todos, filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    with open(filePath, 'w') as fObject:
        fObject.writelines(todos)


def getTodo(filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    with open(filePath, 'r') as fObject:
        dodo = fObject.readlines()
    return dodo


def addTodo(todoItem, filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    with open(filePath, 'w') as fObject:
        fObject.writelines(todoItem)


def editTodo(todoNumber, filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    try:
        todos = getTodo()
        x = input("Enter the new value of the todo items: ") + '\n'
        z = todos[todoNumber - 1]
        todos[todoNumber - 1] = x
        writeToFile(todos)
        z = z.strip('\n')
        x = x.strip('\n')
        print(f"You have changed '{z}' into '{x}'")
    except IndexError:
        print("The given todo number ", todoNumber, 'does not exist')


def completeTodo(todoNumber, filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    try:
        todos = getTodo(filePath)
        todos.pop(todoNumber - 1)
        writeToFile(todos, filePath)
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}.{item}"
            print(row)
        return
    except IndexError:
        print('The Index you have given is invalid')


def showTodo(filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    todos = getTodo(filePath)
    for index, item in enumerate(todos):
        # x = x + 1
        item = item.strip('\n')
        row = f"{index + 1}.{item}"
        print(row)


def clearTodo(filePath='/Users/rajap/Documents/GitHub/RithvikPonniah.github.io/20Apps/todos.txt'):
    clear = input("Are you sure you want to clear all your todos ? press  'y' to confirm ").strip()
    if clear == "y":
        todos = []
        writeToFile(todos, filePath)


if __name__ == '__main__':
    print(__name__)
    print("Burgundi")
