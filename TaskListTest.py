from Task import Task
from TaskList import TaskList

tl = TaskList()
tl.add(Task("Walk the dog"))
tl.add(Task("Clean desk",1))

for x in tl.getItems():
	print(x.desc)
