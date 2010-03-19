class TaskList:
	def __init__(self):
		self.items = []
	def add(self,item):
		if item is not None:
			self.items.append(item)
	def getItems(self):
		return self.items
	def getByPriority(self,priority=None):
		if priority is None:
			return self.items
		result = []
		for x in self.items:
			if x.priority == priority:
				result.append(x)
		return result
