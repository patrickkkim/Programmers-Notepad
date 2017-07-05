from PyQt5.QtWidgets import QMainWindow, QApplication

""" ScreenHandler::Core Class for storing static variables.
Core mainWindow should always be restored whenever it's done using it.
Use setter and restore methods for swapping mainWindow.
Other static variables should only be altered at the final stage of manipulation. 
Never alter static variables while manipulating files.
"""
class Core(QMainWindow):
	def __init__(self):
		super(Core, self).__init__()
		self.mainWindow
		self.textBox
		self.title
		self.directory
		self.defaultDir

	@classmethod
	def setMainWin(self, cls):
		self.restore = Core.mainWindow
		Core.mainWindow = cls

	@classmethod
	def restoreMainWin(self):
		Core.mainWindow = self.restore
		Core.mainWindow.changeTitle()