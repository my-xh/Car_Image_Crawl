# -*- coding: utf-8 -*-

"""
@File    : ui_window.py
@Time    : 2021/4/22 21:54
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""

from PyQt5.QtWidgets import QApplication, QMainWindow
from login import Ui_Login
from main_window import Ui_MainWindow


class LoginWindow(QMainWindow, Ui_Login):
    """登录窗口"""

    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window
        self.btn_login.clicked.connect(self.login)  # 绑定登录按钮的点击事件

    def login(self):
        if self.edit_user.text() == 'xuheng':
            if self.edit_pwd.text() == '666666':
                self.close()
                self.main_window.is_login = True
                self.main_window.show()
            else:
                self.edit_pwd.setText('')
                self.edit_pwd.setPlaceholderText('密码输入错误！请重新输入')
        else:
            self.edit_user.setText('')
            self.edit_user.setPlaceholderText('用户名输入错误！请重新输入')


class UiWindow(QMainWindow, Ui_MainWindow):
    """主窗口"""

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.is_login = False
        self.login = LoginWindow(self)

    def show(self):
        if self.is_login:
            super().show()
        else:
            self.login.show()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = UiWindow()
    window.show()
    sys.exit(app.exec_())
