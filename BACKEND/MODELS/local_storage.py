class LocalStorage:
    users = list()

    @classmethod
    def getUsers(cls):
        return LocalStorage.users

    @classmethod
    def addUser(cls, userObject):
        LocalStorage.users.append(userObject)

