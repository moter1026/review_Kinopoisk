from PyQt6.QtCore import QSize
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QScrollArea
                            

import sys

from iterator import Iterator
import copy_dataset
import copy_dataset_random

class Button(QPushButton):
    def __init__(self, str: str):
        super().__init__()
        self.setFixedSize(QSize(100,50))
        self.setStyleSheet("background-color: yellow; border: 1px solid black; border-radius:10px;")
        self.move(200, 200)
        
        self.setText(str)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lab3-main window")
        self.setFixedSize(QSize(1000,600))
        self.setStyleSheet("padding: 0;")

        self.goodReview = Iterator("good")
        self.badReview = Iterator("bad")

        self.button = Button("След.")
        self.button2 = Button("Пред.")

        self.comboBox = QComboBox()
        self.comboBox.addItems(["good", "bad"])

        self.comboBox.currentTextChanged.connect(self.indexChanged)

        self.textLabel = QLabel()
        self.textLabel.setWordWrap(True)
        self.textLabel.setText("Нажмите на кнопку 'Следующий комментарий'")
        self.textLabel.adjustSize()
        # self.textLabel.setFixedSize(QSize(590, 600))
        # self.textLabel.setStyleSheet("border: 2px solid black;")

        self.scrollArea = QScrollArea()
        self.scrollArea.setWidget(self.textLabel)

        vlayout = QVBoxLayout()
        vlayout.addWidget(self.button)
        vlayout.addWidget(self.comboBox)

        hlayout = QHBoxLayout()
        hlayout.setSpacing(5)
        hlayout.setContentsMargins(0,0,0,0)
        hlayout.addWidget(self.button2)
        hlayout.addWidget(self.scrollArea)
        hlayout.addLayout(vlayout)
        # hlayout.addWidget(button)

        self.button.setCheckable(True)
        if(self.comboBox.currentText() == "good"):
            self.button.clicked.connect(self.nextGoodReview)
        else:
            self.button.clicked.connect(self.nextBadReview)
        widget = QWidget()
        widget.setLayout(hlayout)
        self.setCentralWidget(widget)
   
    def nextGoodReview(self):
        path_of_review = self.goodReview.__next__()
        text_of_review = ""
        try_encodings = ["utf-8", "utf-8-sig", "cp1251", "latin-1"]

        for encoding in try_encodings:
            # print(encoding)
            try:
                with open(path_of_review, "r", encoding=encoding) as readFile:
                    text_of_review = readFile.read()
                break  # Прерываем цикл, если декодирование успешно
            except UnicodeDecodeError:
                continue  # Переходим к следующей кодировке, если декодирование не удалось
        self.textLabel.setText("good\n" + text_of_review)
        self.textLabel.adjustSize()

    
    def nextBadReview(self):
        path_of_review = self.badReview.__next__()
        text_of_review = ""
        try_encodings = ["utf-8", "utf-8-sig", "cp1251", "latin-1"]

        for encoding in try_encodings:
            # print(encoding)
            try:
                with open(path_of_review, "r", encoding=encoding) as readFile:
                    text_of_review = readFile.read()
                break  # Прерываем цикл, если декодирование успешно
            except UnicodeDecodeError:
                continue  # Переходим к следующей кодировке, если декодирование не удалось
        self.textLabel.setText("bad\n" + text_of_review)
        self.textLabel.adjustSize()


    def indexChanged(self, string: str):
        self.button.clicked.disconnect()
        if(self.comboBox.currentText() == "good"):
            self.button.clicked.connect(self.nextGoodReview)
        else:
            self.button.clicked.connect(self.nextBadReview)
        self.textLabel.adjustSize()
        


if __name__ == "__main__":
    app = QApplication(sys.argv) 

    window = MainWindow()
    window.show()

    app.exec()