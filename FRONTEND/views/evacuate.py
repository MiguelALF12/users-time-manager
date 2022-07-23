# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/miguellopez/Desktop/PROYECTS/PAGOS/ARENERO-RAMIRO/FRONTEND/views/QT_DESIGNS/designs/evacuate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FRONTEND.views import icons
from FRONTEND.views.placements import placeholders

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("EVACUAR USUARIO")
        Form.resize(656, 311)
        Form.setMinimumSize(QtCore.QSize(656, 311))
        Form.setMaximumSize(QtCore.QSize(656, 311))
        Form.setStyleSheet("background-color:#ffc3ae;")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setSpacing(26)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(18)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label.setStyleSheet("color:#000000;")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setStyleSheet("color:#000000;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.searchLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(230, 32))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(230, 32))
        self.searchLineEdit.setMouseTracking(True)
        self.searchLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.searchLineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.searchLineEdit.setStyleSheet("QLineEdit{\n"
"    background-color: #ffffff;\n"
"    border: 1px rounded #232323;\n"
"    border-radius: 12px;\n"
"    border-style: outset;\n"
"    font-family: \"Helvetica\";\n"
"    font-weight: 400;\n"
"    font-size: 18px;\n"
"    text-align: left;\n"
"    padding-left: 10px;\n"
"    color:#000000;}\n"
"\n"
"")
        self.searchLineEdit.setText("")
        self.searchLineEdit.setFrame(False)
        self.searchLineEdit.setReadOnly(False)
        self.searchLineEdit.setClearButtonEnabled(True)
        self.searchLineEdit.setObjectName("searchLineEdit")
        self.horizontalLayout.addWidget(self.searchLineEdit)
        self.searchRecordPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchRecordPushButton.sizePolicy().hasHeightForWidth())
        self.searchRecordPushButton.setSizePolicy(sizePolicy)
        self.searchRecordPushButton.setMinimumSize(QtCore.QSize(50, 32))
        self.searchRecordPushButton.setMaximumSize(QtCore.QSize(50, 32))
        self.searchRecordPushButton.setStyleSheet("QPushButton{\n"
"    padding: 0px 10px 0px 10px;\n"
"    background: rgb(255, 246, 53);\n"
"    color: #ffffff;\n"
"    border:1px rounded #232323;\n"
"    border-radius: 10px;\n"
"    border-style: outset;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(232, 218, 70);\n"
"    }\n"
"\n"
"QPushButton:pressed {\n"
"    border-style: inset;\n"
"    background: rgb(214, 218, 218);\n"
"    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/usedIcons/icons8-search-30.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchRecordPushButton.setIcon(icon)
        self.searchRecordPushButton.setIconSize(QtCore.QSize(24, 24))
        self.searchRecordPushButton.setObjectName("searchRecordPushButton")
        self.horizontalLayout.addWidget(self.searchRecordPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLabel.sizePolicy().hasHeightForWidth())
        self.nameLabel.setSizePolicy(sizePolicy)
        self.nameLabel.setMinimumSize(QtCore.QSize(80, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.nameLabel.setFont(font)
        self.nameLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
"color:#ffffff;")
        self.nameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.exitPeopleLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitPeopleLabel.sizePolicy().hasHeightForWidth())
        self.exitPeopleLabel.setSizePolicy(sizePolicy)
        self.exitPeopleLabel.setMinimumSize(QtCore.QSize(60, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.exitPeopleLabel.setFont(font)
        self.exitPeopleLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
"color:#ffffff;")
        self.exitPeopleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exitPeopleLabel.setWordWrap(True)
        self.exitPeopleLabel.setObjectName("exitPeopleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.exitPeopleLabel)
        self.putSaleLabel = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putSaleLabel.sizePolicy().hasHeightForWidth())
        self.putSaleLabel.setSizePolicy(sizePolicy)
        self.putSaleLabel.setMinimumSize(QtCore.QSize(50, 30))
        self.putSaleLabel.setMaximumSize(QtCore.QSize(50, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putSaleLabel.setFont(font)
        self.putSaleLabel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.putSaleLabel.setAutoFillBackground(False)
        self.putSaleLabel.setStyleSheet("background: rgb(97, 177, 66);\n"
"border:1px rounded #232323;\n"
"border-radius: 10px;\n"
"border-style: outset;")
        self.putSaleLabel.setMaxLength(0)
        self.putSaleLabel.setFrame(False)
        self.putSaleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putSaleLabel.setReadOnly(True)
        self.putSaleLabel.setPlaceholderText("")
        self.putSaleLabel.setObjectName("putSaleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.putSaleLabel)
        self.putNameLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putNameLabel.sizePolicy().hasHeightForWidth())
        self.putNameLabel.setSizePolicy(sizePolicy)
        self.putNameLabel.setMinimumSize(QtCore.QSize(210, 35))
        self.putNameLabel.setMaximumSize(QtCore.QSize(210, 35))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putNameLabel.setFont(font)
        self.putNameLabel.setStyleSheet("QLabel {\n"
"    border: 2px rounded;\n"
"    border-color: rgb(57, 57, 57);\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background-color: #ffffff;\n"
"    padding: 5 px;\n"
"    color:#000000}")
        self.putNameLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putNameLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putNameLabel.setLineWidth(2)
        self.putNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putNameLabel.setObjectName("putNameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.putNameLabel)
        self.horizontalLayout_3.addLayout(self.formLayout)
        spacerItem2 = QtWidgets.QSpacerItem(320, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(208, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "EVACUAR USUARIO"))
        self.label_2.setText(_translate("Form", "IDENTIFICADOR"))
        self.searchLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_SEARCH_RECORD']))
        self.nameLabel.setText(_translate("Form", "Nombre"))
        self.exitPeopleLabel.setText(_translate("Form", "Sale"))
        self.putSaleLabel.setToolTip(_translate("Form", "El usuario debe o no salir"))
        self.putNameLabel.setText(_translate("Form", placeholders['PH_NAME']))
        self.pushButton.setText(_translate("Form", "Registrar"))
        self.pushButton_2.setText(_translate("Form", "Cancelar"))

    def showEvacuate(self):
        self.evacuateWidgetInstance = QtWidgets.QWidget()
        # self.registerWidgetInstance.setWindowIcon(QtGui.QIcon(":/images/fact.png"))
        self.setupUi(self.evacuateWidgetInstance)
        self.evacuateWidgetInstance.show()