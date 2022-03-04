class User:

    def __init__(self, name:str, password:str, companyName=None, email=None, phoneNumber=None) -> None:
        self.name = name
        self.password = password
        self.companyName = companyName
        self.email = email
        self.phoneNumber = phoneNumber
        self.library = []

    def __str__(self):
        return f"Username => {self.name}"

    def serializedUser(self):
        return {"name":self.name,
                "password":self.password,
                "companyName":self.companyName,
                "email": self.email,
                "phoneNumber": self.phoneNumber,
                "library":self.library}
                


class BusinessCard:
    
    def __init__(self, email:str, name = None, company = None, phoneNumber = None):
        self.email = email
        self.name = name
        self.company = company
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"Business Card email => {self.email}"

    def serializedBusinessCard(self):
        return {"email":self.email,
                "name":self.name,
                "company":self.company,
                "phoneNumber": self.phoneNumber}
