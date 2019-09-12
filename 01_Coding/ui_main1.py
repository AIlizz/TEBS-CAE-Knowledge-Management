# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tebs-CAE_knowledge_magement_ui_20190725.ui',
# licensing of 'tebs-CAE_knowledge_magement_ui_20190725.ui' applies.
#
# Created: Fri Jul 26 08:45:13 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(323, 242)
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        Dialog.setFont(font)
        Dialog.setCursor(QtCore.Qt.ArrowCursor)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-image: url(:/image/image_source_KM.qrc);\n"
"background-image: url(:/image/image/background.jpg);\n"
"background-image: url(:/image/image/background.jpg);")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(8, 201, 301, 32))
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setCursor(QtCore.Qt.ArrowCursor)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(80, 78, 177, 48))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("华文仿宋")
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "TEBS-CAE知识管理系统", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Dialog", "用户名", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Dialog", "密    码", None, -1))

import image_source_KM_rc
