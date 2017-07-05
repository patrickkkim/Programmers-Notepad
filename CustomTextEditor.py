import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QPlainTextEdit
from Geometry import Location
from FileManipulate import Action
from PopupAction import SaveAs, Open, SetDefaultDir, Find
from FileHandler import Core
from Configure import SetConf

class CustomTextEditor(QMainWindow):
	def __init__(self):
		super(self.__class__, self).__init__()
		self.conf = SetConf()
		self.conf.call()
		Core.title = "untitled"
		Core.directory = Core.defaultDir
		Core.mainWindow = self

		self.initUI()

	def initUI(self):
		self.winLocation = Location()

		self.setWindowTitle(Core.title)
		self.resize(700, 650)
		self.winLocation.moveToCenter()
		self.initTextBox()
		self.initAction()
		self.addMenu()

	def initTextBox(self):
		Core.textBox = QPlainTextEdit()
		Core.textBox.resize(self.size())
		self.setCentralWidget(Core.textBox)

	# Create actions for menu bar.
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

		self.setDefaultDirAction = QAction("Set Directory", self)
		self.setDefaultDirAction.triggered.connect(SetDefaultDir)
		self.setDefaultDirAction.triggered.connect(self.conf.save)

		self.findAction = QAction("Find", self)
		self.findAction.setShortcut("Ctrl+F")
		self.findAction.triggered.connect(Find)

	# Add a menu bar and connects actions appropriately.
	def addMenu(self):
		self.menuBar = self.menuBar()
		fileMenu = self.menuBar.addMenu("File")
		editMenu = self.menuBar.addMenu("Edit")

		# Define file menu actions
		fileMenu.addAction(self.quitAction)
		fileMenu.addAction(self.saveAction)
		fileMenu.addAction(self.saveAsAction)
		fileMenu.addAction(self.openAction)
		fileMenu.addAction(self.setDefaultDirAction)

		# Define edit menu actions
		editMenu.addAction(self.findAction)

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