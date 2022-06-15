import sqlite3

connection = sqlite3.connect("todo.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass


def show_tasks(connection):
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(str(row[0]) + " - " + row[1])


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
    task_index = int(input("Enter task id to delete: "))

    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    connection.commit()

    if rows_deleted == 0:
        print("Error! This task does not exist!")
    else:
        print("Task delete!")


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

connection.close()
