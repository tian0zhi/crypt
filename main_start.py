from main_ui import Ui_MainWindow
from util import *
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QProgressBar   #导入PyQt相关模块
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
import threading
import os
import re

class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle('文件加密解密器')
        self.setWindowIcon(QIcon("fa.png"))
        self.key = None
        self.file_path = None
        self.file_name = None
        self.generate_key_pushButton.clicked.connect(self.generate_key)
        self.load_key_pushButton.clicked.connect(self.load_key)
        self.load_file_pushButton.clicked.connect(self.load_file)
        self.crpty_pushButton.clicked.connect(self.crypt_file)

    def generate_key(self):
        name = QFileDialog.getSaveFileName(self, 'Save key File', "key.cpt")
        if len(name[0])>1:
            key = gen_key()
            save_keyfile(key,name[0])
            QMessageBox.about(self, '提示', "key 文件生成完毕！")
        else:
            QMessageBox.about(self, '提示', "key 文件未生成！")

    def load_key(self):
        name = QFileDialog.getOpenFileName(self)
        if len(name[0])>1:
            self.key = get_key(name[0])
            self.key_lineEdit.clear()
            self.key_lineEdit.setText(name[0].split('/')[-1])
            QMessageBox.about(self, '提示', "key 加载成功！")
        else:
            QMessageBox.about(self, '提示', "key 未加载！")

    def load_file(self):
        name = QFileDialog.getOpenFileName(self)
        if len(name[0]) > 1:
            self.file_path = name[0]
            self.file_name = name[0].split('/')[-1]
            self.file_lineEdit.setText(self.file_name)
            QMessageBox.about(self, '提示', "文件加载成功！")
        else:
            QMessageBox.about(self, '提示', "文件未加载！")

    def crypt_file(self):
        if self.key and self.file_path and self.file_name:
            file_name_elem = self.file_name.split('.')
            name = QFileDialog.getSaveFileName(self, 'Save File', file_name_elem[0]+'_cpt_.'+file_name_elem[-1])
            if len(name[0]) > 1:
                crypt_file(self.file_path,name[0],self.key)
                QMessageBox.about(self, '提示', "文件加密/解密成功！")
            else:
                QMessageBox.about(self, '提示', "未保存文件！")
        else:
            QMessageBox.about(self, '提示', "key/文件未加载！")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyWindow()  # 创建对象
    myWin.show()  # 显示窗口
    sys.exit(app.exec_())  # `的对象，启动即可。