from pymongo import MongoClient

myclt = MongoClient("mongodb://localhost:27017")
mydb = myclt["mongotest"]
mycol = mydb["users"]

class DBmongo:
    def __init__(self):
        pass

    # insert in table
    def insert_user(self,userid,username,phone):
        data = {
            "userId":userid,
            "userName":username,
            "phone":phone
        }
        mycol.insert_one(data)
        print("User inserted in database!")

    # fetch_all
    def find_all(self):
        c = mycol.find()
        for i in c:
            print(i)

    # fetch_one
    def find_one(self,ids):
        query = {
            "userId":ids
        }
        c = mycol.find(query)
        for i in c:
            print(i)
    
    # delete users
    def delete_user(self,userId):
        query = {
            "userId":userId
        }
        c = mycol.delete_one(query)
        print("Record Deleted!",c)

    # update users
    def update_user(self,userId,newName,newPhone):
        data = {
            "userId":userId
        }
        udata = {
            "userId":userId,
            "newName":newName,
            "newPhone":newPhone
        }
        c = mycol.replace_one(data,udata)
        print("User Updated!",c)