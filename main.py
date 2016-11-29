# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from queue import Queue
import threading, time, random

orderQueue = list();

server = [[0], [0], [0]]

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
    beverage = [0,0,0,0,0]
    beverageCost = [2000, 3000, 4000, 5000, 6000]

    totalOfOrder = 0

    def  SetTotalOrder(self):
        self.totalOfOrder = self.beverage[0] + self.beverage[1] + self.beverage[2] + self.beverage[3] + self.beverage[4]


def WhoIsServerWhenZero(tempOrder):
    minCost = 987654321
    minServer = -1
    maxCost = -1
    maxServer = -1
    beverCost = -1

    for i in range(0, 5):
        if tempOrder.beverage[4-i] != 0 :
            beverCost = tempOrder.beverageCost[4-i]
            break

    for i in range(0, 3):
        if maxCost < server[i][0] :
            maxCost = server[i][0]
            maxServer = i

    for i in range(0, 3):
        if minCost > server[i][0] and server[i][0] + beverCost <= server[maxServer][0] :
            minCost = server[i][0]
            minServer = i

    return minServer


def DistributeOrder():
    tempOrder = orderQueue[0];
    newServer = [[], [], []]

    for i in range(0, tempOrder.totalOfOrder):
        idx = WhoIsServerWhenZero(tempOrder)

        if (tempOrder.beverage[4] != 0):
            server[idx].append(tempOrder.beverageCost[4])
            newServer[idx].append(tempOrder.beverageCost[4])
            server[idx][0] += tempOrder.beverageCost[4]
            tempOrder.beverage[4] -= 1
            continue

        if (tempOrder.beverage[3] != 0):
            server[idx].append(tempOrder.beverageCost[3])
            newServer[idx].append(tempOrder.beverageCost[3])
            server[idx][0] += tempOrder.beverageCost[3]
            tempOrder.beverage[3] -= 1
            continue

        if (tempOrder.beverage[2] != 0):
            server[idx].append(4000)
            newServer[idx].append(4000)
            server[idx][0] += tempOrder.beverageCost[2]
            tempOrder.beverage[2] -= 1
            continue

        if (tempOrder.beverage[1] != 0):
            server[idx].append(3000)
            newServer[idx].append(3000)
            server[idx][0] += tempOrder.beverageCost[1]
            tempOrder.beverage[1] -= 1
            continue

        if (tempOrder.beverage[0] != 0):
            server[idx].append(2000)
            newServer[idx].append(2000)
            server[idx][0] += tempOrder.beverageCost[0]
            tempOrder.beverage[0] -= 1
            continue

    ui.lcdNumber_1.setProperty("value", server[0][0] / 1000)
    ui.lcdNumber_2.setProperty("value", server[1][0] / 1000)
    ui.lcdNumber_3.setProperty("value", server[2][0] / 1000)

    ui.startProgress(newServer)
    orderQueue.pop()


class Timer:
    def __init__(self, full_time, timer_callback):
        self.timer = QTimer()
        self.tick_time = full_time / 1000;
        self.timer.timeout.connect(timer_callback)

    def start(self):
        self.timer.start(self.tick_time)

class TimerHandler:
    def __init__(self, progress_bar, handler_num):
        self.progress_cnt = 0
        self.progress_bar = progress_bar
        self.now_timer = None
        self.handler_num = handler_num
        self.queue = Queue()
        self.run_flag = False

    def start(self):
        if self.now_timer is None or self.run_flag:
            return None
        elif not self.run_flag:
            self.now_timer.start()
            self.run_flag = True

    def timer_callback(self):
        self.progress_cnt += 0.1
        self.progress_bar.setProperty("value", self.progress_cnt)

        if self.progress_cnt >= 100:
            server[self.handler_num][0] -= server[self.handler_num][1]
            server[self.handler_num].pop(1)
            ui.lcdNumber_1.setProperty("value", server[0][0] / 1000)
            ui.lcdNumber_2.setProperty("value", server[1][0] / 1000)
            ui.lcdNumber_3.setProperty("value", server[2][0] / 1000)

            self.end()

    def push_back(self, full_time_list):
        print(full_time_list)
        for full_time in full_time_list:
            if self.now_timer is None:
                print(1)
                self.now_timer = Timer(full_time, self.timer_callback)
            else:
                print(2)
                self.queue.put(Timer(full_time, self.timer_callback))

    def end(self):
        self.progress_cnt = 0
        self.progress_bar.setProperty("value", self.progress_cnt)

        if self.queue.qsize() == 0:
            self.now_timer = None
            self.run_flag = False
        else:
            self.now_timer = self.queue.get()
            self.now_timer.start()

    def get_progress_cnt(self):
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

        self.progress_timer_1 = TimerHandler(self.progressBar_1, 0)
        self.progress_timer_2 = TimerHandler(self.progressBar_2, 1)
        self.progress_timer_3 = TimerHandler(self.progressBar_3, 2)

    def startProgress(self, newServer):
        print(newServer)
        if (len(newServer[0]) != 0):
            self.progress_timer_1.push_back(newServer[0][0:len(newServer[0])])
            self.progress_timer_1.start()

        if (len(newServer[1]) != 0):
            self.progress_timer_2.push_back(newServer[1][0:len(newServer[1])])
            self.progress_timer_2.start()

        if (len(newServer[2]) != 0):
            self.progress_timer_3.push_back(newServer[2][0:len(newServer[2])])
            self.progress_timer_3.start()

    def spinBoxValue(self):
        order = Order()
        order.beverage[0] = self.spinBox.value()
        order.beverage[1] = self.spinBox_2.value()
        order.beverage[2] = self.spinBox_3.value()
        order.beverage[3] = self.spinBox_4.value()
        order.beverage[4] = self.spinBox_5.value()
        self.spinBox.setProperty("value", 0)
        self.spinBox_2.setProperty("value", 0)
        self.spinBox_3.setProperty("value", 0)
        self.spinBox_4.setProperty("value", 0)
        self.spinBox_5.setProperty("value", 0)

        order.SetTotalOrder()
        orderQueue.append(order)
        print(order.beverage)
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
