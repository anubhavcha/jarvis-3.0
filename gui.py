from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1556, 984)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 10, 1761, 1061))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(530, 210, 551, 431))
        self.label_2.setStyleSheet("background-color: Transparent;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Samy_gui/sci-unscreen.gif"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(-40, 0, 421, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Samy_gui/2l.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(570, 610, 471, 131))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Samy_gui/3l.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(1200, 0, 401, 281))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Samy_gui/4lp.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(660, 370, 291, 111))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Samy_gui/Samy.gif"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(670, 630, 261, 91))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("Samy_gui/Samy.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
