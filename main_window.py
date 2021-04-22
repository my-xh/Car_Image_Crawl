# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1016, 740)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(10, 10, 191, 41))
        self.btn_search.setObjectName("btn_search")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(10, 60, 211, 651))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 209, 649))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.tree_dir = QtWidgets.QTreeView(self.scrollAreaWidgetContents)
        self.tree_dir.setGeometry(QtCore.QRect(0, 0, 211, 621))
        self.tree_dir.setObjectName("tree_dir")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setGeometry(QtCore.QRect(220, 60, 781, 651))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 779, 649))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 781, 651))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.grid_image = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.grid_image.setContentsMargins(0, 0, 0, 0)
        self.grid_image.setObjectName("grid_image")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "汽车之家图片抓取工具"))
        self.btn_search.setText(_translate("MainWindow", "阿斯顿·马丁 汽车图片"))

