import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

# Глобальная переменная для подсчета ISMIS
ISMIS = 0

class Ui_UniLog(object):
    def setupUi(self, UniLog):
        # Настройки окна
        UniLog.setObjectName("UniLog")
        UniLog.setEnabled(True)
        UniLog.resize(900, 600)
        UniLog.setMinimumSize(QtCore.QSize(900, 600))
        UniLog.setMaximumSize(QtCore.QSize(900, 600))
        
        # Создание центрального виджета
        self.centralwidget = QtWidgets.QWidget(UniLog)
        self.centralwidget.setObjectName("centralwidget")
        
        # Добавление фоновых изображений и настройка элементов интерфейса
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
        self.set_button_style(self.Uploadbtn)
        self.Uploadbtn.setObjectName("Uploadbtn")
        self.Uploadbtn.clicked.connect(self.upload_log)  # Привязка функции к кнопке
        
        self.ListenFolder = QtWidgets.QPushButton(self.centralwidget)
        self.ListenFolder.setEnabled(True)
        self.ListenFolder.setGeometry(QtCore.QRect(20, 160, 171, 31))
        self.set_button_style(self.ListenFolder)
        self.ListenFolder.setObjectName("ListenFolder")
        
        self.Missing_Count = QtWidgets.QLabel(self.centralwidget)
        self.Missing_Count.setGeometry(QtCore.QRect(260, 100, 101, 61))
        self.set_label_style(self.Missing_Count)
        self.Missing_Count.setObjectName("Missing_Count")
        self.Missing_Count.setAlignment(QtCore.Qt.AlignCenter)
        
        self.Missing_Count.raise_()
        UniLog.setCentralWidget(self.centralwidget)
        self.retranslateUi(UniLog)
        QtCore.QMetaObject.connectSlotsByName(UniLog)

    def retranslateUi(self, UniLog):
        _translate = QtCore.QCoreApplication.translate
        UniLog.setWindowTitle(_translate("UniLog", "UniLog"))
        self.Uploadbtn.setText(_translate("UniLog", "Upload Log"))
        self.ListenFolder.setText(_translate("UniLog", "Listen Folder"))
        self.update_ui()  # Обновляем значение ISMIS в интерфейсе

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
        self.Missing_Count.setText(str(ISMIS))

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
        """Обработка лог-файла для подсчета ISMIS"""
        global ISMIS
        with open(file_path, "r") as file:
            lines = file.readlines()
            for line in lines:
                if "is missing!" in line:
                    ISMIS += 1

class UniLogApp(QMainWindow, Ui_UniLog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.check_value()

    def check_value(self):
        """Проверка значения ISMIS и обновление интерфейса"""
        if ISMIS > 0:
            self.update_ui()
            print('ISMIS сейчас:', ISMIS)
        else:
            print('ISMIS сейчас:', ISMIS)
            print('меньше')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UniLog = UniLogApp()
    UniLog.show()
    sys.exit(app.exec_())
