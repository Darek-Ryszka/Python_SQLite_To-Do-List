import sqlite3

connection = sqlite3.connect("todo.db")


def create_table(connection):
    pass


def show_tasks(connection):
    pass


def add_task(connection):
    pass


def delete_task(connection):
    pass


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
