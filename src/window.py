import sys

from PyQt5.QtCore import QMetaObject, Qt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from qasync import asyncSlot

import constants as constants

app = QApplication(sys.argv)
smile_form_class = uic.loadUiType("./res/smilewindow.ui")[0]


class SmileWindow(QMainWindow, smile_form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


smileWindow = SmileWindow()

async def display_smile():
    app.processEvents()
    smileWindow.show()

async def minimize_smile():
    app.processEvents()
    smileWindow.hide()


gauge_form_class = uic.loadUiType("./res/gaugewindow.ui")[0]


class GaugeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar Example")
        self.setGeometry(100, 100, 300, 150)
        main_widget = QWidget()
        layout = QVBoxLayout()
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setMinimum(constants.PROGRESS_BAR_MIN)
        self.progress_bar.setMaximum(constants.PROGRESS_BAR_MAX)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)
        self.current_value = 0

    def update_progress(self, value):
        self.progress_bar.setValue(value)

gaugeWindow = GaugeWindow()

async def display_gauge():
    app.processEvents()
    gaugeWindow.show()

async def minimize_gauge():
    app.processEvents()
    gaugeWindow.hide()

async def set_gauge(value):
    app.processEvents()
    gaugeWindow.update_progress(value)