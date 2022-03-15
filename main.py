from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget,
    QHBoxLayout,
    QApplication, QPushButton,
    QFileDialog, QTableWidget,
    QTableWidgetItem
)
from PyQt5.QtGui import (
    QPixmap
)
from PyQt5.QtCore import Qt

import sys

from numpy import csingle
from alg import predictor

csv_path = r'patient_data.csv'


class Window(QWidget):
    def __init__(self, fn, filePath=None):
        super().__init__()
        self.initUI()
        self.fn = fn
        if filePath:
            self.load(filePath)

    def initUI(self):
        self.vbox = QVBoxLayout()

        self.hbox = QHBoxLayout()
        self.btnLoad = QPushButton("Load")
        self.btnLoad.clicked.connect(self.btnLoad_onClick)
        self.hbox.addWidget(self.btnLoad)

        self.btn2 = QPushButton("Результаты")
        self.btn2.clicked.connect(self.btn2_onClick)
        self.hbox.addWidget(self.btn2)

        self.vbox.addLayout(self.hbox)

        self.table = QTableWidget()
        self.vbox.addWidget(self.table)

        self.setLayout(self.vbox)

    def btn2_onClick(self):
        #self.fn()
        self.load('result.csv')

    def btnLoad_onClick(self):
        self.load()

    def load(self, path=None):
        if path is None:
            path = QFileDialog.getOpenFileName(
                self,
                'Open image',
                '',
                "Таблица csv (*.csv)"
            )[0]
            csv_path = path
            if not path:
                return # Пользователь нажал на отмену или крест

        lst = []
        with open(path, 'r') as f:
            for line in f.readlines():
                lst.append(line.rstrip().split(','))
        self.table.clear()
        self.table.setColumnCount(len(lst[0]))
        self.table.setRowCount(len(lst) - 1)
        self.table.setHorizontalHeaderLabels(lst[0])


        for i in range(len(lst)-1):
            for j in range(len(lst[i])):
                self.table.setItem(i, j, QTableWidgetItem(lst[i+1][j]))
                self.table.item(i, j).setFlags(Qt.ItemIsEnabled | Qt.ItemIsSelectable)

        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()



if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = Window(predictor(csv_path))
    win.show()

    sys.exit(app.exec_())
