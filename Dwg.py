# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dwg.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DWG_SET_WINDOW(object):
    def setupUi(self, DWG_SET_WINDOW):
        DWG_SET_WINDOW.setObjectName("DWG_SET_WINDOW")
        DWG_SET_WINDOW.resize(863, 458)
        self.centralwidget = QtWidgets.QWidget(DWG_SET_WINDOW)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 837, 414))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_13 = QtWidgets.QLabel(self.layoutWidget)
        self.label_13.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_set = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_set.setFont(font)
        self.pushButton_set.setObjectName("pushButton_set")
        self.horizontalLayout.addWidget(self.pushButton_set)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_clear.setFont(font)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_cancel = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_cancel.setFont(font)
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        self.horizontalLayout.addWidget(self.pushButton_cancel)
        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_14 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_14.setFont(font)
        self.label_14.setMouseTracking(False)
        self.label_14.setTabletTracking(False)
        self.label_14.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_14.setAcceptDrops(False)
        self.label_14.setToolTip("")
        self.label_14.setAutoFillBackground(True)
        self.label_14.setObjectName("label_14")
        self.verticalLayout.addWidget(self.label_14)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setMouseTracking(False)
        self.label_2.setTabletTracking(False)
        self.label_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_2.setAcceptDrops(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setMouseTracking(False)
        self.label_3.setTabletTracking(False)
        self.label_3.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_3.setAcceptDrops(False)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setMouseTracking(False)
        self.label_4.setTabletTracking(False)
        self.label_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_4.setAcceptDrops(False)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setMouseTracking(False)
        self.label_6.setTabletTracking(False)
        self.label_6.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_6.setAcceptDrops(False)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_1.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_1.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.verticalLayout_3.addWidget(self.lineEdit_1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_3.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_3.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_5.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_5.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.verticalLayout_3.addWidget(self.lineEdit_5)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setMouseTracking(False)
        self.label_5.setTabletTracking(False)
        self.label_5.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_5.setAcceptDrops(False)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_7.setFont(font)
        self.label_7.setMouseTracking(False)
        self.label_7.setTabletTracking(False)
        self.label_7.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_7.setAcceptDrops(False)
        self.label_7.setToolTip("")
        self.label_7.setAutoFillBackground(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setMouseTracking(False)
        self.label_8.setTabletTracking(False)
        self.label_8.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_8.setAcceptDrops(False)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setMouseTracking(False)
        self.label_9.setTabletTracking(False)
        self.label_9.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_9.setAcceptDrops(False)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setMouseTracking(False)
        self.label_10.setTabletTracking(False)
        self.label_10.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_10.setAcceptDrops(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_6.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_6.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.verticalLayout_4.addWidget(self.lineEdit_6)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_7.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_7.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.verticalLayout_4.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_8.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_8.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.verticalLayout_4.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_9.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_9.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.verticalLayout_4.addWidget(self.lineEdit_9)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_10.setMinimumSize(QtCore.QSize(240, 30))
        self.lineEdit_10.setMaximumSize(QtCore.QSize(240, 25))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout_4.addWidget(self.lineEdit_10)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_12 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_2.addWidget(self.label_12)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_11.setMinimumSize(QtCore.QSize(240, 100))
        self.lineEdit_11.setMaximumSize(QtCore.QSize(999, 999))
        self.lineEdit_11.setText("")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.horizontalLayout_2.addWidget(self.lineEdit_11)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 2, 2)
        DWG_SET_WINDOW.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DWG_SET_WINDOW)
        self.statusbar.setObjectName("statusbar")
        DWG_SET_WINDOW.setStatusBar(self.statusbar)

        self.retranslateUi(DWG_SET_WINDOW)
        QtCore.QMetaObject.connectSlotsByName(DWG_SET_WINDOW)

    def retranslateUi(self, DWG_SET_WINDOW):
        _translate = QtCore.QCoreApplication.translate
        DWG_SET_WINDOW.setWindowTitle(_translate("DWG_SET_WINDOW", "MainWindow"))
        self.label_13.setText(_translate("DWG_SET_WINDOW", "SCALE:由系統自行運算"))
        self.pushButton_set.setText(_translate("DWG_SET_WINDOW", "確認參數(Set)"))
        self.pushButton_clear.setText(_translate("DWG_SET_WINDOW", "清除參數(Clear)"))
        self.pushButton_cancel.setText(_translate("DWG_SET_WINDOW", "取消(Cancel)"))
        self.label_14.setText(_translate("DWG_SET_WINDOW", "出圖日期\n"
"(Date)"))
        self.label_2.setText(_translate("DWG_SET_WINDOW", "硬度\n"
"(Hardness)"))
        self.label_3.setText(_translate("DWG_SET_WINDOW", "繪圖\n"
"(Plotter)"))
        self.label_4.setText(_translate("DWG_SET_WINDOW", "審核\n"
"(Review)"))
        self.label_6.setText(_translate("DWG_SET_WINDOW", "核准\n"
"(Approve)"))
        self.label_5.setText(_translate("DWG_SET_WINDOW", "材料\n"
"(Material)"))
        self.label_7.setText(_translate("DWG_SET_WINDOW", "數量\n"
"(Quantity)"))
        self.label_8.setText(_translate("DWG_SET_WINDOW", "圖名\n"
"(Figure Name)"))
        self.label_9.setText(_translate("DWG_SET_WINDOW", "圖號\n"
"(Figure Number)"))
        self.label_10.setText(_translate("DWG_SET_WINDOW", "單位(Unit)"))
        self.lineEdit_6.setText(_translate("DWG_SET_WINDOW", " Aluminum"))
        self.lineEdit_10.setText(_translate("DWG_SET_WINDOW", "mm"))
        self.label_12.setText(_translate("DWG_SET_WINDOW", "備註\n"
"(Note)"))