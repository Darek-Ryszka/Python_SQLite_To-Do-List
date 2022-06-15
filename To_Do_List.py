import sqlite3

connection = sqlite3.connect("todo.db")

while True:
    print()
    print("1. Show tasks")
    print("2. Add tasks")
    print("3. Delete tasks")
    print("4. Exit")

    user_choice = int(input("Choose a number: "))
    print()
