from BACKEND.MODELS.local_storage import LocalStorage
from BACKEND.MODELS.User import User


class CrudLocalStorage:
    storage = LocalStorage()

    @classmethod
    def saveUser(cls, userObject):
        if isinstance(userObject, User):
            CrudLocalStorage.storage.addUser(userObject)

    @classmethod
    def getUser(cls, userObject):
        # if isinstance(userObject, User):
        #     CrudLocalStorage.storage.setUsers(userObject)
        pass

    @classmethod
    def getUsers(cls):
        return CrudLocalStorage.storage.getUsers()

# TODO: Remove left for implementation
# TODO: Modify getUser, need a way to fetch by all the searchParams
