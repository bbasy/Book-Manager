from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from View.inputView import Ui_inputView
from View.mainView import Ui_mainWindow
from Model.database import DB 

class main_View(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # Model is loaded into book table
        self.ui.bookTable.setModel(model)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./books.db")
    if not db.open():
        sys.exit(-1)

    model = QtSql.QSqlTableModel()
    model.setTable("Books")
    model.select()

    mainWindow = main_View()

    mainWindow.show()
    sys.exit(app.exec())
