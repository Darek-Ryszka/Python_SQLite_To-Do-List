import sqlite3

connection = sqlite3.connect("todo.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass


def show_tasks(connection):
    pass


def add_task(connection):
    print("We add a task")
    task = input("The content of the task: ")
    if task == "0":
        print("Return to menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
        print("Task added!")


def delete_task(connection):
    pass


create_table(connection)

while True:
    print()
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Delete tasks")
    print("4. Exit")

    user_choice = int(input("Choose a number: "))
    print()

    if user_choice == 1:
        show_tasks(connection)

    if user_choice == 2:
        add_task(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break
