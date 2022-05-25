import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QHeaderView, QComboBox,
                             QLineEdit, QCheckBox, QWidget, QHBoxLayout)


class DemoTableWidget(QMainWindow):
    def __init__(self, parent=None):
        super(DemoTableWidget, self).__init__(parent)
        # 設置窗口標題
        self.setWindowTitle('實戰PyQt5: QTableWidget 演示')
    # 設置窗口大小
        self.resize(500, 300)
        self.initUi()


    def initUi(self):
        # #行數和列數
        rows = 8
        cols = 4
        tableWidget = QTableWidget(rows, cols, self)
        tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('狀態'))
        tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('起始值'))
        tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem('結束值'))
        tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem('選擇'))
        # 所有列自動拉伸，充滿界面
        tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        for row in range(rows):
            # 第一列，啟用/禁用選擇
            cmbState = QComboBox()
            cmbState.addItem('Disabled')
            cmbState.addItem('Enabled')
            cmbState.setCurrentIndex(0)
            tableWidget.setCellWidget(row, 0, cmbState)
            # 第二列，起始值
            startVal = QLineEdit('0.0')
            startVal.setAlignment(Qt.AlignHCenter)
            tableWidget.setCellWidget(row, 1, startVal)
            # 第三列，結束值
            stopVal = QLineEdit('100.0')
            stopVal.setAlignment(Qt.AlignHCenter)
            tableWidget.setCellWidget(row, 2, stopVal)
            # 第四列，複選按鈕,居中排列
            chkBox = QCheckBox('相對值')
            chkBox.setChecked(True)
            hLayout = QHBoxLayout()
            widget = QWidget(tableWidget)
            hLayout.addWidget(chkBox)
            hLayout.setContentsMargins(0, 0, 0, 0)
            hLayout.setAlignment(Qt.AlignHCenter)
            widget.setLayout(hLayout)
            tableWidget.setCellWidget(row, 3, widget)
            self.setCentralWidget(tableWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
window = DemoTableWidget()
window.show()
sys.exit(app.exec())
