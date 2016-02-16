#!/usr/bin/python -tt
class Main:
	truth = 0

	def __init__(self):
		return

	def update(self):
		if Main.truth == 0:
			Main.truth = 1
		elif Main.truth ==1:
			Main.truth = 0

class SubMain:
	def __init__(self):
		self.main = Main()

	def callMainUpdate(self):
		Main().update()

	def callTruth(self):
		self.main.truth = 1
		
a = Main()
b = SubMain()
b.callMainUpdate()
print a.truth
a.update()
print a.truth
b.callTruth()
print a.truth