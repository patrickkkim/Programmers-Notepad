from PyQt5.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel, QPushButton
from ScreenHandler import Core
from Geometry import Location
from FileManipulate import Action

class Find(QDialog):
	def __init__(self):
		super(Find, self).__init__()
		self.title = "Find Things"
		self.initUI()
		self.exec_()

	def initUI(self):
		self.winLocation = Location()
		self.action = Action()
		self.vBox = QVBoxLayout()
		self.hBox = QHBoxLayout()
 
		self.setWindowTitle(self.title)
		self.resize(450, 50)
		Core.setMainWin(self)
		self.winLocation.moveToCenter()
		Core.restoreMainWin()

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
		self.setLayout(self.vBox)