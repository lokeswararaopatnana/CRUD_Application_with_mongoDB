from mongostore import DBmongo

def app():
    db =DBmongo()

    while True:
        print("******Welcome to CRUD******")
        print("""\tPress 1 to Insert New User \n
        Press 2 to Display All Users \n
        Press 3 to Display One User \n
        Press 4 to Update a User \n
        Press 5 to Delete a User \n
        Press 6 to Exit the CRUD App
        """)
        try:
            option = int(input("Select Any One Option:"))
            if(option == 1):
                # insert user
                uid = int(input("Enter UserId:"))
                uname = input("Enter UserName:")
                uphone = input("Enter UserPhone:")
                db.insert_user(uid,uname,uphone)

            elif(option == 2):
                # display all users
                db.find_all()
            
            elif(option == 3):
                # display one user
                uid = int(input("Enter UserId:"))
                db.find_one(uid)
                pass

            elif(option == 4):
                # update a user
                uid = int(input("Enter user to update:"))
                uname = input("Enter new User Name:")
                uphone = input("Enter new User Phone:")
                db.update_user(uid,uname,uphone)
                pass

            elif(option == 5):
                # delete a user
                uid = int(input("Enter UserId to delete:"))
                db.delete_user(uid)
                pass

            elif(option == 6):
                # to exit the program
                break

            else:
                print("Invalid input ! Try again!")
        except Exception as e:
            print(e)
            print("Invalid datails ! Try again !")

if __name__ == "__main__":
    app()