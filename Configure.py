from FileHandler import Core

DEFAULT_DIR = "#default_directory "
END_OF_LINE = ";"

""" Configure methods for saving Core variables as text file.
"""
class SetConf(object):
	def save(self):
		text = ""
		text += DEFAULT_DIR
		text += Core.defaultDir
		text += END_OF_LINE

		file = open("configure", "w")
		file.write(text)
		file.close()

	def create(self):
		Core.defaultDir = "/home/"
		self.save()

	def call(self):
		try:
			file = open("configure", "r")
		except IOError:
			self.create()
			return 0

		text = file.read()
		Core.defaultDir = text[(text.find(DEFAULT_DIR) + len(DEFAULT_DIR)) : text.find(END_OF_LINE)]