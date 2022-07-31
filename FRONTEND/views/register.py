# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/miguellopez/Desktop/PROYECTS/PAGOS/ARENERO-RAMIRO/FRONTEND/views/QT_DESIGNS/designs/register.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from FRONTEND.views import icons
from FRONTEND.views.constantsAndOthers import placeholders, DEFAULT_USER_TIME_PRICES, VIP_USER_TIME_PRICES
from BACKEND.CRUD.CRUD_users import *


class UiForm(object):
    formInstance = None

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1100, 370)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1100, 370))
        Form.setMaximumSize(QtCore.QSize(1100, 370))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(198, 221, 234);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.registerUserLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.registerUserLabel.sizePolicy().hasHeightForWidth())
        self.registerUserLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.registerUserLabel.setFont(font)
        self.registerUserLabel.setScaledContents(False)
        self.registerUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.registerUserLabel.setWordWrap(True)
        self.registerUserLabel.setStyleSheet("color:#000000;")
        self.registerUserLabel.setObjectName("registerUserLabel")
        self.verticalLayout.addWidget(self.registerUserLabel)
        self.line = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line.sizePolicy().hasHeightForWidth())
        self.line.setSizePolicy(sizePolicy)
        self.line.setMinimumSize(QtCore.QSize(995, 5))
        self.line.setStyleSheet("margin-left:20px;margin-right:20px;")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
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
        self.nameLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLineEdit.sizePolicy().hasHeightForWidth())
        self.nameLineEdit.setSizePolicy(sizePolicy)
        self.nameLineEdit.setMinimumSize(QtCore.QSize(210, 30))
        self.nameLineEdit.setMaximumSize(QtCore.QSize(210, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.nameLineEdit.setStyleSheet("background: #ffffff;\n"
                                        "border:2px rounded;\n"
                                        "border-radius: 10px;\n"
                                        "border-style: outset;\n"
                                        "border-color: rgb(57, 57, 57);\n"
                                        "color:#000000;")
        self.nameLineEdit.setFrame(False)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.nameLineEdit.setReadOnly(False)
        self.nameLineEdit.setClearButtonEnabled(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.braceletNumLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.braceletNumLabel.sizePolicy().hasHeightForWidth())
        self.braceletNumLabel.setSizePolicy(sizePolicy)
        self.braceletNumLabel.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.braceletNumLabel.setFont(font)
        self.braceletNumLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                            "color:#ffffff;")
        self.braceletNumLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.braceletNumLabel.setWordWrap(True)
        self.braceletNumLabel.setObjectName("braceletNumLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.braceletNumLabel)
        self.braceletNumLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.braceletNumLineEdit.sizePolicy().hasHeightForWidth())
        self.braceletNumLineEdit.setSizePolicy(sizePolicy)
        self.braceletNumLineEdit.setMinimumSize(QtCore.QSize(100, 30))
        self.braceletNumLineEdit.setMaximumSize(QtCore.QSize(100, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.braceletNumLineEdit.setFont(font)
        self.braceletNumLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.braceletNumLineEdit.setStyleSheet("background: #ffffff;\n"
                                               "border:2px rounded;\n"
                                               "border-radius: 10px;\n"
                                               "border-style: outset;\n"
                                               "border-color: rgb(57, 57, 57);\n"
                                               "color:#000000;")
        self.braceletNumLineEdit.setFrame(False)
        self.braceletNumLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.braceletNumLineEdit.setReadOnly(False)
        self.braceletNumLineEdit.setClearButtonEnabled(True)
        self.braceletNumLineEdit.setObjectName("braceletNumLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.braceletNumLineEdit)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem)
        self.horizontalLayout.addLayout(self.formLayout)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_2.setObjectName("formLayout_2")
        self.ParentIDLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParentIDLineEdit.sizePolicy().hasHeightForWidth())
        self.ParentIDLineEdit.setSizePolicy(sizePolicy)
        self.ParentIDLineEdit.setMinimumSize(QtCore.QSize(130, 30))
        self.ParentIDLineEdit.setMaximumSize(QtCore.QSize(130, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ParentIDLineEdit.setFont(font)
        self.ParentIDLineEdit.setStyleSheet("background: #ffffff;\n"
                                            "border:2px rounded;\n"
                                            "border-radius: 10px;\n"
                                            "border-style: outset;\n"
                                            "border-color: rgb(57, 57, 57);\n"
                                            "color:#000000;")
        self.ParentIDLineEdit.setFrame(False)
        self.ParentIDLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ParentIDLineEdit.setReadOnly(False)
        self.ParentIDLineEdit.setObjectName("ParentIDLineEdit")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.ParentIDLineEdit)
        self.totalTimeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTimeLabel.sizePolicy().hasHeightForWidth())
        self.totalTimeLabel.setSizePolicy(sizePolicy)
        self.totalTimeLabel.setMinimumSize(QtCore.QSize(80, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.totalTimeLabel.setFont(font)
        self.totalTimeLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                          "color:#ffffff;")
        self.totalTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.totalTimeLabel.setObjectName("totalTimeLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totalTimeLabel)
        self.parentLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentLabel.sizePolicy().hasHeightForWidth())
        self.parentLabel.setSizePolicy(sizePolicy)
        self.parentLabel.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.parentLabel.setFont(font)
        self.parentLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                       "color:#ffffff;")
        self.parentLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.parentLabel.setObjectName("parentLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.parentLabel)
        self.ParentLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ParentLineEdit.sizePolicy().hasHeightForWidth())
        self.ParentLineEdit.setSizePolicy(sizePolicy)
        self.ParentLineEdit.setMinimumSize(QtCore.QSize(210, 32))
        self.ParentLineEdit.setMaximumSize(QtCore.QSize(210, 32))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.ParentLineEdit.setFont(font)
        self.ParentLineEdit.setStyleSheet("background: #ffffff;\n"
                                          "border:2px rounded;\n"
                                          "border-radius: 10px;\n"
                                          "border-style: outset;\n"
                                          "border-color: rgb(57, 57, 57);\n"
                                          "color:#000000;")
        self.ParentLineEdit.setFrame(False)
        self.ParentLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.ParentLineEdit.setReadOnly(False)
        self.ParentLineEdit.setObjectName("ParentLineEdit")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.ParentLineEdit)
        self.parentIDLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.parentIDLabel.sizePolicy().hasHeightForWidth())
        self.parentIDLabel.setSizePolicy(sizePolicy)
        self.parentIDLabel.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.parentIDLabel.setFont(font)
        self.parentIDLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                         "color:#ffffff;")
        self.parentIDLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.parentIDLabel.setObjectName("parentIDLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.parentIDLabel)
        self.totalTimeComboBox = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTimeComboBox.sizePolicy().hasHeightForWidth())
        self.totalTimeComboBox.setSizePolicy(sizePolicy)
        self.totalTimeComboBox.setMinimumSize(QtCore.QSize(130, 22))
        self.totalTimeComboBox.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.totalTimeComboBox.setFont(font)
        self.totalTimeComboBox.setMouseTracking(True)
        self.totalTimeComboBox.setStyleSheet("background: #ffffff;\n"
                                             "border:2px rounded;\n"
                                             "border-radius: 6px;\n"
                                             "border-style: outset;\n"
                                             "border-color: rgb(57, 57, 57);\n"
                                             "color:#000000;")
        self.totalTimeComboBox.setObjectName("totalTimeComboBox")
        self.totalTimeComboBox.addItem("")
        self.totalTimeComboBox.addItem("")
        self.totalTimeComboBox.addItem("")
        self.totalTimeComboBox.addItem("")
        self.totalTimeComboBox.addItem("")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.totalTimeComboBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.formLayout_2.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        self.horizontalLayout.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeft)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignCenter)
        self.formLayout_3.setObjectName("formLayout_3")

        self.vipUserLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vipUserLabel.sizePolicy().hasHeightForWidth())
        self.vipUserLabel.setSizePolicy(sizePolicy)
        self.vipUserLabel.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.vipUserLabel.setFont(font)
        self.vipUserLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                        "color:#ffffff;")
        self.vipUserLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.vipUserLabel.setObjectName("vipUserLabel")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.vipUserLabel)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.YesVipUserRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YesVipUserRadioButton.sizePolicy().hasHeightForWidth())
        self.YesVipUserRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.YesVipUserRadioButton.setFont(font)
        self.YesVipUserRadioButton.setStyleSheet("color:#000000;\n"
                                                 "")
        self.YesVipUserRadioButton.setCheckable(True)
        self.YesVipUserRadioButton.setChecked(False)
        self.YesVipUserRadioButton.setAutoRepeat(False)
        self.YesVipUserRadioButton.setObjectName("YesVipUserRadioButton")
        self.horizontalLayout_6.addWidget(self.YesVipUserRadioButton)
        self.NoVipUserRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoVipUserRadioButton.sizePolicy().hasHeightForWidth())
        self.NoVipUserRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.NoVipUserRadioButton.setFont(font)
        self.NoVipUserRadioButton.setStyleSheet("color:#000000;\n"
                                                "")
        self.NoVipUserRadioButton.setCheckable(True)
        self.NoVipUserRadioButton.setChecked(False)
        self.NoVipUserRadioButton.setAutoRepeat(False)
        self.NoVipUserRadioButton.setObjectName("NoVipUserRadioButton")
        self.horizontalLayout_6.addWidget(self.NoVipUserRadioButton)
        self.formLayout_3.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_6)

        self.putPriceLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putPriceLabel.sizePolicy().hasHeightForWidth())
        self.putPriceLabel.setSizePolicy(sizePolicy)
        self.putPriceLabel.setMinimumSize(QtCore.QSize(130, 30))
        self.putPriceLabel.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putPriceLabel.setFont(font)
        self.putPriceLabel.setStyleSheet("QLabel {\n"
                                         "    border: 2px rounded;\n"
                                         "    border-color: rgb(57, 57, 57);\n"
                                         "    border-radius: 8px;\n"
                                         "    border-style: outset;\n"
                                         "    background-color: #ffffff;\n"
                                         "    padding: 5 px;\n"
                                         "    color:#000000;\n"
                                         "}")
        self.putPriceLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putPriceLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putPriceLabel.setLineWidth(2)
        self.putPriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putPriceLabel.setObjectName("putPriceLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.putPriceLabel)
        self.priceLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.priceLabel.sizePolicy().hasHeightForWidth())
        self.priceLabel.setSizePolicy(sizePolicy)
        self.priceLabel.setMinimumSize(QtCore.QSize(100, 20))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.priceLabel.setFont(font)
        self.priceLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                      "color:#ffffff;")
        self.priceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.priceLabel.setWordWrap(True)
        self.priceLabel.setObjectName("priceLabel")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
        self.payedLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.payedLabel.sizePolicy().hasHeightForWidth())
        self.payedLabel.setSizePolicy(sizePolicy)
        self.payedLabel.setMinimumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.payedLabel.setFont(font)
        self.payedLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
                                      "color:#ffffff;")
        self.payedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.payedLabel.setObjectName("payedLabel")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.payedLabel)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.YesPayedRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.YesPayedRadioButton.sizePolicy().hasHeightForWidth())
        self.YesPayedRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.YesPayedRadioButton.setFont(font)
        self.YesPayedRadioButton.setStyleSheet("color:#000000;\n"
                                               "")
        self.YesPayedRadioButton.setCheckable(True)
        self.YesPayedRadioButton.setChecked(False)
        self.YesPayedRadioButton.setAutoRepeat(False)
        self.YesPayedRadioButton.setObjectName("YesPayedRadioButton")
        self.horizontalLayout_3.addWidget(self.YesPayedRadioButton)
        self.NoPayedRadioButton = QtWidgets.QRadioButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoPayedRadioButton.sizePolicy().hasHeightForWidth())
        self.NoPayedRadioButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.NoPayedRadioButton.setFont(font)
        self.NoPayedRadioButton.setStyleSheet("color:#000000;\n"
                                              "")
        self.NoPayedRadioButton.setCheckable(True)
        self.NoPayedRadioButton.setChecked(False)
        self.NoPayedRadioButton.setAutoRepeat(False)
        self.NoPayedRadioButton.setObjectName("NoPayedRadioButton")
        self.horizontalLayout_3.addWidget(self.NoPayedRadioButton)
        self.formLayout_3.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.formLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.acceptRegisterRequestPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptRegisterRequestPushButton.sizePolicy().hasHeightForWidth())
        self.acceptRegisterRequestPushButton.setSizePolicy(sizePolicy)
        self.acceptRegisterRequestPushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.acceptRegisterRequestPushButton.setFont(font)
        self.acceptRegisterRequestPushButton.setStyleSheet("QPushButton{\n"
                                                           "    padding: 0px 10px 0px 10px;\n"
                                                           "    background: rgb(163, 111, 61);\n"
                                                           "    color: #232323;\n"
                                                           "    border:1px rounded #232323;\n"
                                                           "    border-radius: 5px;\n"
                                                           "    border-style: outset;\n"
                                                           "}\n"
                                                           "\n"
                                                           "QPushButton:hover {\n"
                                                           "    background: #e0d1bd;\n"
                                                           "    }\n"
                                                           "\n"
                                                           "QPushButton:pressed {\n"
                                                           "    border-style: inset;\n"
                                                           "    background: rgb(214, 218, 218);\n"
                                                           "    }")
        self.acceptRegisterRequestPushButton.setObjectName("acceptRegisterRequestPushButton")
        self.horizontalLayout_2.addWidget(self.acceptRegisterRequestPushButton)
        self.denyRegisterRequestPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.denyRegisterRequestPushButton.sizePolicy().hasHeightForWidth())
        self.denyRegisterRequestPushButton.setSizePolicy(sizePolicy)
        self.denyRegisterRequestPushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.denyRegisterRequestPushButton.setFont(font)
        self.denyRegisterRequestPushButton.setStyleSheet("QPushButton{\n"
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
        self.denyRegisterRequestPushButton.setObjectName("denyRegisterRequestPushButton")
        self.horizontalLayout_2.addWidget(self.denyRegisterRequestPushButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        self.totalTimeComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # Connecting acceptRegister and denyRegister buttons
        self.acceptRegisterRequestPushButton.clicked.connect(self.saveUser)
        self.denyRegisterRequestPushButton.clicked.connect(self.closeRegister)

        # other signals
        self.totalTimeComboBox.activated.connect(lambda: self.putPriceLabel.setText(str(self.calcChargingPrice())))
        # TODO: Here goes something similar but with VIP users

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "REGISTRAR USUARIO"))
        self.registerUserLabel.setText(_translate("Form", "REGISTRAR USUARIO"))
        self.nameLabel.setText(_translate("Form", "Nombre"))
        self.nameLineEdit.setToolTip(_translate("Form", "Nombre de usuario"))
        self.nameLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_NAME']))
        self.braceletNumLabel.setText(_translate("Form", "Número de manilla"))
        self.braceletNumLineEdit.setToolTip(_translate("Form", "numero de manilla"))
        self.braceletNumLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_BRACELET_NUMBER']))
        self.ParentIDLineEdit.setToolTip(_translate("Form", "Cedula de acudiente"))
        self.ParentIDLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_PARENT_ID']))
        self.totalTimeLabel.setText(_translate("Form", "Tiempo"))
        self.parentLabel.setText(_translate("Form", "Acudiente"))
        self.ParentLineEdit.setToolTip(_translate("Form", "nombre de acudiente"))
        self.ParentLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_PARENT']))
        self.parentIDLabel.setText(_translate("Form", "Acudiente-ID"))
        self.totalTimeComboBox.setCurrentText(_translate("Form", "Seleccione"))
        self.totalTimeComboBox.setItemText(0, _translate("Form", "Seleccione"))
        self.totalTimeComboBox.setItemText(1, _translate("Form", "15 minutos"))
        self.totalTimeComboBox.setItemText(2, _translate("Form", "30 minutos"))
        self.totalTimeComboBox.setItemText(3, _translate("Form", "1 hora"))
        self.totalTimeComboBox.setItemText(4, _translate("Form", "2 horas"))
        self.ParentLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_PARENT']))
        self.priceLabel.setText(_translate("Form", "Valor total a pagar"))
        self.putPriceLabel.setText(_translate("Form", placeholders['PH_TOTAL_MONEY']))
        self.payedLabel.setText(_translate("Form", "Cancelado"))
        self.YesPayedRadioButton.setText(_translate("Form", "SI"))
        self.NoPayedRadioButton.setText(_translate("Form", "NO"))
        self.vipUserLabel.setText(_translate("Form", "Usuario VIP"))
        self.YesVipUserRadioButton.setText(_translate("Form", "SI"))
        self.NoVipUserRadioButton.setText(_translate("Form", "NO"))
        self.acceptRegisterRequestPushButton.setText(_translate("Form", "Aceptar"))
        self.denyRegisterRequestPushButton.setText(_translate("Form", "Cancelar"))

    def showRegister(self):
        self.registerWidgetInstance = QtWidgets.QWidget()
        # self.registerWidgetInstance.setWindowIcon(QtGui.QIcon(":/images/fact.png"))
        self.setupUi(self.registerWidgetInstance)
        UiForm.formInstance = self.registerWidgetInstance
        self.registerWidgetInstance.show()

    def closeRegister(self):
        return UiForm.formInstance.close() if UiForm.formInstance is not None else 0

    def show_pop_up(self, show_text, message_type):
        message = QMessageBox()
        # message.windowIcon()
        message.setWindowTitle("Arenero PlayKids")
        message.setText(show_text)
        message.setIcon(message_type)
        message.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = message.exec_()

    def validateFields(self, user):
        # Default values
        # {'Nombre': '', 'Manilla': '', 'Tiempo': 'Seleccione',
        # 'Acudiente': '', 'ID-Acudiente': '', 'Dinero': '', 'Pagado': False, 'Usuario VIP': False}
        # All are obligatory, at the momment, ignoring the fact that payed and vipUser can go False
        fieldsWithErrors = []
        excludedFields = ["Manilla", "Dinero", "Pagado", "Usuario VIP"]
        noTAdmitedValues = ["", None]
        for field, value in user.items():
            if field not in excludedFields:
                if value in noTAdmitedValues:
                    fieldsWithErrors.append(field)
        if len(fieldsWithErrors) != 0:
            separator = ","
            self.show_pop_up(f"Tienes errores en los campos {separator.join(fieldsWithErrors)}", QMessageBox.Warning)
        else:
            return True

    def calcChargingPrice(self):
        selectedTime = self.totalTimeComboBox.currentText()
        if self.YesVipUserRadioButton.isChecked():
            return VIP_USER_TIME_PRICES[selectedTime]
        else:
            return DEFAULT_USER_TIME_PRICES[selectedTime]

    def saveUser(self):
        newUser = {
            "Nombre": self.nameLineEdit.text().strip(),
            "Manilla": self.braceletNumLineEdit.text().strip(),
            "Tiempo": self.totalTimeComboBox.currentText(),
            "Acudiente": self.ParentLineEdit.text().strip(),
            "ID-Acudiente": self.ParentIDLineEdit.text().strip(),
            "Dinero": self.calcChargingPrice(),
            "Pagado": True if self.YesPayedRadioButton.isChecked() else False,
            "Usuario VIP": True if self.YesVipUserRadioButton.isChecked() else False,
            # TODO: Remember manage this when creating count time module
            "Hora entrada": 0,
            "Hora salida": 0,
            "Sale": False
        }
        if self.validateFields(newUser):
            print("Usuario añadido -> ", newUser)
            createUser(newUser)
            self.closeRegister()

# TODO: Problems with checkbox section
