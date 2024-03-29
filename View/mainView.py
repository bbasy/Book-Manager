from PyQt6 import QtCore, QtGui, QtWidgets
from Model.database import DB
from View.inputView import Ui_inputView
from Model import config

db = DB()

class input_View(QtWidgets.QDialog, Ui_inputView):
    def __init__(self, parent=None):
        super(input_View, self).__init__(parent)
        self.ui = Ui_inputView()
        self.ui.setupUi(self)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1164, 593)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bookTable = QtWidgets.QTableView(self.centralwidget)
        self.bookTable.setGeometry(QtCore.QRect(10, 20, 1011, 521))
        self.bookTable.setObjectName("bookTable")
        self.bookTable.horizontalHeader().setDefaultSectionSize(170)
        self.bookTable.verticalHeader().setVisible(False)

        self.insertItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.insertItemBtn.setGeometry(QtCore.QRect(1030, 20, 121, 122))
        self.insertItemBtn.setObjectName("insertItemBtn")
        self.insertItemBtn.clicked.connect(self.insertView)

        self.deleteItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteItemBtn.setGeometry(QtCore.QRect(1030, 150, 121, 122))
        self.deleteItemBtn.setObjectName("deleteItemBtn")

        self.clearBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clearBtn.setGeometry(QtCore.QRect(1030, 420, 121, 122))
        self.clearBtn.setObjectName("clearBtn")

        self.editItemBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editItemBtn.setGeometry(QtCore.QRect(1030, 280, 121, 125))
        self.editItemBtn.setObjectName("editItemBtn")

        mainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(mainWindow)
        self.statusBar.setObjectName("statusBar")
        mainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Library Manager"))
        self.insertItemBtn.setText(_translate("mainWindow", "Insert Book"))
        self.deleteItemBtn.setText(_translate("mainWindow", "Delete Selected"))
        self.clearBtn.setText(_translate("mainWindow", "Clear Table"))
        self.editItemBtn.setText(_translate("mainWindow", "Edit Field"))

    # Opens insert view where users can type their book names/isbn
    def insertView(self):
        inputWindow = input_View()
        inputWindow.show()

    def deleteItem(self):
        pass

    def clearTbl(self):
        pass

    def editItem(self):
        pass

    def updateView(self):
        pass
