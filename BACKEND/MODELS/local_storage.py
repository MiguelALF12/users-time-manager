import threading
class LocalStorage:
    users = list()
    change = bool()  # This allows us to check whenever a change is made.

    @classmethod
    def getUsers(cls):
        return LocalStorage.users

    @classmethod
    def addUser(cls, userObject):
        LocalStorage.users.append(userObject)

    @classmethod
    def getChange(cls):
        return LocalStorage.change

    @classmethod
    def setChange(cls, newChange):
        LocalStorage.change = newChange




