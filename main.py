import click
from src.db import create_table, seed_db
from src.app import App


@click.group()
def main():
    pass

@main.command()
def init_db():
    """Creates table and seeds it"""
    #create_table()
    seed_db()
    

@main.command()
def run():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    main()

# from tkinter import *
# import mysql.connector



# def connect_to_db():
#     return mysql.connector.connect(
#         host='localhost',
#         user='root',
#         database ='nice_bank',
#         password='Apple1!'
#     )



# if __name__ == '__main__':
#     connection = connect_to_db()
#     cursor = connection.cursor()
#     userdata_table = "SELECT * FROM user"
    
#     cursor.execute(userdata_table)

    
    

#     def addingaccount(firstname,lastname,birthday,address,balance, pincode, username, password):
#         """
#         INSERT INTO user(firstname,lastname,birthday,address,balance,pincode,username,password)
#         VALUES (?,?,?,?,?,?,?,?)
#         """,(firstname,lastname,birthday,address,balance,pincode,username,password)
        

#     accountchoices = input("Will you, create account, login, or delete a account?")
    
#     if accountchoices == "create account":
        
#         firstnamecreate = input("what is your first name \n")
#         lastnamecreate = input("what is your last name \n")
#         birthdaycreate = input("what is your birthdate \n")
#         addresscreate = input("what is your address \n")
#         balancecreate = input("what would you like to set your balance at \n")
#         pincodecreate = input("create a pincode \n")
#         usernamecreate = input("Make your username\n")
#         passwordcreate = input("Make your password")
#         cursor.execute(addingaccount(firstnamecreate,lastnamecreate,birthdaycreate,addresscreate,balancecreate,pincodecreate,usernamecreate,passwordcreate))
        
#         # cursor.execute(addingaccount(firstnamecreate,lastnamecreate,birthdaycreate,addresscreate,balancecreate,pincodecreate))
#         #print(addingaccount(firstnamecreate,lastnamecreate,birthdaycreate,addresscreate,balancecreate,pincodecreate))
#         print()
        
        


#     for x in cursor:
#         print(x)
#     connection.commit()
#     cursor.close()
    
#     connection.close()
    


# root = Tk()

# myLabel = Label(root, text="Hello World! To the menu! currently working on general code, this is now an example UI for now")
# usernameLabel = Label(root,text="Username: ")
# usernameInput=Entry(root,text="Username!!", borderwidth=5)

# passwordLabel = Label(root,text="Password: ")
# passwordInput=Entry(root,text="Password!!", borderwidth=5)

# loginButton = Button(root,text="Login", bg="lightblue",)
# createaccountButton = Button(root,text="Create account", bg="lightblue",)


# myLabel.grid(row=0,column=0)
# usernameLabel.grid(row=1,column=1)
# usernameInput.grid(row=1,column=2)
# passwordLabel.grid(row=2,column=1)
# passwordInput.grid(row=2,column=2)
# loginButton.grid(row=5,column=1)
# createaccountButton.grid(row=6,column=1)





# root.mainloop()



# print("Hello World")