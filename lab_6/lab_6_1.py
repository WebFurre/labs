class UserAccount:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.__password = password
    def set_password(self, new_password):
        self.__password = new_password
    def check_password(self, password):
        if self.__password == password:
            return True
        else:
            return False

user = UserAccount("Roman","webfurre@gmail.com","1234")
user.set_password("5678")
if user.check_password("1234"):
    print("вверный пароль")
else:
    print("невверный пароль")
if user.check_password("5678"):
    print("вверный пароль")
else:
    print("невверный пароль")