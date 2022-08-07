from datetime import datetime, timedelta
import threading, time
import re
from random import randint #  Just for testing

from BACKEND.MODELS.User import User
from BACKEND.CRUD.CRUD_local_storage import CrudLocalStorage
from FRONTEND.views.constantsAndOthers import totalTimeConvertion


def createUser(user):
    userRecorded = User(user['Nombre'], user['Manilla'], user['Tiempo'], user['Acudiente'],
                        user['ID-Acudiente'], user['Dinero'], user['Pagado'], user['Usuario VIP'],
                        user['Hora entrada'], user['Hora salida'], user['Sale'])
    CrudLocalStorage.saveUser(userRecorded)
    assignIndexes(userRecorded)
    userRecordTime(userRecorded)
    calcExitTime(userRecorded)
    print("USUARIO GUARDADO CON EXITO. INDICE {} - HORA ENTRADA {} - HORA SALIDA {}".format(
        getAttribute(userRecorded, "index"),
        getAttribute(userRecorded, "entryHour").time(),
        getAttribute(userRecorded, "exitHour").time()))
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


def userRecordTime(userObject):
    entryTime = datetime.now()
    setAttribute(userObject, "entryHour", entryTime)


def calcExitTime(userObject):
    entryTime = getAttribute(userObject, "entryHour")
    totalTime = getAttribute(userObject, "totalTime")
    timeConvertions = totalTimeConvertion[totalTime]
    # timeToStay = timedelta(seconds=timeConvertions[2])
    secondsRandom = randint(5,25)
    timeToStay = timedelta(seconds= secondsRandom)
    exitTime = entryTime + timeToStay
    setAttribute(userObject, "exitHour", exitTime)

def usersWhoStay():
    return [user for user in CrudLocalStorage.getUsers() if not getAttribute(user, "userTimeDone")]

def startCounting():
    # TODO: How to implement changes?
    userIndex = 0
    while True:
        usersWhoStayObj = usersWhoStay()
        if len(CrudLocalStorage.getUsers()) > 0:
            if CrudLocalStorage.getChange(): # If True means there has been some changes
                #here would go the code related with edition view and functionality
                continue
            if userIndex < len(usersWhoStayObj):
                currentTime = datetime.now().time()
                userExitTime = getAttribute(usersWhoStayObj[userIndex],
                                            "exitHour").time()  # In string just to avoid miliseconds
                if userExitTime <= currentTime:  # when equals, means that the tme is up for that user.
                    print(f"USUARIO CON INDICE {userIndex} POR SALIR")
                    setAttribute(usersWhoStayObj[userIndex], "userTimeDone", True)
                userIndex += 1
            else:
                userIndex = 0
        else:
            print("DURMIENDO")
            userIndex = 0
            time.sleep(10)  # we wait for 30 seconds to see if there are users in order to
            # proceed with the time comparison


def startCountingThread():
    countingThread = threading.Thread(target=startCounting)
    countingThread.start()
