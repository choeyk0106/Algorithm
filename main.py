# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import threading, time, random


orderQueue = list();

server1 = 0
server2 = 0
server3 = 0

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Order:
    Americano = 0
    CaffeLatte = 0
    Cappuccino = 0
    CaffeMocha = 0
    CaramelMacchiato = 0

    totalOfOrder = 0
    OrderNumber = 0
    def SetTotalOrder(self):
        self.totalOfOrder = self.Americano + self.CaffeLatte + self.Cappuccino + self.CaffeMocha + self.CaramelMacchiato

def DistributeOrder():
    tempOrder = orderQueue[0];
    sumOfCost = server1 + server2 + server3;
    if(sumOfCost == 0):
        for i in range(0, tempOrder.totalOfOrder):
            if(tempOrder.Americano != 0):
                print("uu")
    else:
        print("sum is 1")

    orderQueue.pop()

class TimerHandler:
    @staticmethod
    def get_timer_by_list(progress_bar, time_list):
        first_timer = TimerHandler(progress_bar, time_list[0])
        post_timer = first_timer
        for i in range(1, len(time_list)):
            temp = TimerHandler(progress_bar, time_list[i])
            post_timer.enroll_end_callback(temp.start)
            post_timer = temp

        return first_timer

    def __init__(self, progress_bar, full_time):
        self.timer = QTimer()
        self.progress_bar = progress_bar
        self.progress_cnt = 0
        self.tick_time = full_time / 1000;
        self.end_callback = None

        def timer_callback():
            self.progress_cnt += 0.1
            self.progress_bar.setProperty("value", self.progress_cnt)

            if self.progress_cnt >= 100:
                self.timer.stop()
                self.end()

        self.timer.timeout.connect(timer_callback)

    def start(self):
        self.timer.start(self.tick_time)

    def enroll_end_callback(self, callback):
        self.end_callback = callback

    def end(self):
        self.progress_bar.setProperty("value", 0)
        if self.end_callback is not None:
            self.end_callback()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(576, 561)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 431, 181))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsTristate)
        self.tableWidget.setItem(0, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(0, 1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(1, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(2, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(3, 1, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 0, item)
        item = QtGui.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.tableWidget.setItem(4, 1, item)
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(100, 10, 256, 31))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        # count up / down
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(370, 80, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.spinBox_2 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(370, 110, 42, 22))
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_3.setGeometry(QtCore.QRect(370, 140, 42, 22))
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_4.setGeometry(QtCore.QRect(370, 170, 42, 22))
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(self.centralwidget)
        self.spinBox_5.setGeometry(QtCore.QRect(370, 200, 42, 22))
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))

        # order button
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(450, 210, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.spinBoxValue)

        # tag number box
        self.lcdNumber_1 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_1.setGeometry(QtCore.QRect(40, 320, 141, 71))
        self.lcdNumber_1.setObjectName(_fromUtf8("lcdNumber_1"))
        self.lcdNumber_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(220, 320, 141, 71))
        self.lcdNumber_2.setObjectName(_fromUtf8("lcdNumber_2"))
        self.lcdNumber_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdNumber_3.setGeometry(QtCore.QRect(400, 320, 141, 71))
        self.lcdNumber_3.setObjectName(_fromUtf8("lcdNumber_3"))

        # progressbar
        self.progressBar_1 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_1.setGeometry(QtCore.QRect(60, 400, 121, 21))
        self.progressBar_1.setProperty("value", 0)
        self.progressBar_1.setObjectName(_fromUtf8("progressBar_1"))
        self.progressBar_2 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(240, 400, 121, 21))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(420, 400, 121, 21))
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setObjectName(_fromUtf8("progressBar_3"))

        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(150, 260, 271, 41))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 576, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.progress_timer_1 = TimerHandler.get_timer_by_list(self.progressBar_1, [1000, 1400, 2000, 4000, 3100])
        self.progress_timer_1.start()

        self.progress_timer_2 = TimerHandler.get_timer_by_list(self.progressBar_2, [1400, 2000, 1000, 4000, 3100])
        self.progress_timer_2.start()

        self.progress_timer_3 = TimerHandler.get_timer_by_list(self.progressBar_3, [2300, 4400, 5100, 2000, 1200])
        self.progress_timer_3.start()

    def download(self):
        self.completed = 0

        while (self.completed < 100):
            self.completed += 0.0001
            self.progress.setValue(self.completed)

    def spinBoxValue(self):
        order = Order()
        order.Americano = self.spinBox.value()
        order.CaffeLatte = self.spinBox_2.value()
        order.Cappuccino = self.spinBox_3.value()
        order.CaffeMocha = self.spinBox_4.value()
        order.CaramelMacchiato = self.spinBox_5.value()
        print("아메리카노", order.Americano, "개")
        print("카페라떼", order.CaffeLatte, "개")
        print("카푸치노", order.Cappuccino, "개")
        print("카페모카", order.CaffeMocha, "개")
        print("카라멜마뀌아로~", order.CaramelMacchiato, "개")
        self.spinBox.setProperty("value", 0)
        self.spinBox_2.setProperty("value", 0)
        self.spinBox_3.setProperty("value", 0)
        self.spinBox_4.setProperty("value", 0)
        self.spinBox_5.setProperty("value", 0)

        order.SetTotalOrder()
        orderQueue.append(order)
        DistributeOrder()

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "Americano", None))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainWindow", "Caffe Latte", None))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cappuccino", None))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainWindow", "Caffe Mocha", None))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainWindow", "Caramel Macchiato", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Price", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Count", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("MainWindow", "3500", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "2min", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "4000", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "2.5min", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "4000", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "2.5min", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "4500", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "3min", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "5000", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "4min", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">MENU</span></p></body></html>", None))
        self.pushButton.setText(_translate("MainWindow", "Order", None))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Progress Bar</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
