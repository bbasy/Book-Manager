import sys
sys.path.append("..")

from PyQt6 import QtCore, QtGui, QtWidgets
from Model.googleBooksAPI import booksAPI

class Ui_inputView(object):
    def setupUi(self, inputView):
        inputView.setObjectName("inputView")
        inputView.resize(394, 341)
        self.layoutWidget = QtWidgets.QWidget(inputView)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")

        self.isbnLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.isbnLabel.setFont(font)
        self.isbnLabel.setObjectName("isbnLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.isbnLabel)

        self.isbnInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.isbnInput.setObjectName("isbnInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.isbnInput)

        self.titleLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.titleLabel.setFont(font)
        self.titleLabel.setObjectName("titleLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.titleLabel)

        self.titleInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.titleInput.setObjectName("titleInput")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.titleInput)

        self.authorLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.authorLabel)

        self.authorInput = QtWidgets.QLineEdit(self.layoutWidget)
        self.authorInput.setObjectName("authorInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.authorInput)

        self.pagesRLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pagesRLabel.setFont(font)
        self.pagesRLabel.setObjectName("pagesRLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pagesRLabel)

        self.pagesRInput = QtWidgets.QSpinBox(self.layoutWidget)
        self.pagesRInput.setObjectName("pagesRInput")
        self.pagesRInput.setMinimum(0)
        self.pagesRInput.setMaximum(10000)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pagesRInput)

        self.pagesTotLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pagesTotLabel.setFont(font)
        self.pagesTotLabel.setObjectName("pagesTotLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.LabelRole, self.pagesTotLabel)

        self.pagesTotInput = QtWidgets.QSpinBox(self.layoutWidget)
        self.pagesTotInput.setObjectName("pagesTotInput")
        self.pagesTotInput.setMinimum(0)
        self.pagesTotInput.setMaximum(10000)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.ItemRole.FieldRole, self.pagesTotInput)

        self.buttonBox = QtWidgets.QDialogButtonBox(self.layoutWidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Cancel|QtWidgets.QDialogButtonBox.StandardButton.Help|QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.button(QtWidgets.QDialogButtonBox.StandardButton.Help).setText("Fill")
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.ItemRole.FieldRole, self.buttonBox)
        
        self.buttonBox.rejected.connect(lambda: self.cancelButton(inputView))
        self.buttonBox.helpRequested.connect(lambda: self.helpButton())


        self.isbnLabel.setBuddy(self.isbnInput)
        self.titleLabel.setBuddy(self.titleInput)
        self.authorLabel.setBuddy(self.authorInput)
        self.pagesRLabel.setBuddy(self.pagesRInput)
        self.pagesTotLabel.setBuddy(self.pagesTotInput)

        self.retranslateUi(inputView)
        QtCore.QMetaObject.connectSlotsByName(inputView)

    def retranslateUi(self, inputView):
        _translate = QtCore.QCoreApplication.translate
        inputView.setWindowTitle(_translate("inputView", "inputView"))
        self.isbnLabel.setText(_translate("inputView", "ISBN:"))
        self.titleLabel.setText(_translate("inputView", "Title:"))
        self.authorLabel.setText(_translate("inputView", "Author:"))
        self.pagesRLabel.setText(_translate("inputView", "Pages Read:"))
        self.pagesTotLabel.setText(_translate("inputView", "Total Pages:"))
        

    def okButton(self, inputView):
        pass
        
    def cancelButton(self, inputView):
        self.isbnInput.setText("")
        self.titleInput.setText("")
        self.authorInput.setText("")
        self.pagesRInput.setValue(0)
        self.pagesTotInput.setValue(0)
        inputView.close()

    def helpButton(self):
        self.checkInput()

    def checkInput(self):
        # List for the users input: [ISBN, Title, Author, Pages Read, Pages Total]
        self.inputData = []
        self.queryData = ""
        self.inputData.append(self.isbnInput.text())
        self.inputData.append(self.titleInput.text())
        self.inputData.append(self.authorInput.text())
        self.inputData.append(self.pagesRInput.value())
        self.inputData.append(self.pagesTotInput.value())
        self.book = booksAPI()
        # Excludes pages read and pages total from being indexed
        self.getQueryData = True
        for i in range(0, 3):
            # Get information to query by searching for first field that is not blank
            if self.inputData[i] != "" and self.getQueryData:
                self.queryData = self.inputData[i]
                self.getQueryData = False

        for x in range(0, 5):
            # Fill blank information with information received from query
            if self.inputData[x] == "":
                match x:
                    case 0:
                        self.isbnInput.setText(self.book.searchISBN(self.queryData))
                        break;
                    
                    case 1:
                        self.titleInput.setText(self.book.search(self.queryData, "title"))
                        break;
                    
                    case 2:
                        self.authorInput.setText(self.book.searchAuthor(self.queryData))
                        break;

            if self.inputData[4] == 0:
                self.pagesTotInput.setValue(self.book.search(self.queryData, "pageCount"))
