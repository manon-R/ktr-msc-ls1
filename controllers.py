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
        json_user = json.dumps(new_user.serializedUser())

        with open("datas.json", "w") as datafile:
            datafile.write(json_user)

        print(f"User {name} successfully created !") #or return ?

    def loginUser(self):
        pass

    def createBusinessCard(self,user:User ,email, name, company, phoneNumber): #Current user
        new_card = BusinessCard(email,name, company, phoneNumber)
        json_card = json.dumps(new_card.serializedBusinessCard())

        user.library.append(new_card)
        json_user = user.serializedUser()
        with open("datas.json", "w") as datafile:
            datafile.write(json_card)
            datafile.write(json_user)

        print(f"New card successfully created and added to your library !")


