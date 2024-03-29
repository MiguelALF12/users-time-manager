# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/miguellopez/Desktop/PROYECTS/PAGOS/ARENERO-RAMIRO/FRONTEND/views/QT_DESIGNS/designs/edit.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from FRONTEND.constantsAndOthers import placeholders

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1170, 426)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(1170, 426))
        Form.setMaximumSize(QtCore.QSize(1170, 426))
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(254, 194, 248);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.editLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editLabel.sizePolicy().hasHeightForWidth())
        self.editLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.editLabel.setFont(font)
        self.editLabel.setScaledContents(False)
        self.editLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.editLabel.setWordWrap(True)
        self.editLabel.setStyleSheet("color:#000000;")
        self.editLabel.setObjectName("editLabel")
        self.verticalLayout.addWidget(self.editLabel)
        self.searchRecordLayout = QtWidgets.QHBoxLayout()
        self.searchRecordLayout.setObjectName("searchRecordLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchRecordLayout.addItem(spacerItem)
        self.searchIdentifierLabel = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.searchIdentifierLabel.setFont(font)
        self.searchIdentifierLabel.setStyleSheet("color:#000000")
        self.searchIdentifierLabel.setObjectName("searchIdentifierLabel")
        self.searchRecordLayout.addWidget(self.searchIdentifierLabel)
        self.searchLineEdit = QtWidgets.QLineEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchLineEdit.sizePolicy().hasHeightForWidth())
        self.searchLineEdit.setSizePolicy(sizePolicy)
        self.searchLineEdit.setMinimumSize(QtCore.QSize(466, 32))
        self.searchLineEdit.setMaximumSize(QtCore.QSize(466, 32))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.searchLineEdit.setFont(font)
        self.searchLineEdit.setMouseTracking(True)
        self.searchLineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
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
        self.searchRecordLayout.addWidget(self.searchLineEdit)
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
        self.searchRecordLayout.addWidget(self.searchRecordPushButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.searchRecordLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.searchRecordLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem2)
        self.bodyLayou = QtWidgets.QHBoxLayout()
        self.bodyLayou.setObjectName("bodyLayou")
        self.nama_braceletNum_formLayout = QtWidgets.QFormLayout()
        self.nama_braceletNum_formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.nama_braceletNum_formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.nama_braceletNum_formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.nama_braceletNum_formLayout.setObjectName("nama_braceletNum_formLayout")
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
        self.nama_braceletNum_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
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
        self.nama_braceletNum_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.braceletNumLabel)
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
"border:2px rounded #232323;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-color: rgb(57, 57, 57);\n"
"color:#000000;")
        self.braceletNumLineEdit.setFrame(False)
        self.braceletNumLineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.braceletNumLineEdit.setReadOnly(False)
        self.braceletNumLineEdit.setClearButtonEnabled(True)
        self.braceletNumLineEdit.setObjectName("braceletNumLineEdit")
        self.nama_braceletNum_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.braceletNumLineEdit)
        spacerItem3 = QtWidgets.QSpacerItem(20, 80, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.nama_braceletNum_formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem3)
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
"border:2px rounded #232323;\n"
"border-radius: 10px;\n"
"border-style: outset;\n"
"border-color: rgb(57, 57, 57);\n"
"padding-left:25px;"
"color:#000000;")
        self.nameLineEdit.setFrame(False)
        self.nameLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.nameLineEdit.setReadOnly(False)
        self.nameLineEdit.setClearButtonEnabled(True)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nama_braceletNum_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.bodyLayou.addLayout(self.nama_braceletNum_formLayout)
        self.time_hours_formLayout = QtWidgets.QFormLayout()
        self.time_hours_formLayout.setRowWrapPolicy(QtWidgets.QFormLayout.WrapLongRows)
        self.time_hours_formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.time_hours_formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.time_hours_formLayout.setObjectName("time_hours_formLayout")
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
        self.time_hours_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.totalTimeLabel)
        self.putTotalTimeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putTotalTimeLabel.sizePolicy().hasHeightForWidth())
        self.putTotalTimeLabel.setSizePolicy(sizePolicy)
        self.putTotalTimeLabel.setMinimumSize(QtCore.QSize(130, 30))
        self.putTotalTimeLabel.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putTotalTimeLabel.setFont(font)
        self.putTotalTimeLabel.setStyleSheet("QLabel {\n"
"    border: 2px rounded;\n"
"    border-color: rgb(57, 57, 57);\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background-color: #ffffff;\n"
"    padding: 5 px;\n"
"    color:#000000;}")
        self.putTotalTimeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putTotalTimeLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putTotalTimeLabel.setLineWidth(2)
        self.putTotalTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putTotalTimeLabel.setObjectName("putTotalTimeLabel")
        self.time_hours_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.putTotalTimeLabel)
        self.extraTimeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.extraTimeLabel.sizePolicy().hasHeightForWidth())
        self.extraTimeLabel.setSizePolicy(sizePolicy)
        self.extraTimeLabel.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.extraTimeLabel.setFont(font)
        self.extraTimeLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
