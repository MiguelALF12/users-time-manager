from BACKEND.MODELS.local_storage import LocalStorage
from BACKEND.MODELS.User import User


class CrudLocalStorage:
    storage = LocalStorage()

    @classmethod
    def saveUser(cls, userObject):
        if isinstance(userObject, User):
            CrudLocalStorage.storage.addUser(userObject)

    @classmethod
    def getUsers(cls):
        return CrudLocalStorage.storage.getUsers()

    @classmethod
    def setUsers(cls, newStorage):
        CrudLocalStorage.storage = newStorage

    @classmethod
    def getChange(cls):
        return CrudLocalStorage.storage.getChange()

    @classmethod
    def setChange(cls, newChange):
        CrudLocalStorage.storage.setChange(newChange)

# TODO: Remove left for implementation
# TODO: Is there any problem if a ledt all the functionality as a how this works?
