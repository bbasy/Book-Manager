from PyQt6 import QtCore, QtGui, QtWidgets
from Model.database import DB

db = DB()

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1164, 593)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.bookTable = QtWidgets.QTableWidget(self.centralwidget)
        self.bookTable.setGeometry(QtCore.QRect(10, 20, 1011, 521))
        self.bookTable.setObjectName("bookTable")
        self.bookTable.setColumnCount(6)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bookTable.setHorizontalHeaderItem(5, item)
        self.bookTable.horizontalHeader().setDefaultSectionSize(170)
        self.bookTable.verticalHeader().setVisible(False)
        self.loadData()

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

        item = self.bookTable.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "ID"))
        item = self.bookTable.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "ISBN"))
        item = self.bookTable.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Title"))
        item = self.bookTable.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Author"))
        item = self.bookTable.horizontalHeaderItem(4)
        item.setText(_translate("mainWindow", "Pages Read"))
        item = self.bookTable.horizontalHeaderItem(5)
        item.setText(_translate("mainWindow", "Total Pages"))

    # Opens insert view where users can type their book names/isbn
    def insertView(self):
        input_View.show() 

    def deleteItem(self):
        pass

    def clearTbl(self):
        pass

    def editItem(self):
        pass
    
    def loadData(self):
        # Dynamically sizes the table rows
        self.bookTable.setRowCount(len(db.view()))
        tableRow = 0
        for rows in db.view():
            self.bookTable.setItem(tableRow, 0, QtWidgets.QTableWidgetItem(str(rows[0])))
            self.bookTable.setItem(tableRow, 1, QtWidgets.QTableWidgetItem(str(rows[1])))
            self.bookTable.setItem(tableRow, 2, QtWidgets.QTableWidgetItem(rows[2]))
            self.bookTable.setItem(tableRow, 3, QtWidgets.QTableWidgetItem(rows[3]))
            self.bookTable.setItem(tableRow, 4, QtWidgets.QTableWidgetItem(str(rows[4])))
            self.bookTable.setItem(tableRow, 5, QtWidgets.QTableWidgetItem(str(rows[5])))
            tableRow += 1
