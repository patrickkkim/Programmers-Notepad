import os
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QFileSystemModel, QTreeView, QHBoxLayout, QVBoxLayout
from Geometry import Location
from FileManipulate import Action
from ScreenHandler import Core

""" Viewer has two layouts: hBox and vBox. hBox for horizontal layouts and vBox for vertical layouts.
	Also has a QTreeView set with model.
"""
class Popup(QDialog):
	def __init__(self, title, width, height):
		super(Popup, self).__init__()

		self.title = title
		self.width = width
		self.height = height

		self.initUI()
		self.exec_()

	def initUI(self):
		self.winLocation = Location()
		self.action = Action()
		self.hBox = QHBoxLayout()
		self.vBox = QVBoxLayout()

		self.setWindowTitle(self.title)
		self.resize(self.width, self.height)
		Core.setMainWin(self)
		self.winLocation.moveToCenter()
		Core.restoreMainWin()

		self.setLayout(self.vBox)

	def initDirUI(self):
		Core.directory = Core.defaultDir
		self.model = QFileSystemModel()
		self.tree = QTreeView()

		self.model.setRootPath('')
		self.tree.setModel(self.model)
		self.tree.setColumnWidth(0, 450)

	def setTitle(self, title):
		Core.title = title

	def setSelection(self, index):
		self.selectedDir = self.tree.selectionModel().model().filePath(index)
		self.selectedTitle = self.tree.selectionModel().model().fileName(index)

class SaveAs(Popup):
	def __init__(self):
		super(SaveAs, self).__init__("Save file as", 800, 500)

	def initDirUI(self):
		super(SaveAs, self).initDirUI()
		self.tree.setRootIndex(self.model.index(Core.defaultDir))
		self.tree.selectionModel().currentChanged.connect(self.setSelection)

		saveName = QLabel("Filename")
		self.saveNameEdit = QLineEdit()
		saveBtn = QPushButton("Save")
		cancelBtn = QPushButton("Cancel")

		self.saveNameEdit.setText(Core.title)

		saveBtn.clicked.connect(lambda func: Core.setMainWin(self))
		saveBtn.clicked.connect(self.setDirSelected)
		saveBtn.clicked.connect(Core.restoreMainWin)
		cancelBtn.clicked.connect(lambda func: Core.setMainWin(self))
		cancelBtn.clicked.connect(self.action.close)
		cancelBtn.clicked.connect(Core.restoreMainWin)

		self.hBox.addWidget(saveName)
		self.hBox.addWidget(self.saveNameEdit)
		self.hBox.addWidget(saveBtn)
		self.hBox.addWidget(cancelBtn)

		self.vBox.addWidget(self.tree) 
		self.vBox.addLayout(self.hBox)

	def initUI(self):
		super(SaveAs, self).initUI()
		self.initDirUI()

	def setSelection(self, index):
		super(SaveAs, self).setSelection(index)
		if os.path.isfile(self.selectedDir):
			self.saveNameEdit.setText(self.selectedTitle)

	def setDirSelected(self):
		dir = self.selectedDir

		if os.path.isdir(dir):
			Core.directory = dir
		else:
			Core.directory = dir[0 : dir.rfind("/")]

		Core.title = self.saveNameEdit.text()
		self.action.save()
		self.action.close()

class Open(Popup):
	def __init__(self):
		super(Open, self).__init__("Open file", 800, 500)

	def initDirUI(self):
		super(Open, self).initDirUI()
		self.tree.setRootIndex(self.model.index(Core.defaultDir))
		self.tree.selectionModel().currentChanged.connect(self.setSelection)

		openBtn = QPushButton("Open")
		cancelBtn = QPushButton("Cancel")

		openBtn.clicked.connect(lambda func: Core.setMainWin(self))
		openBtn.clicked.connect(self.setDirSelected)
		openBtn.clicked.connect(Core.restoreMainWin)
		openBtn.clicked.connect(lambda func: self.setTitle(Core.title))
		cancelBtn.clicked.connect(lambda func: Core.setMainWin(self))
		cancelBtn.clicked.connect(self.action.close)
		cancelBtn.clicked.connect(Core.restoreMainWin)

		self.hBox.addWidget(openBtn)
		self.hBox.addWidget(cancelBtn)

		self.vBox.addWidget(self.tree)
		self.vBox.addLayout(self.hBox)

	def initUI(self):
		super(Open, self).initUI()
		self.initDirUI()

	def setDirSelected(self):
		dir = self.selectedDir
		if os.path.isdir(dir):
			if self.tree.isExpanded(self.model.index(dir)):
				expand = False
			else:
				expand = True
			self.tree.setExpanded(self.model.index(dir), expand)
		else:
			Core.directory = dir[0 : dir.rfind("/")]
			Core.title = self.selectedTitle
			self.action.open()
			self.action.close()

class Find(Popup):
	def __init__(self):
		super(Find, self).__init__("Find", 500, 50)

	def initUI(self):
		super(Find, self).initUI()
		
		findLabel = QLabel("Find with")
		findEdit = QLineEdit()
		findBtn = QPushButton("Find")
		cancelBtn = QPushButton("Cancel")

		findBtn.clicked.connect(lambda func: self.action.find(findEdit.text()))
		cancelBtn.clicked.connect(lambda fucn: Core.setMainWin(self))
		cancelBtn.clicked.connect(self.action.close)
		cancelBtn.clicked.connect(Core.restoreMainWin)

		self.hBox.addWidget(findLabel)
		self.hBox.addWidget(findEdit)
		self.hBox.addWidget(findBtn)
		self.hBox.addWidget(cancelBtn)

		self.vBox.addLayout(self.hBox)