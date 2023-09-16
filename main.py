import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog 
from PyQt5.QtGui import QPixmap, QIcon


notfound_lines = []
missing_lines = []
warning_lines = []
failed_lines = []

miss_file = 0
warning = 0
not_found = 0
failed = 0

class Ui_UniLog(object):
    def setupUi(self, UniLog):
        UniLog.setObjectName("UniLog")
        UniLog.setEnabled(True)
        UniLog.resize(900, 250)
        UniLog.setMinimumSize(QtCore.QSize(900, 250))
        UniLog.setMaximumSize(QtCore.QSize(900, 250))
        self.centralwidget = QtWidgets.QWidget(UniLog)
        self.centralwidget.setObjectName("centralwidget")
        self.Warning = QtWidgets.QLabel(self.centralwidget)
        self.Warning.setGeometry(QtCore.QRect(270, 70, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(29)
        self.Warning.setFont(font)
        self.Warning.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Warning.setStyleSheet("color: rgb(210, 224, 255);")
        self.Warning.setAlignment(QtCore.Qt.AlignCenter)
        self.Warning.setObjectName("Warning")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 921, 251))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/Python/Repositories/UniLog_UI/Image/main2.png"))
        self.label.setObjectName("label")
        self.Not_Found = QtWidgets.QLabel(self.centralwidget)
        self.Not_Found.setGeometry(QtCore.QRect(430, 70, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(29)
        self.Not_Found.setFont(font)
        self.Not_Found.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Not_Found.setStyleSheet("color: rgb(210, 224, 255);")
        self.Not_Found.setAlignment(QtCore.Qt.AlignCenter)
        self.Not_Found.setObjectName("Not_Found")
        self.Failed = QtWidgets.QLabel(self.centralwidget)
        self.Failed.setGeometry(QtCore.QRect(600, 70, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(29)
        self.Failed.setFont(font)
        self.Failed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Failed.setStyleSheet("color: rgb(210, 224, 255);")
        self.Failed.setAlignment(QtCore.Qt.AlignCenter)
        self.Failed.setObjectName("Failed")
        self.Missing_Count = QtWidgets.QLabel(self.centralwidget)
        self.Missing_Count.setGeometry(QtCore.QRect(760, 70, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Inder")
        font.setPointSize(29)
        self.Missing_Count.setFont(font)
        self.Missing_Count.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Missing_Count.setStyleSheet("color: rgb(210, 224, 255);")
        self.Missing_Count.setAlignment(QtCore.Qt.AlignCenter)
        self.Missing_Count.setObjectName("Missing_Count")

        #кнопка upload_log
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 171, 41))
        self.pushButton.setStyleSheet("border: 2px solid rgba(80, 101, 124, 0.6);\n"
"border-radius: 20px;\n"
"color: rgb(210, 224, 255);\n"
"font: 14pt \"Inder\";")
        self.pushButton.setObjectName("upload")
        self.pushButton.clicked.connect(self.upload_log)  # Привязка функции к кнопке

        #кнопка convert_log
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 171, 41))
        self.pushButton_2.setStyleSheet("border: 2px solid rgba(80, 101, 124, 0.6);\n"
"border-radius: 20px;\n"
"color: rgb(210, 224, 255);\n"
"font: 14pt \"Inder\";")
        self.pushButton_2.setObjectName("convert")
        self.label.raise_()
        self.Warning.raise_()
        self.Not_Found.raise_()
        self.Failed.raise_()
        self.Missing_Count.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        UniLog.setCentralWidget(self.centralwidget)

        self.retranslateUi(UniLog)
        QtCore.QMetaObject.connectSlotsByName(UniLog)

    def retranslateUi(self, UniLog):
        _translate = QtCore.QCoreApplication.translate
        UniLog.setWindowTitle(_translate("UniLog", "UniLog"))
        self.Warning.setText(_translate("UniLog", "0"))
        self.Not_Found.setText(_translate("UniLog", "0"))
        self.Failed.setText(_translate("UniLog", "0"))
        self.Missing_Count.setText(_translate("UniLog", "0"))
        self.pushButton.setText(_translate("UniLog", "Upload log"))
        self.pushButton_2.setText(_translate("UniLog", "Convert log"))
        self.update_ui()  # Обновляем интерфейс
    
    def set_button_style(self, button):
        """Установка стиля для кнопки"""
        button.setFont(QtGui.QFont("Inder", 16))
        button.setStyleSheet(
            "font: 75 16pt 'Inder';"
            "background-color: rgb(106, 128, 255);"
            "color: rgb(255, 255, 255);"
            "border: none;"
            "border-radius: 10px;"
        )

    def set_label_style(self, label):
        """Установка стиля для метки"""
        label.setFont(QtGui.QFont("Inder", 29))
        label.setStyleSheet("color: rgb(255, 188, 7);")

    def update_ui(self):
        """Обновление значения ISMIS в интерфейсе"""
        self.Missing_Count.setText(str(miss_file))
        self.Warning.setText(str(warning))
        self.Not_Found.setText(str(not_found))
        self.Failed.setText(str(failed))

    def upload_log(self):
        """Обработчик нажатия на кнопку Upload Log"""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(
            None, "Select Log File", "", "Text Files (*.log *.txt);;All Files (*)", options=options
        )
        if file_path:
            self.process_log_file(file_path)
            self.update_ui()

    def process_log_file(self, file_path):
        """Обработка лог-файла"""

        with open(file_path, "r") as file:
            lines = file.readlines()

            global miss_file
            global warning
            global not_found
            global failed

            for line in lines:
                if "is missing!" in line:
                    miss_file += 1
                    missing_lines.append(line)
                    print('Потерянные файлы: ' , missing_lines)
                if "WARNING:" in line:
                    warning += 1
                    warning_lines.append(line)
                    print('Предупреждение: ' , warning_lines)
                if "not found" in line:
                    not_found += 1
                    notfound_lines.append(line)
                    print('Файл не найден: ' , notfound_lines)
                if "Failed" in line:
                    failed += 1
                    notfound_lines.append(line)
                    print('Ошибка : ' , failed_lines)



class UniLogApp(QMainWindow, Ui_UniLog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check_value()


    def check_value(self):
        #Проверка для обновления UI
        if miss_file > 0:
            self.update_ui()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UniLog = UniLogApp()
    UniLog.show()
    sys.exit(app.exec_())
