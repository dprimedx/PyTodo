class TaskList(list):
	def __init__(self):
		self.items = []
	def add(self,item):
		if item is not None:
			self.items.append(item)
	def getItems(self):
		return self.items
