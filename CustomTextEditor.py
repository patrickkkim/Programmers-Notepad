import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPlainTextEdit
from Geometry import Location
from FileManipulate import Action
from DirectoryAction import SaveAs, Open
from FindAction import Find
from ScreenHandler import Core

class CustomTextEditor(QMainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		Core.title = "untitled"
		Core.defaultDir = "/home/patkim/Documents/"
		Core.directory = Core.defaultDir
		Core.mainWindow = self

		self.initUI()

	# Initializes the main UI.
	def initUI(self):
		self.winLocation = Location()

		self.setWindowTitle(Core.title)
		self.resize(700, 650)
		self.winLocation.moveToCenter()
		self.initTextBox()
		self.initAction()
		self.addMenu()

	# Generates a text box
	def initTextBox(self):
		Core.textBox = QPlainTextEdit()
		Core.textBox.resize(self.size())
		self.setCentralWidget(Core.textBox)

	# Generates actions for menu bar.
	def initAction(self):
		self.action = Action()

		self.quitAction = QAction("Quit Application", self)
		self.quitAction.setShortcut("Ctrl+Q")
		self.quitAction.triggered.connect(self.action.quit)

		self.saveAction = QAction("Save", self)
		self.saveAction.setShortcut("Ctrl+S")
		self.saveAction.triggered.connect(self.isFileSavedEvent)

		self.saveAsAction = QAction("Save As", self)
		self.saveAsAction.setShortcut("Ctrl+Shift+S")
		self.saveAsAction.triggered.connect(SaveAs)

		self.openAction = QAction("Open", self)
		self.openAction.setShortcut("Ctrl+O")
		self.openAction.triggered.connect(Open)

		self.findAction = QAction("Find", self)
		self.findAction.setShortcut("Ctrl+F")
		self.findAction.triggered.connect(Find)

	# Generates a menu bar and adds actions accordingly.
	def addMenu(self):
		self.menuBar = self.menuBar()
		fileMenu = self.menuBar.addMenu('&File')
		fileMenu.addAction(self.quitAction)
		fileMenu.addAction(self.saveAction)
		fileMenu.addAction(self.saveAsAction)
		fileMenu.addAction(self.openAction)
		fileMenu.addAction(self.findAction)

	def isFileSavedEvent(self):
		if Core.title == "untitled":
			SaveAs()
		else:
			self.action.save()

	def changeTitle(self):
		self.setWindowTitle(Core.title)

if __name__ == '__main__':
	app = QApplication(sys.argv)
	myApp = CustomTextEditor()
	myApp.show()
	sys.exit(app.exec_())