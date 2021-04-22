# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):

    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(292, 267)
        Login.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(20, 20, 251, 221))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_user = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_user.sizePolicy().hasHeightForWidth())
        self.label_user.setSizePolicy(sizePolicy)
        self.label_user.setObjectName("label_user")
        self.verticalLayout.addWidget(self.label_user)
        self.edit_user = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_user.sizePolicy().hasHeightForWidth())
        self.edit_user.setSizePolicy(sizePolicy)
        self.edit_user.setText("")
        self.edit_user.setObjectName("edit_user")
        self.verticalLayout.addWidget(self.edit_user)
        self.label_pwd = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_pwd.sizePolicy().hasHeightForWidth())
        self.label_pwd.setSizePolicy(sizePolicy)
        self.label_pwd.setObjectName("label_pwd")
        self.verticalLayout.addWidget(self.label_pwd)
        self.edit_pwd = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_pwd.sizePolicy().hasHeightForWidth())
        self.edit_pwd.setSizePolicy(sizePolicy)
        self.edit_pwd.setObjectName("edit_pwd")
        self.verticalLayout.addWidget(self.edit_pwd)
        self.empty = QtWidgets.QLabel(self.widget)
        self.empty.setText("")
        self.empty.setObjectName("empty")
        self.verticalLayout.addWidget(self.empty)
        self.btn_login = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_login.sizePolicy().hasHeightForWidth())
        self.btn_login.setSizePolicy(sizePolicy)
        self.btn_login.setObjectName("btn_login")
        self.verticalLayout.addWidget(self.btn_login)
        self.btn_quit = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_quit.sizePolicy().hasHeightForWidth())
        self.btn_quit.setSizePolicy(sizePolicy)
        self.btn_quit.setObjectName("btn_quit")
        self.verticalLayout.addWidget(self.btn_quit)

        self.retranslateUi(Login)
        self.btn_quit.clicked.connect(Login.close)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "登录"))
        self.label_user.setText(_translate("Login", "用户名(xuheng):"))
        self.label_pwd.setText(_translate("Login", "密码(666666):"))
        self.btn_login.setText(_translate("Login", "登录"))
        self.btn_quit.setText(_translate("Login", "退出"))
