from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog
from PyQt5.QtCore import Qt

import cheker

class Ui_UniLog(object):
    def setupUi(self, UniLog):
        UniLog.setObjectName("UniLog")
        UniLog.setEnabled(True)
        UniLog.resize(900, 600)
        UniLog.setMinimumSize(QtCore.QSize(900, 600))
        UniLog.setMaximumSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(UniLog)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 901, 581))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("image/Main.png")) 
        self.label.setObjectName("label")
        self.label2 = QtWidgets.QLabel(self.centralwidget)
        self.label2.setGeometry(QtCore.QRect(240, 20, 141, 171))
        self.label2.setText("")
        self.label2.setPixmap(QtGui.QPixmap("image/MissFile.png"))
        self.label2.setObjectName("label2")
        self.Uploadbtn = QtWidgets.QPushButton(self.centralwidget)
        self.Uploadbtn.setEnabled(True)
        self.Uploadbtn.setGeometry(QtCore.QRect(20, 120, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.Uploadbtn.setFont(font)
        self.Uploadbtn.setToolTip("")
        self.Uploadbtn.setStyleSheet("font: 75 12pt \"Calibri\";\n"
"background-color: rgb(106, 128, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Inder\";\n"
"border: none;\n"
"border-radius: 10px;")
        self.Uploadbtn.setCheckable(False)
        self.Uploadbtn.setObjectName("Uploadbtn")
        self.ListenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.ListenFolder.setEnabled(True)
        self.ListenFolder.setGeometry(QtCore.QRect(20, 160, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.ListenFolder.setFont(font)
        self.ListenFolder.setToolTip("")
        self.ListenFolder.setStyleSheet("font: 75 12pt \"Calibri\";\n"
"background-color: rgb(106, 128, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"Inder\";\n"
"border: none;\n"
"border-radius: 10px;")
        self.ListenFolder.setCheckable(False)
        self.ListenFolder.setObjectName("ListenFolder")
        UniLog.setCentralWidget(self.centralwidget)
        self.retranslateUi(UniLog)
        QtCore.QMetaObject.connectSlotsByName(UniLog)

    def retranslateUi(self, UniLog):
        _translate = QtCore.QCoreApplication.translate
        UniLog.setWindowTitle(_translate("UniLog", "UniLog"))
        self.Uploadbtn.setText(_translate("UniLog", "Upload Log"))
        self.ListenFolder.setText("Listen Folder")

class UniLogApp(QMainWindow, Ui_UniLog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Uploadbtn.clicked.connect(self.upload_log)

    def upload_log(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(None, "Select Log File", "", "Text Files (*.txt);;All Files (*)", options=options)
        if file_path:
            cheker.process_log_file(file_path)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    UniLog = UniLogApp()
    UniLog.show()
    sys.exit(app.exec_())
