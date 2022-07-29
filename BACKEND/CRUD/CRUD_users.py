from BACKEND.MODELS.User import User
from BACKEND.CRUD.CRUD_local_storage import CrudLocalStorage


def createUser(user):
    userRecorded = User(user['Nombre'], user['Manilla'], user['Tiempo'], user['Acudiente'],
                        user['ID-Acudiente'], user['Dinero'], user['Pagado'], user['Usuario VIP'])
    CrudLocalStorage.saveUser(userRecorded)
    print("Total de usuarios -> ", CrudLocalStorage.getUsers())


def getAttribute(userObject, attr):
    if isinstance(userObject, User):
        if attr == "name":
            return userObject.name
        elif attr == "braceletNumber":
            return userObject.braceletNumber
        elif attr == "totalTime":
            return userObject.totalTime
        elif attr == "parent":
            return userObject.parent
        elif attr == "parentID":
            return userObject.parentID
        elif attr == "money":
            return userObject.money
        elif attr == "payed":
            return userObject.payed
        elif attr == "vipUser":
            return userObject.vipUser

# self.searchRecordParameterComboBox.setItemText(0, _translate("mainWindow", "Seleccionar"))
#         self.searchRecordParameterComboBox.setItemText(1, _translate("mainWindow", "Index"))
#         self.searchRecordParameterComboBox.setItemText(2, _translate("mainWindow", "Nombre"))
#         self.searchRecordParameterComboBox.setItemText(3, _translate("mainWindow", "No. manilla"))
#         self.searchRecordParameterComboBox.setItemText(4, _translate("mainWindow", "Tiempo total"))
#         self.searchRecordParameterComboBox.setItemText(5, _translate("mainWindow", "Hora entrada"))
#         self.searchRecordParameterComboBox.setItemText(6, _translate("mainWindow", "Hora salida"))
#         self.searchRecordParameterComboBox.setItemText(7, _translate("mainWindow", "Sale"))
#         self.searchRecordParameterComboBox.setItemText(8, _translate("mainWindow", "Valor a pagar"))
#         self.searchRecordParameterComboBox.setItemText(9, _translate("mainWindow", "Cancelado"))
#         self.searchRecordParameterComboBox.setItemText(10, _translate("mainWindow", "Acudiente"))
#         self.searchRecordParameterComboBox.setItemText(11, _translate("mainWindow", "Acudiente-ID"))
#         self.searchRecordParameterComboBox.setItemText(12, _translate("mainWindow", "Listar"))

# def searchUsersByParams(value, param):
#     users = CrudLocalStorage.getUsers()
#     foundedUsers = []
#     for user in users:
#         if getAttribute(user,param)


# TODO: Left doing setAttribute(userObject, attr)
# TODO: Left doing searchUsersByParams
#Notes: (Spanish) para la función de buscar usuarios por params, creo que es mejor definir atributos como hora de entrada
# y hora de salida, sale, y cancelado propios para User(), esto me permitirá hacer la busqueda de manera mas integra. Por otra parte
# debo de encontrar una manera de renombrar los params de manera tal que pueda acceder a los getters de Users().