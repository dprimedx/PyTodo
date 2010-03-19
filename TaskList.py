class TaskList:
	def __init__(self):
		self.items = []
		self.currentID = 0

	def add(self,item):
		if item is not None:
			self.currentID += 1
			item.id = self.currentID
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

	def getByID(self,id=-1):
		if id > -1:
			for x in self.items:
				if x.id == id:
					return x
