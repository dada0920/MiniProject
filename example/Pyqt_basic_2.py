import sys
import io
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# sys.stdout = io.TextIOWrapper(sys.stdout.detach(),encoding="utf-8")
# sys.stderr = io.TextIOWrapper(sys.stderr.detach(),encoding="utf-8")

class TestForm(QMainWindow) : #PyQt5.QtWidgets 에서 상속받아서 불러옴

    #생성자
    def __init__(self):
        super().__init__() #부모의 생성자 함수 호출
        self.setupUI()
    def setupUI(self):
        self.setWindowTitle("PyQT test") #제목표시줄
        self.setGeometry(800,400,500,500) #window창 크기 조절
        #800,400 = window 창 위치(어디에띄울까?)
        #500,300 = windwo 창의 크기
        btn_1=QPushButton("Click1",self)
        btn_2=QPushButton("Click2",self)
        btn_3=QPushButton("Click3",self)

        btn_1.move(200,100)
        btn_2.move(200,150)
        btn_3.move(200,200)


        #누르는 자체를 signal (시그널)
        btn_1.clicked.connect(self.btn_1_clicked)
        btn_2.clicked.connect(self.btn_2_clicked)
        btn_3.clicked.connect(QCoreApplication.instance().quit) #시그널 & 슬

        #창이 나오는 것을 slot (슬롯)

    def btn_1_clicked(self):
        QMessageBox.about(self,"Button Title","click")


    def btn_2_clicked(self):
        print("Button 2  click")



if __name__ == "__main__":
    # label=QLabel("프 로 젝 트")
    # label.show()

    app=QApplication(sys.argv)
    window=TestForm()




    window.show()

    app.exec_()
