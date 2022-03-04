from controllers import *

class Views:
    
    def __init__(self):
        self.mainMenuOptions = {1 : self.loginForm,
                                2 : self.createUserForm,
                                3 : print("Bye bye !")}


    def mainMenu(self):
        choice = int(input("************************ Menu ************************\n\n\
                            1 => Login\n\
                            2 => Create your profile\n\
                            3 => Quit\n\
                            Your choice ? "))
        while choice not in [1,2,3]:
            choice = int(input("************************ Menu ************************\n\n\
                            1 => Login\n\
                            2 => Create your profile\n\
                            3 => Quit\n\
                            Please select 1, 2 or 3"))
        















controller = Controllers()
views = Views()

views.mainMenu()