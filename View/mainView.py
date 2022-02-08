from PyQt6 import QtCore, QtGui, QtWidgets


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

        self.insertItemBtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.insertView())
        self.insertItemBtn.setGeometry(QtCore.QRect(1030, 20, 121, 122))
        self.insertItemBtn.setObjectName("insertItemBtn")

        self.deleteItemBtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.deleteItem())
        self.deleteItemBtn.setGeometry(QtCore.QRect(1030, 150, 121, 122))
        self.deleteItemBtn.setObjectName("deleteItemBtn")

        self.clearBtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.clearTbl())
        self.clearBtn.setGeometry(QtCore.QRect(1030, 420, 121, 122))
        self.clearBtn.setObjectName("clearBtn")

        self.editItemBtn = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.editItem())
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
    
    def deleteItem(self):

    def clearTbl(self):

    def editItem(self):


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec())
