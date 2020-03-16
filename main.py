import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from lib.YouViewerLayout import Ui_MainWindow
from PyQt5 import QtWebEngineWidgets
import re
import datetime
import io

# form_class=uic.loadUiType('D:/section6/ui/youtube.ui')[0]
sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")
class Main(QMainWindow, Ui_MainWindow):
    def __init__(self) :
        super().__init__()
        #초기화
        self.setupUi(self)
        #인증버튼
        self.initAuthLock()

    #기본 UI 비활성화
    def initAuthLock(self):
        self.previewButton.setEnabled(False)
        self.fileNavButton.setEnabled(False)
        self.streamCombobox.setEnabled(False)
        self.startButton.setEnabled(False)
        self.calendarWidget.setEnabled(False)
        self.urlTextEdit.setEnabled(False)
        self.pathTextEdit.setEnabled(False)

        self.showStatusMsg("인증안됨")

    def initAuthActive(self):
        self.previewButton.setEnabled(True)
        self.fileNavButton.setEnabled(True)
        self.streamCombobox.setEnabled(True)
        self.startButton.setEnabled(True)
        self.calendarWidget.setEnabled(True)
        self.urlTextEdit.setEnabled(True)
        self.pathTextEdit.setEnabled(True)
        self.showStatusMsg("인증됨")
    def showStatusMsg(self,msg):
        self.statusbar.showMessage(msg)
if __name__ == "__main__" :
    app=QApplication(sys.argv)
    window=Main()
    window.show()
    app.exec_()
