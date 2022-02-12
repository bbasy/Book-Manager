from PyQt6 import QtCore, QtGui, QtWidgets
from View.inputView import Ui_inputView
from View.mainView import Ui_mainWindow
from Model.database import DB 

class main_View(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)

class input_View(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_inputView()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = main_View()

    input_View = input_View()
    input_View.hide()

    mainWindow.show()
    sys.exit(app.exec())
