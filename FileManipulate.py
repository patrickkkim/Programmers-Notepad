import os
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QMessageBox
from ScreenHandler import Core

# Action methods for wiring buttons or menues
class Action(object):
	def quit(self):
		quitMsg = "Are you sure?"
		reply = QMessageBox.question(Core.mainWindow, 'Message', quitMsg, QMessageBox.Yes, QMessageBox.No)

		if reply == QMessageBox.Yes:
			QCoreApplication.exit()

	def close(self):
		Core.mainWindow.close()

	def save(self):
		text = Core.textBox.toPlainText()
		file = open(Core.directory + "/" + Core.title, 'w')
		file.write(text)
		file.close()

	def open(self):
		file = open(Core.directory + "/" + Core.title, 'r')
		Core.textBox.document().setPlainText(file.read())
		file.close()

	def find(self, word):
		Core.textBox.find(word)

	def selectAll(self):
		pass

	def copy(self):
		pass

	def paste(self):
		pass

	def cut(self):
		pass

