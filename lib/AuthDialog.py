import sys
from PyQt5.QtWidgets import *

class AuthDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUI()
        pass

    def setupUI(self):
        self.setGeometry(150,500,150,50)
        self.setFixedSize(300,100)

        laebl1=QLabel1("IND")
        label=QLabel("passord")

        self.lineEdit=QLineEdit
if __name__ == "__main__"








































































































































































:
    app=QApplication(sys.argv)
    loginDialog=AuthDialog()
    loginDialog.show()
    app.exec_()
