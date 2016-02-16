#!/usr/bin/python -tt

class SimpleClass:
	truth = False
	def __init__(self, iterable):
		self.items_list = []
		self.__update(iterable)

	def update(self, iterable):
		for item in iterable:
			self.items_list.append(item)

	__update = update

class SubClass(SimpleClass):
	def update(self, keys, values):
		for item in zip(keys, values):
			self.items_list.append(item)
		SimpleClass.truth = True	

x = SimpleClass(['L','M','N'])
x.update('O')
print x.items_list

y = SubClass(['H','I','J','K','L'])
y.update('5','N')
y.update('6', 'O')
print y.items_list
print y.items_list[2]
x.update('P')
print x.items_list
print x.truth