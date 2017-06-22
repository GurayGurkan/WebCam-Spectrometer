# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui_1.ui'
#
# Created: Thu Jun 22 18:34:54 2017
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 380)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.figure2 = GraphicsView(self.centralwidget)
        self.figure2.setGeometry(QtCore.QRect(10, 20, 360, 120))
        self.figure2.setObjectName(_fromUtf8("figure2"))
        self.figure1 = PlotWidget(self.centralwidget)
        self.figure1.setGeometry(QtCore.QRect(10, 160, 360, 151))
        self.figure1.setObjectName(_fromUtf8("figure1"))
        self.buttonStart = QtGui.QPushButton(self.centralwidget)
        self.buttonStart.setGeometry(QtCore.QRect(380, 30, 60, 25))
        self.buttonStart.setObjectName(_fromUtf8("buttonStart"))
        self.buttonStop = QtGui.QPushButton(self.centralwidget)
        self.buttonStop.setGeometry(QtCore.QRect(380, 60, 60, 25))
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        self.gridLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(450, 30, 179, 80))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.sliderExpo = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderExpo.setMinimum(1)
        self.sliderExpo.setMaximum(7)
        self.sliderExpo.setOrientation(QtCore.Qt.Vertical)
        self.sliderExpo.setObjectName(_fromUtf8("sliderExpo"))
        self.gridLayout.addWidget(self.sliderExpo, 1, 1, 1, 1)
        self.sliderGain = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderGain.setMaximum(255)
        self.sliderGain.setOrientation(QtCore.Qt.Vertical)
        self.sliderGain.setObjectName(_fromUtf8("sliderGain"))
        self.gridLayout.addWidget(self.sliderGain, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.sliderBrigh = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderBrigh.setMinimum(0)
        self.sliderBrigh.setMaximum(255)
        self.sliderBrigh.setOrientation(QtCore.Qt.Vertical)
        self.sliderBrigh.setObjectName(_fromUtf8("sliderBrigh"))
        self.gridLayout.addWidget(self.sliderBrigh, 1, 2, 1, 1)
        self.sliderContr = QtGui.QSlider(self.gridLayoutWidget)
        self.sliderContr.setMaximum(255)
        self.sliderContr.setOrientation(QtCore.Qt.Vertical)
        self.sliderContr.setObjectName(_fromUtf8("sliderContr"))
        self.gridLayout.addWidget(self.sliderContr, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Spectrometer v1.0", None))
        self.buttonStart.setText(_translate("MainWindow", "Start", None))
        self.buttonStop.setText(_translate("MainWindow", "Stop", None))
        self.label.setText(_translate("MainWindow", "Gain", None))
        self.label_3.setText(_translate("MainWindow", "Bright.", None))
        self.label_2.setText(_translate("MainWindow", "Expo", None))
        self.label_4.setText(_translate("MainWindow", "Cont.", None))

from pyqtgraph import GraphicsView, PlotWidget

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

