

class User:

    def __init__(self, name, braceletNumber, totalTime, parent, parentID, money, payed, vipUser,
                 entryHour, exitHour, userTimeDone):
        self.__index = 0  # Default value
        self.__name = name
        self.__braceletNumber = braceletNumber
        self.__totalTime = totalTime
        self.__parent = parent
        self.__parentID = parentID
        self.__money = money
        self.__payed = payed
        self.__vipUser = vipUser
        self.__entryHour = entryHour
        self.__exitHour = exitHour
        self.__userTimeDone = userTimeDone

    @property
    def index(self):
        return self.__index

    @index.setter
    def index(self, newIndex):
        self.__index = newIndex

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, newName):
        self.__name = newName

    @property
    def braceletNumber(self):
        return self.__braceletNumber

    @braceletNumber.setter
    def braceletNumber(self, newBraceletNumber):
        self.__name = newBraceletNumber

    @property
    def totalTime(self):
        return self.__totalTime

    @totalTime.setter
    def totalTime(self, newTotalTime):
        self.__totalTime = newTotalTime

    @property
    def parent(self):
        return self.__parent

    @parent.setter
    def parent(self, newParent):
        self.__parent = newParent

    @property
    def parentID(self):
        return self.__parentID

    @parentID.setter
    def parentID(self, newParentID):
        self.__parentID = newParentID

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, newMoney):
        self.__money = newMoney

    @property
    def payed(self):
        return self.__payed

    @payed.setter
    def payed(self, newPayed):
        self.__payed = newPayed

    @property
    def vipUser(self):
        return self.__vipUser

    @vipUser.setter
    def vipUser(self, newVipUser):
        self.__vipUser = newVipUser

    @property
    def entryHour(self):
        return self.__entryHour

    @entryHour.setter
    def entryHour(self, newEntryHour):
        self.__entryHour = newEntryHour

    @property
    def exitHour(self):
        return self.__exitHour

    @exitHour.setter
    def exitHour(self, newExitHour):
        self.__exitHour = newExitHour

    @property
    def userTimeDone(self):
        return self.__userTimeDone

    @userTimeDone.setter
    def userTimeDone(self, newUserTimeDone):
        self.__userTimeDone = newUserTimeDone