"color:#ffffff;")
        self.extraTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.extraTimeLabel.setObjectName("extraTimeLabel")
        self.time_hours_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.extraTimeLabel)
        self.addedValueLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addedValueLabel.sizePolicy().hasHeightForWidth())
        self.addedValueLabel.setSizePolicy(sizePolicy)
        self.addedValueLabel.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.addedValueLabel.setFont(font)
        self.addedValueLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
"color:#ffffff;")
        self.addedValueLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.addedValueLabel.setObjectName("addedValueLabel")
        self.time_hours_formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.addedValueLabel)
        self.putExtraPriceLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putExtraPriceLabel.sizePolicy().hasHeightForWidth())
        self.putExtraPriceLabel.setSizePolicy(sizePolicy)
        self.putExtraPriceLabel.setMinimumSize(QtCore.QSize(130, 30))
        self.putExtraPriceLabel.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putExtraPriceLabel.setFont(font)
        self.putExtraPriceLabel.setStyleSheet("QLabel {\n"
"    border: 2px rounded;\n"
"    border-color: rgb(57, 57, 57);\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background-color: #ffffff;\n"
"    padding: 5 px;\n"
"    color:#000000;}")
        self.putExtraPriceLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putExtraPriceLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putExtraPriceLabel.setLineWidth(2)
        self.putExtraPriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putExtraPriceLabel.setObjectName("putExtraPriceLabel")
        self.time_hours_formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.putExtraPriceLabel)
        self.exitTimeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitTimeLabel.sizePolicy().hasHeightForWidth())
        self.exitTimeLabel.setSizePolicy(sizePolicy)
        self.exitTimeLabel.setMinimumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.exitTimeLabel.setFont(font)
        self.exitTimeLabel.setStyleSheet("background:rgb(80, 80, 80);\n"
"color:#ffffff;")
        self.exitTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exitTimeLabel.setWordWrap(True)
        self.exitTimeLabel.setObjectName("exitTimeLabel")
        self.time_hours_formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.exitTimeLabel)
        self.putExitTimeLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putExitTimeLabel.sizePolicy().hasHeightForWidth())
        self.putExitTimeLabel.setSizePolicy(sizePolicy)
        self.putExitTimeLabel.setMinimumSize(QtCore.QSize(130, 30))
        self.putExitTimeLabel.setMaximumSize(QtCore.QSize(130, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.putExitTimeLabel.setFont(font)
        self.putExitTimeLabel.setStyleSheet("QLabel {\n"
"    border: 2px rounded;\n"
"    border-color: rgb(57, 57, 57);\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background-color: #ffffff;\n"
"    padding: 5 px;\n"
"    color:#000000;}")
        self.putExitTimeLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putExitTimeLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putExitTimeLabel.setLineWidth(2)
        self.putExitTimeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putExitTimeLabel.setObjectName("putExitTimeLabel")
        self.time_hours_formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.putExitTimeLabel)
        self.totalTimeComboBox_2 = QtWidgets.QComboBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totalTimeComboBox_2.sizePolicy().hasHeightForWidth())
        self.totalTimeComboBox_2.setSizePolicy(sizePolicy)
        self.totalTimeComboBox_2.setMinimumSize(QtCore.QSize(130, 22))
        self.totalTimeComboBox_2.setMaximumSize(QtCore.QSize(210, 30))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.totalTimeComboBox_2.setFont(font)
        self.totalTimeComboBox_2.setMouseTracking(True)
        self.totalTimeComboBox_2.setStyleSheet("QComboBox {\n"
"    border: 2px rounded;\n"
"    border-radius: 8px;\n"
"    border-style: outset;   \n"
"    border-color: rgb(57, 57, 57);\n"
"    padding: 5px 18px 5px 5px;   \n"
"    background-color:#ffffff;\n"
"    color:#000;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item{\n"
"    background-color: #ffffff; \n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"    color: #ffffff;\n"
"}")
        self.totalTimeComboBox_2.setObjectName("totalTimeComboBox_2")
        self.totalTimeComboBox_2.addItem("")
        self.totalTimeComboBox_2.addItem("")
        self.totalTimeComboBox_2.addItem("")
        self.totalTimeComboBox_2.addItem("")
        self.totalTimeComboBox_2.addItem("")
        self.time_hours_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.totalTimeComboBox_2)
        self.bodyLayou.addLayout(self.time_hours_formLayout)
        self.price_formLayout = QtWidgets.QFormLayout()
        self.price_formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.price_formLayout.setFormAlignment(QtCore.Qt.AlignCenter)
        self.price_formLayout.setObjectName("price_formLayout")
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
        self.price_formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.priceLabel)
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
"    color:#000000;}")
        self.putPriceLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putPriceLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putPriceLabel.setLineWidth(2)
        self.putPriceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putPriceLabel.setObjectName("putPriceLabel")
        self.price_formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.putPriceLabel)
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
        self.price_formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.payedLabel)
        self.putPayedLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.putPayedLabel.sizePolicy().hasHeightForWidth())
        self.putPayedLabel.setSizePolicy(sizePolicy)
        self.putPayedLabel.setMinimumSize(QtCore.QSize(70, 30))
        self.putPayedLabel.setMaximumSize(QtCore.QSize(70, 30))
        self.putPayedLabel.setStyleSheet("QLabel {\n"
"    border: 2px rounded;\n"
"    border-color: rgb(57, 57, 57);\n"
"    border-radius: 8px;\n"
"    border-style: outset;\n"
"    background-color: rgb(119, 191, 65);\n"
"    padding: 5 px;\n"
"}")
        self.putPayedLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.putPayedLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.putPayedLabel.setLineWidth(2)
        self.putPayedLabel.setText("")
        self.putPayedLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.putPayedLabel.setObjectName("putPayedLabel")
        self.price_formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.putPayedLabel)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.price_formLayout.setItem(2, QtWidgets.QFormLayout.FieldRole, spacerItem4)
        self.bodyLayou.addLayout(self.price_formLayout)
        self.verticalLayout_2.addLayout(self.bodyLayou)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem5)
        self.dialogEditRequestsLayout = QtWidgets.QHBoxLayout()
        self.dialogEditRequestsLayout.setSpacing(30)
        self.dialogEditRequestsLayout.setObjectName("dialogEditRequestsLayout")
        spacerItem6 = QtWidgets.QSpacerItem(40, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dialogEditRequestsLayout.addItem(spacerItem6)
        self.acceptEditRequestPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.acceptEditRequestPushButton.sizePolicy().hasHeightForWidth())
        self.acceptEditRequestPushButton.setSizePolicy(sizePolicy)
        self.acceptEditRequestPushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.acceptEditRequestPushButton.setFont(font)
        self.acceptEditRequestPushButton.setStyleSheet("QPushButton{\n"
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
        self.acceptEditRequestPushButton.setObjectName("acceptEditRequestPushButton")
        self.dialogEditRequestsLayout.addWidget(self.acceptEditRequestPushButton)
        self.denyEditRequestPushButton = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.denyEditRequestPushButton.sizePolicy().hasHeightForWidth())
        self.denyEditRequestPushButton.setSizePolicy(sizePolicy)
        self.denyEditRequestPushButton.setMinimumSize(QtCore.QSize(120, 30))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.denyEditRequestPushButton.setFont(font)
        self.denyEditRequestPushButton.setStyleSheet("QPushButton{\n"
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
        self.denyEditRequestPushButton.setObjectName("denyEditRequestPushButton")
        self.dialogEditRequestsLayout.addWidget(self.denyEditRequestPushButton)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.dialogEditRequestsLayout.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.dialogEditRequestsLayout)

        self.retranslateUi(Form)
        self.totalTimeComboBox_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "EDITAR USUARIOS"))
        self.editLabel.setText(_translate("Form", "EDITAR USUARIO"))
        self.searchIdentifierLabel.setText(_translate("Form", "IDENTIFICADOR"))
        self.searchLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_SEARCH_RECORD']))
        self.nameLabel.setText(_translate("Form", "Nombre"))
        self.braceletNumLabel.setText(_translate("Form", "Número de manilla"))
        self.braceletNumLineEdit.setToolTip(_translate("Form", "Total de personas"))
        self.braceletNumLineEdit.setPlaceholderText(_translate("Form", placeholders['PH_BRACELET_NUMBER']))
        self.nameLineEdit.setToolTip(_translate("Form", "Total de personas"))
        self.nameLineEdit.setPlaceholderText(_translate("Form",placeholders['PH_NAME']))
        self.totalTimeLabel.setText(_translate("Form", "Tiempo"))
        self.putTotalTimeLabel.setText(_translate("Form", placeholders['PH_HOUR']))
        self.extraTimeLabel.setText(_translate("Form", "Tiempo extra"))
        self.addedValueLabel.setText(_translate("Form", "Valor añadido"))
        self.putExtraPriceLabel.setText(_translate("Form", placeholders['PH_TOTAL_MONEY']))
        self.exitTimeLabel.setText(_translate("Form", "Hora estimada de salida"))
        self.putExitTimeLabel.setText(_translate("Form", placeholders['PH_HOUR']))
        # TODO Determine what are the options available to choose in terms of extra time
        self.totalTimeComboBox_2.setCurrentText(_translate("Form", "Seleccione"))
        self.totalTimeComboBox_2.setItemText(0, _translate("Form", "Seleccione"))
        self.totalTimeComboBox_2.setItemText(1, _translate("Form", "New Item"))
        self.totalTimeComboBox_2.setItemText(2, _translate("Form", "New Item"))
        self.totalTimeComboBox_2.setItemText(3, _translate("Form", "New Item"))
        self.totalTimeComboBox_2.setItemText(4, _translate("Form", "New Item"))
        self.priceLabel.setText(_translate("Form", "Valor total a pagar"))
        self.putPriceLabel.setText(_translate("Form",placeholders['PH_TOTAL_MONEY']))
        self.payedLabel.setText(_translate("Form", "Cancelado"))
        self.acceptEditRequestPushButton.setText(_translate("Form", "Aceptar"))
        self.denyEditRequestPushButton.setText(_translate("Form", "Cancelar"))

    def showEdit(self):
        self.editWidgetInstance = QtWidgets.QWidget()
        # self.registerWidgetInstance.setWindowIcon(QtGui.QIcon(":/images/fact.png"))
        self.setupUi(self.editWidgetInstance)
        self.editWidgetInstance.show()
