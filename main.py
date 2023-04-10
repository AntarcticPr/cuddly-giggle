from tkinter import *
import mysql.connector

def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Apple1!'
    )

if __name__ == '__main__':
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)
    cursor.close()
    connection.close()

root = Tk()

myLabel = Label(root, text="Hello World! To the menu!")

myLabel.pack()

root.mainloop()

print("Hello World")