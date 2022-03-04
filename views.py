from controllers import *
import json

class Views:
    def __init__(self):
        self.controller = Controllers()
    
    def mainMenu(self):
        
        choice = input("\n****************** Menu ******************\n\n\
                1 => Login\n\n\
                2 => Create your profile\n\n\
                3 => Quit\n\n\
                Your choice ? ")

        while choice not in ["1","2","3"]:
            choice = input("\n****************** Menu ******************\n\n\
                            1 => Login\n\
                            2 => Create your profile\n\
                            3 => Quit\n\
                            Please select 1, 2 or 3")

        if choice == "1":
            self.loginForm()

        elif choice == "2":
            self.createUserForm()

        else:
            print("Bye bye !")


    def menuUser(self):
        pass
        
    def loginForm(self):
        name = input("\n\n****************** Login ******************\n\n\
                Name => ")
        password = input("\n\
                Password => ")
        with open("datas.json") as fp:
            listdata = json.load(fp)
        

        
    def validPassword(self,ps1, ps2):
        result = False
        if ps1 == ps2:
            if len(ps1) < 8:
                print("\nPassword too short .. (Min. 8 characters)")
            elif ps1.isalpha():
                print("\nPlease add at least one number to secure your password")
            else:
                result = True
        else:
            print("\nInvalid Confirmation")
        return result

    def createUserForm(self):
        name = input("\n\n****************** Create your profile ******************\n\n\
                Name => ")
        password1 = input("\n\
                Password => ")
        password2 = input("\n\
                Confirm you password => ")
        while  self.validPassword(password1, password2) == False:
            password1 = input("\n\
                Password => ")
            password2 = input("\n\
                Confirm you password => ")
        company = input("\n\
                Company (optional, press ENTER) => ")
        email = input("\n\
                Email address (optional, press ENTER) => ")
        phone_number = input("\n\
                Phone Number (optional, press ENTER) => ")
        
        self.controller.createUser(name, password1, company, email, phone_number)
        self.menuUser()
        















controller = Controllers()
views = Views()

views.mainMenu()