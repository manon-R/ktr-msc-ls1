from controllers import *
import json

class Views:
    def __init__(self):
        self.checkJsonFile()
        self.controller = Controllers()
        self.current_user = None
    
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


    def userMenu(self):
        print(f"\n\n ~ {self.current_user['name']} Workspace ~ ")
        choice = input("\n****************** Home ******************\n\n\
                1 => Add Business Card\n\n\
                2 => My library\n\n\
                3 => Logout\n\n\
                Your choice ? ")

        while choice not in ["1", "2", "3"]:
            choice = input("\n****************** Menu ******************\n\n\
                            1 => Add Business Card\n\
                            2 => My library\n\
                            3 => Logout\n\
                            Please select 1, 2 or 3")

        if choice == "1":
            self.businessCardForm()

        elif choice == "2":
            self.displayLibrary()

        else:
            print(f"Bye bye {self.current_user['name']}!")
            self.mainMenu()
        
    def loginForm(self):
        name = input("\n\n****************** Login ******************\n\n\
                Name => ")
        password = input("\n\
                Password => ")
        with open("datas.json") as fp:
            listdata = json.load(fp)
        if listdata[name]["password"] == self.controller.hashPassword(password): #Or in controllers ?
            self.current_user = listdata[name]
            print(f"\n\nWelcome {self.current_user['name']} ! ")
            self.userMenu()
        else:
            print("\nInvalid Name or Password")
            self.loginForm()
        

        
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
        
        self.current_user = self.controller.createUser(name, password1, company, email, phone_number)
        self.userMenu()
        
    def businessCardForm(self):
        email = input("\n\n****************** Create a new Business Card ******************\n\n\
                Email address => ")
        name = input("\n\
                Name (optional, press ENTER) => ")
        company = input("\n\
                Company (optional, press ENTER) => ")
    
        phone_number = input("\n\
                Phone Number (optional, press ENTER) => ")
        
        self.controller.createBusinessCard(self.current_user, email, name, company, phone_number)
        self.userMenu()

    def displayLibrary(self):
        if self.current_user["library"]:
            print("\n\n****************** Your Library ******************\n")
            for card in self.current_user["library"]:
                print(f"{card}\n")
        else:
            print("\n\nYour Library is empty... Let's go for looking for new working partners !")
        
        self.userMenu()
        

    def checkJsonFile(self):
        try:
            with open("datas.json") as fp:
                listdata = json.load(fp)
            pass
        except json.decoder.JSONDecodeError:
            with open("datas.json", "w") as datafile:
                json.dump({}, datafile) 







views = Views()

views.mainMenu()