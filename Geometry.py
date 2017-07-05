from PyQt5.QtWidgets import QDesktopWidget
from ScreenHandler import Core

class Location(object):

	# Sets the center point of the user's screen and move the Editor to it.
	def moveToCenter(self):
		qtRectangle = Core.mainWindow.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().center()
		qtRectangle.moveCenter(centerPoint)
		Core.mainWindow.move(qtRectangle.topLeft())

	def moveToTopLeft(self):
		qtRectangle = Core.mainWindow.frameGeometry()
		centerPoint = QDesktopWidget().availableGeometry().topLeft()
		qtRectangle.moveCenter(centerPoint)
		Core.mainWindow.move(qtRectangle.topLeft())