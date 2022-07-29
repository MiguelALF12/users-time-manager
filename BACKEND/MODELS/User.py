
DEFAULT_USER_TIME_PRICES = {
    '15 minutos': 8000,
    '30 minutos': 14000,
    '1 hora': 18000,
    '2 horas': 32000,
}

VIP_USER_TIME_PRICES = {
    '15 minutos': 8000,
    '30 minutos': 11500,
    '1 hora': 14500,
    '2 horas': 32000,
}

class User:
    def __init__(self, name, braceletNumber, totalTime, parent, parentID, money, payed, vipUser):
        self.__name = name
        self.__braceletNumber = braceletNumber
        self.__totalTime = totalTime
        self.__parent = parent
        self.__parentID = parentID
        self.__money = money
        self.__payed = payed
        self.__vipUser = vipUser

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

