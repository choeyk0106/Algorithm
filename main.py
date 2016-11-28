﻿# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
import threading, time, random

orderQueue = list();

server = [[0],[0],[0]]

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


def WhoIsServerWhenZero():
    minCost = 9999
    minServer = -1
    maxCost = -1
    maxServer = -1

    for i in range(0, 3):
        if (maxCost < server[i][0]):
            maxCost = server[i][0]
            maxServer = i

    for i in range(0, 3):
        if (minCost > server[i][0] and i != maxServer):
            minCost = server[i][0]
            minServer = i

    return minServer


def DistributeOrder():
    tempOrder = orderQueue[0];
    newServer= [[],[],[]]

    for i in range(0, tempOrder.totalOfOrder):
        idx = WhoIsServerWhenZero()

        if (tempOrder.CaramelMacchiato != 0):
            server[idx].append(6000)
            newServer[idx].append(6000)
            server[idx][0] += 6000
            tempOrder.CaramelMacchiato -= 1
            continue

        if (tempOrder.CaffeMocha != 0):
            server[idx].append(5000)
            newServer[idx].append(5000)
            server[idx][0] += 5000
            tempOrder.CaffeMocha -= 1
            continue

        if (tempOrder.Cappuccino != 0):
            server[idx].append(4000)
            newServer[idx].append(4000)
            server[idx][0] += 4000
            tempOrder.Cappuccino -= 1
            continue

        if (tempOrder.CaffeLatte != 0):
            server[idx].append(3000)
            newServer[idx].append(3000)
            server[idx][0] += 3000
            tempOrder.CaffeLatte -= 1
            continue

        if (tempOrder.Americano != 0):
            server[idx].append(2000)
            newServer[idx].append(2000)
            server[idx][0] += 2000
            tempOrder.Americano -= 1
            continue

    ui.lcdNumber_1.setProperty("value", server[0][0]/1000)
    ui.lcdNumber_2.setProperty("value", server[1][0]/1000)
    ui.lcdNumber_3.setProperty("value", server[2][0]/1000)
    
    ui.startProgress(newServer)
    orderQueue.pop()


class TimerHandler:
    @staticmethod
    def get_timer_by_list(progress_bar, time_list, num):
        first_timer = TimerHandler(progress_bar, time_list[0], num)
        post_timer = first_timer
        for i in range(1, len(time_list)):
            temp = TimerHandler(progress_bar, time_list[i], num)
            post_timer.enroll(temp)
            post_timer = temp

        return first_timer

    def __init__(self, progress_bar, full_time, num):
        self.timer = QTimer()
        self.progress_bar = progress_bar
        self.progress_cnt = 0
        self.tick_time = full_time / 1000;
        self.num = num
        self.enrolled_timer = None
        self.end_tag = False

        def timer_callback():
            self.progress_cnt += 0.1
            self.progress_bar.setProperty("value", self.progress_cnt)

            if self.progress_cnt >= 100:
                server[self.num][0] -= server[self.num][1]
                server[self.num].pop(1)
                ui.lcdNumber_1.setProperty("value", server[0][0]/1000)
                ui.lcdNumber_2.setProperty("value", server[1][0]/1000)
                ui.lcdNumber_3.setProperty("value", server[2][0]/1000)

                self.timer.stop()
                self.end()

        self.timer.timeout.connect(timer_callback)

    def start(self):
        self.timer.start(self.tick_time)

    def enroll(self, timer):
        self.enrolled_timer = timer

    def enroll_last(self, timer):
        if self.enrolled_timer is None:
            self.enrolled_timer = timer
            return

        now_timer = self.enrolled_timer

        while now_timer.enrolled_timer is not None:
            now_timer = now_timer.enrolled_timer

        now_timer.enrolled_timer = timer

    def end(self):
        self.progress_bar.setProperty("value", 0)
        if self.enrolled_timer is not None:
            self.enrolled_timer.start()
        self.end_tag = True

    def get_end_tag(self):
        if self.enrolled_timer is None:
            return self.end_tag

        now_timer = self.enrolled_timer

        while now_timer.enrolled_timer is not None:
            now_timer = now_timer.enrolled_timer

        return self.end_tag

    def getProgressCnt(self):
        return self.progress_cnt


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
        item.setFlags(
            QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsDragEnabled | QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsTristate)
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
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.progressBar_3 = QtGui.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(420, 400, 121, 21))
        self.progressBar_3.setProperty("value", 0)
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

        self.progress_timer_1 = None
        self.progress_timer_2 = None
        self.progress_timer_3 = None

    def startProgress(self, newServer):
        print(server)
        if(len(newServer[0]) != 0):
            temp_timer = TimerHandler.get_timer_by_list(self.progressBar_1, newServer[0][0:len(newServer[0])], 0)

            if(self.progress_timer_1 == None or self.progress_timer_1.get_end_tag()== True):
                self.progress_timer_1 = temp_timer
                self.progress_timer_1.start()
            else:
                self.progress_timer_1.enroll_last(temp_timer)

        if (len(newServer[1]) != 0):
            temp_timer = TimerHandler.get_timer_by_list(self.progressBar_2, newServer[1][0:len(newServer[1])], 1)

            if(self.progress_timer_2 == None or self.progress_timer_2.get_end_tag() == True):
                self.progress_timer_2 = temp_timer
                self.progress_timer_2.start()
            else:
                self.progress_timer_2.enroll_last(temp_timer)

        if (len(newServer[2]) != 0):
            temp_timer = TimerHandler.get_timer_by_list(self.progressBar_3, newServer[2][0:len(newServer[2])], 2)

            if(self.progress_timer_3 == None or self.progress_timer_3.get_end_tag()== True):
                self.progress_timer_3 = temp_timer
                self.progress_timer_3.start()
            else:
                self.progress_timer_3.enroll_last(temp_timer)

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
        item.setText(_translate("MainWindow", "3500\\", None))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("MainWindow", "2sec", None))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("MainWindow", "4000\\", None))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("MainWindow", "3sec", None))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("MainWindow", "4000\\", None))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("MainWindow", "4sec", None))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("MainWindow", "4500\\", None))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("MainWindow", "5sec", None))
        item = self.tableWidget.item(4, 0)
        item.setText(_translate("MainWindow", "5000\\", None))
        item = self.tableWidget.item(4, 1)
        item.setText(_translate("MainWindow", "6sec", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.textBrowser.setHtml(_translate("MainWindow",
                                            "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                            "p, li { white-space: pre-wrap; }\n"
                                            "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                            "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt;\">MENU</span></p></body></html>",
                                            None))
        self.pushButton.setText(_translate("MainWindow", "Order", None))
        self.textBrowser_2.setHtml(_translate("MainWindow",
                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                              "p, li { white-space: pre-wrap; }\n"
                                              "</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                              "<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">Progress Bar</span></p></body></html>",
                                              None))


if __name__ == "__main__":
    import sys

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
