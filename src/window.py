import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic


app = QApplication(sys.argv)
form_class = uic.loadUiType("./res/smilewindow.ui")[0]


class Window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


smileWindow = Window()

async def display():
    smileWindow.show()

async def minimize():
    smileWindow.hide()