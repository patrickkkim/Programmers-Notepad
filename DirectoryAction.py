import os
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QFileSystemModel, QTreeView, QHBoxLayout, QVBoxLayout
from Geometry import Location
from FileManipulate import Action
from ScreenHandler import Core

""" Viewer has two layouts: hBox and vBox. hBox for horizontal layouts and vBox for vertical layouts.
	Also has a QTreeView set with model.
"""
class DirectoryViewer(QDialog):
	def __init__(self):
		super(DirectoryViewer, self).__init__()

		self.title = ""
		self.initUI()
		self.exec_()

	def initUI(self):
		self.winLocation = Location()
		self.action = Action()
		self.hBox = QHBoxLayout()
		self.vBox = QVBoxLayout()

		self.setWindowTitle(self.title)
		self.resize(850, 600)
		Core.setMainWin(self)
		self.winLocation.moveToTopLeft()
		Core.restoreMainWin()

		self.initDirUI()
		self.setLayout(self.vBox)

	def initDirUI(self):
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

class SaveAs(DirectoryViewer):
	def __init__(self):
		super(SaveAs, self).__init__()

	def initDirUI(self):
		super(SaveAs, self).initDirUI()
		self.tree.setRootIndex(self.model.index(Core.defaultDir))
		self.tree.selectionModel().currentChanged.connect(self.setSelection)

		saveName = QLabel("Filename")
		self.saveNameEdit = QLineEdit()
		saveBtn = QPushButton("Save")
		cancelBtn = QPushButton("Cancel")

		self.saveNameEdit.setText(Core.title)
		saveBtn.clicked.connect(lambda func: self.setTitle(self.saveNameEdit.text()))
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
		self.title = "Save File As"
		super(SaveAs, self).initUI()

	def setSelection(self, index):
		super(SaveAs, self).setSelection(index)
		if os.path.isfile(self.selectedDir):
			self.saveNameEdit.setText(self.selectedTitle)

	def setDirSelected(self):
		dir = self.selectedDir
		if os.path.isdir(dir):
			Core.directory = dir
			self.action.save()
			self.action.close()
		else:
			Core.directory = dir[0 : dir.rfind("/")]

class Open(DirectoryViewer):
	def __init__(self):
		super(Open, self).__init__()

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
		self.title = "Open File"
		super(Open, self).initUI()

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