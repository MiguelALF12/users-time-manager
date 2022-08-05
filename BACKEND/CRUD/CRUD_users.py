from BACKEND.MODELS.User import User
from BACKEND.CRUD.CRUD_local_storage import CrudLocalStorage
import re


def createUser(user):
    userRecorded = User(user['Nombre'], user['Manilla'], user['Tiempo'], user['Acudiente'],
                        user['ID-Acudiente'], user['Dinero'], user['Pagado'], user['Usuario VIP'],
                        user['Hora entrada'], user['Hora salida'], user['Sale'])
    CrudLocalStorage.saveUser(userRecorded)
    assignIndexes(userRecorded)
    print("Usuario indexado con éxito -> ", getAttribute(userRecorded, "index"))
    print("Total de usuarios -> ", CrudLocalStorage.getUsers())


def getAttribute(userObject, attr):
    if isinstance(userObject, User):
        # There two options because of the search function, in order to make it easier for it
        if attr == "index" or attr == "Index":
            return userObject.index
        elif attr == "name" or attr == "Nombre":
            return userObject.name
        elif attr == "braceletNumber" or attr == "No. manilla":
            return userObject.braceletNumber
        elif attr == "totalTime" or attr == "Tiempo total":
            return userObject.totalTime
        elif attr == "parent" or attr == "Acudiente":
            return userObject.parent
        elif attr == "parentID" or attr == "Acudiente-ID":
            return userObject.parentID
        elif attr == "money" or attr == "Valor a pagar":
            return userObject.money
        elif attr == "payed" or attr == "Cancelado":
            return userObject.payed
        elif attr == "vipUser" or attr == "Usuario VIP":  # TODO: need to add this to comboBox
            return userObject.vipUser
        elif attr == "entryHour" or attr == "Hora entrada":
            return userObject.entryHour
        elif attr == "exitHour" or attr == "Hora salida":
            return userObject.exitHour
        elif attr == "userTimeDone" or attr == "Sale":
            return userObject.userTimeDone


def setAttribute(userObject, attr, newValue):
    if isinstance(userObject, User):
        # There two options because of the search function, in order to make it easier for it
        if attr == "index" or attr == "Index":
            userObject.index = newValue
        elif attr == "name" or attr == "Nombre":
            userObject.name = newValue
        elif attr == "braceletNumber" or attr == "No. manilla":
            userObject.braceletNumber = newValue
        elif attr == "totalTime" or attr == "Tiempo total":
            userObject.totalTime = newValue
        elif attr == "parent" or attr == "Acudiente":
            userObject.parent = newValue
        elif attr == "parentID" or attr == "Acudiente-ID":
            userObject.parentID = newValue
        elif attr == "money" or attr == "Valor a pagar":
            userObject.money = newValue
        elif attr == "payed" or attr == "Cancelado":
            userObject.payed = newValue
        elif attr == "vipUser" or attr == "Usuario VIP":  # TODO: need to add this to comboBox
            userObject.vipUser = newValue
        elif attr == "entryHour" or attr == "Hora entrada":
            userObject.entryHour = newValue
        elif attr == "exitHour" or attr == "Hora salida":
            userObject.exitHour = newValue
        elif attr == "userTimeDone" or attr == "Sale":
            userObject.userTimeDone = newValue


def searchUsersByParams(value, param, **kwargs):
    users = CrudLocalStorage.getUsers()
    foundedUsers = []
    exactSearchPattern = r'[\w.-]+|([\w .-]+)+'  # This regex refers to everycase whenever the search value takes
    for user in users:  # a form either this 'Miguel lopez' or this 'Miguel'.
        userAttribute = str(getAttribute(user, param)).lower()  # The old one was [\w.-]+ [\w.-]+|[\w.-]+
        # TODO: How can i improve this conditional?
        # TODO: For Payed and Sale, they could go as yes or no values for search input
        # Check for good patterns
        if re.search(exactSearchPattern, value):
            if userAttribute == value.lower() or value.lower() in userAttribute:
                foundedUsers.append(user)
    return foundedUsers


# TODO: The search is made just by clicking, so we will have all the values at once, and need juts the idnex
# def searchUsersByValue():
#     users = CrudLocalStorage.getUsers()
#     foundedUser = None
#     exactSearchPattern = r'[\w.-]+|([\w .-]+)+'
#     for user in users:
#         userAttributes = [attrValue for attrValue in user.get]
# Other functions

def evacuateUser(userIndex):
    users = CrudLocalStorage.getUsers()
    for user in users:
        if userIndex == getAttribute(user, "index"):
            users.remove(user)
    print("-----------------(CRUD_USERS) PROCESO DE ELIMINACIÓN EXITOSO !!-----------------")
def updateIndexes():
    users = CrudLocalStorage.getUsers()
    newIndex = 0
    for user in users:
        setAttribute(user, "index", newIndex)
        newIndex += 1

def calcTotalMoney(data):
    totalMoney = 0
    for user in data:
        totalMoney += getAttribute(user, "money")
    return totalMoney


def assignIndexes(userObject):
    users = CrudLocalStorage.getUsers()
    if isinstance(userObject, User):
        if len(users) > 1:
            lastUser = users[len(users) - 2]
            lastUserIndex = getAttribute(lastUser, "index")
            indexToAssign = lastUserIndex + 1
            setAttribute(userObject, "index", indexToAssign)
