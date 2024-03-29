# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/miguellopez/Desktop/PROYECTS/PAGOS/ARENERO-RAMIRO/FRONTEND/views/QT_DESIGNS/designs/evacuateConfirmationDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FRONTEND import evacuateConfirmationAccept, evacuateConfirmationDeny
from BACKEND.CRUD.CRUD_users import evacuateUser, updateIndexes
class UiForm(object):
    formInstance = None

    def setupUi(self, Form, deleteUserSpecs):
        Form.setObjectName("Form")
        Form.resize(428, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(428, 200))
        Form.setMaximumSize(QtCore.QSize(428, 200))
        Form.setStyleSheet("background-color: rgb(169, 201, 202);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMinimumSize(QtCore.QSize(404, 0))
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.titleLabel.setFont(font)
        self.titleLabel.setScaledContents(False)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setWordWrap(True)
        self.titleLabel.setObjectName("titleLabel")
        self.titleLabel.setStyleSheet("color:#000000;")
        self.verticalLayout.addWidget(self.titleLabel)
        self.messageLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.messageLabel.setFont(font)
        self.messageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.messageLabel.setWordWrap(True)
        self.messageLabel.setObjectName("messageLabel")
        self.messageLabel.setStyleSheet("color:#000000;")
        self.verticalLayout.addWidget(self.messageLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.acceptConfirmEvacuatePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptConfirmEvacuatePushButton.sizePolicy().hasHeightForWidth())
        self.acceptConfirmEvacuatePushButton.setSizePolicy(sizePolicy)
        self.acceptConfirmEvacuatePushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.acceptConfirmEvacuatePushButton.setFont(font)
        self.acceptConfirmEvacuatePushButton.setStyleSheet("QPushButton{\n"
"    padding: 0px 10px 0px 10px;\n"
"    background: #e0d1bd;\n"
"    color: #232323;\n"
"    border:1px rounded #232323;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(163, 111, 61);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218);\n"
"    }")
        self.acceptConfirmEvacuatePushButton.setObjectName("acceptConfirmEvacuatePushButton")
        self.horizontalLayout.addWidget(self.acceptConfirmEvacuatePushButton)
        self.cancelConfirmEvacuatePushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cancelConfirmEvacuatePushButton.sizePolicy().hasHeightForWidth())
        self.cancelConfirmEvacuatePushButton.setSizePolicy(sizePolicy)
        self.cancelConfirmEvacuatePushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.cancelConfirmEvacuatePushButton.setFont(font)
        self.cancelConfirmEvacuatePushButton.setStyleSheet("QPushButton{\n"
"    padding: 0px 10px 0px 10px;\n"
"    background: rgb(230, 230, 230);\n"
"    color: #232323;\n"
"    border:1px rounded #232323;\n"
"    border-radius: 5px;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(255,255,255);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218);\n"
"    }")
        self.cancelConfirmEvacuatePushButton.setObjectName("cancelConfirmEvacuatePushButton")
        self.horizontalLayout.addWidget(self.cancelConfirmEvacuatePushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)

        # Connecting accept, cancel and forced evacuation
        # TODO: HEre goes the verification of users payment and sale attr in order to be able to launch acceptance evacuation message
        if deleteUserSpecs[0]:
            evacuateUser(deleteUserSpecs[1]) # TODO: (Spanish activated) se debe obtener el indice no mediante la tabla si no mediante el usuario, ya que al momento de eliminar consevutvamente, el indice
            updateIndexes()
            self.acceptConfirmEvacuatePushButton.clicked.connect(self.launchEvacuateConfirmationAccepted) #TODO: (1) se actualiza, mientras que el propio del usuario.
        else:
            self.acceptConfirmEvacuatePushButton.clicked.connect(self.launchEvacuateConfirmationDenied)

        self.cancelConfirmEvacuatePushButton.clicked.connect(self.closeEvacuateDenyConfirmation)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "CONFIRMACIÓN DE EVACUACIÓN"))
        self.titleLabel.setText(_translate("Form", "EVACUAR USUARIO"))
        self.messageLabel.setText(_translate("Form", "Estas a punto de evacuar un usuario. \n"
"Esta seguro de la decisión?. \n"
"Esto no se podrá deshacer:"))
        self.acceptConfirmEvacuatePushButton.setText(_translate("Form", "Aceptar"))
        self.cancelConfirmEvacuatePushButton.setText(_translate("Form", "Cancelar"))

    def showEvacuateConfirmation(self, ableToDelete, userToEvacuateIndex):
        deleteUserSpecs = (ableToDelete, userToEvacuateIndex)
        self.evacuateConfirmationWidgetInstance = QtWidgets.QWidget()
        # self.registerWidgetInstance.setWindowIcon(QtGui.QIcon(":/images/fact.png"))
        self.setupUi(self.evacuateConfirmationWidgetInstance, deleteUserSpecs)
        UiForm.formInstance = self.evacuateConfirmationWidgetInstance
        self.evacuateConfirmationWidgetInstance.show()

    @staticmethod
    def closeEvacuateDenyConfirmation():
        # TODO: type allows us to define what to do with the give nuser (remove it or not)
        return UiForm.formInstance.close() if UiForm.formInstance is not None else 0

    def launchEvacuateConfirmationAccepted(self):
        print("-----------------USUARIO ELIMINADO CON EXITO !! -----------------")
        self.viewEvacuateConfirmaction = evacuateConfirmationAccept.UiForm()
        self.viewEvacuateConfirmaction.showEvacuateConfirmationAccepted()
        self.closeEvacuateDenyConfirmation()

    def launchEvacuateConfirmationDenied(self):
        print("-----------------EL USUARIO NO PUDO SER ELIMINADO !! -----------------")
        self.viewEvacuateConfirmaction = evacuateConfirmationDeny.UiForm()
        self.viewEvacuateConfirmaction.showEvacuateConfirmationDenied()
        self.closeEvacuateDenyConfirmation()