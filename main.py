from PyQt6 import QtCore, QtGui, QtWidgets, QtSql
from View.inputView import Ui_inputView
from View.mainView import Ui_mainWindow
from Model import config
from Model.database import DB 

class main_View(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(QtWidgets.QMainWindow, self).__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        # Watcher to update view when model is changed
        self.fs_watcher = QtCore.QFileSystemWatcher(['books.db'])
        self.fs_watcher.fileChanged.connect(self.file_changed)
        # Model is loaded into book table
        self.model = QtSql.QSqlTableModel()
        self.model.setTable("Books")
        self.ui.bookTable.setModel(self.model)
        self.model.select()

    def file_changed(self):
        self.model.select()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName("./books.db")
    if not db.open():
        sys.exit(-1)

    mainWindow = main_View()

    mainWindow.show()
    sys.exit(app.exec())
