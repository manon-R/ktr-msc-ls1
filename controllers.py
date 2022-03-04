from models import *
import json
import hashlib

class Controllers():

    def hashPassword(self, password:str):
        secure_password = hashlib.sha256(str.encode(password)).hexdigest()
        return secure_password

    def createUser(self,name, password, companyName, email, phoneNumber):
        new_password = self.hashPassword(password)
        new_user = User(name, new_password, companyName, email, phoneNumber)
        

        with open("datas.json") as fp:
            listdata = json.load(fp)

        
        listdata[name] = new_user.serializedUser()
 
        with open("datas.json", "w") as datafile:
            json.dump(listdata, datafile) 

        print(f"User {name} successfully created !") #or return ?
        
        return new_user.serializedUser()


    def createBusinessCard(self, currentUser,email, name, company, phoneNumber): #Current user
        new_card = BusinessCard(email,name, company, phoneNumber)

        currentUser["library"].append(new_card.serializedBusinessCard())
        
        with open("datas.json") as fp:
            listdata = json.load(fp)

        listdata[currentUser["name"]] = currentUser
        listdata[email] = new_card.serializedBusinessCard()

        with open("datas.json", "w") as datafile:
            json.dump(listdata, datafile)
            


        print(f"New card successfully created and added to your library !")


