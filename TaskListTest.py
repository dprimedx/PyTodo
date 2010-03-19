from Task import Task
from TaskList import TaskList

tl = TaskList()
tl.add(Task("Walk the dog"))
tl.add(Task("Clean desk",1))
tl.add(Task("Wash sheets",0))
tl.add(Task("Do homework",2))

for x in tl.getByPriority():
	print(x.desc)
