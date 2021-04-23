# -*- coding: utf-8 -*-

"""
@File    : main.py
@Time    : 2021/4/22 23:49
@Author  : my-xh
@Version : 1.0
@Software: PyCharm
@Desc    : 
"""

import os
import sys

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PIL import Image
from ui_window import UiWindow
from car_spider import CarSpider


def sort_file_by_name(file):
    """若文件名为纯数字，则按照数字大小排序"""
    base_name = os.path.basename(file)
    file_name, _ = os.path.splitext(base_name)
    if file_name.isdigit():
        return int(file_name)
    else:
        return ord(file_name)


class MyUI(UiWindow):

    def __init__(self):
        super().__init__()
        self.path = os.path.join(os.getcwd(), 'car').replace('/', '\\')
        self.spider = CarSpider()
        self.setup()

    def setup(self):
        self.tree_dir.hide()

        # 设置TreeWidget的根节点
        self.root = QTreeWidgetItem(self.tree_dir)
        self.root.setText(0, 'V8 Vantage 2018款 4.0T V8')

        self.btn_search.clicked.connect(self.search)
        self.tree_dir.clicked.connect(self.show_result)

    def search(self):
        """启动爬虫"""
        self.btn_search.setVisible(False)
        self.spider.get_img(save_to=self.path)
        self.btn_search.setVisible(True)

        self.tree_dir.setHeaderLabel('爬虫爬取的结果')
        self.add_tree_widget_items(self.root)
        self.tree_dir.show()

    def show_result(self):
        """展示爬取结果"""
        items = self.tree_dir.currentItem()
        if items.text(0) == 'V8 Vantage 2018款 4.0T V8':
            self.root.takeChildren()  # 删除root下的子节点
            self.add_tree_widget_items(self.root)
        else:
            # # 删除右侧的图片列表
            while self.grid_image.count() > 0:
                item = self.grid_image.takeAt(0)
                widget = item.widget()
                widget.deleteLater()

            # 将对应目录下的图片加入图片列表中
            dir_name = items.text(0)
            path = os.path.join(self.path, dir_name).replace('/', '\\')
            img_files = [os.path.join(path, img_file).replace(
                '/', '\\') for img_file in os.listdir(path)]
            img_files.sort(key=sort_file_by_name)

            row = 0
            for i in range(len(img_files)):
                row, col = i // 3, i % 3  # 计算图片所在的行列号
                # 创建容器组件
                widget = QWidget()
                widget.setGeometry(QtCore.QRect(0, 0, 300, 240))
                # 创建显示图片的标签
                label = QLabel(widget)
                label.setGeometry(QtCore.QRect(0, 0, 300, 240))
                label.setPixmap(QtGui.QPixmap(img_files[i]))
                label.setScaledContents(True)
                # 创建显示大图的按钮
                link_btn = QCommandLinkButton(widget)
                link_btn.setGeometry(QtCore.QRect(0, 0, 100, 40))
                link_btn.setText(os.path.basename(img_files[i]))
                link_btn.clicked.connect(lambda: self.show_large_image(path))  # 将点击信号与查看大图功能绑定
                # 添加容器组件
                self.grid_image.addWidget(widget, row, col)

            self.scrollArea_2.verticalScrollBar().setValue(0)  # 重置滚动条位置
            self.scrollAreaWidgetContents_2.setMinimumWidth(800)
            self.scrollAreaWidgetContents_2.setMinimumHeight(240 * (row + 1))  # 根据图片行数设置组件高度

    def add_tree_widget_items(self, root):
        """给指定根节点添加多个子节点"""
        for dir_name in os.listdir(self.path):
            QTreeWidgetItem(root).setText(0, dir_name)

    def show_large_image(self, path):
        """查看大图功能"""
        sender = self.grid_image.sender()  # 获取信号源点击的按钮
        img_name = sender.text()  # 获取图片名称
        img_file = os.path.join(path, img_name).replace('/', '\\')
        Image.open(img_file).show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyUI()
    window.show()
    sys.exit(app.exec_())
