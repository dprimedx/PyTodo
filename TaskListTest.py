from Task import Task
from TaskList import TaskList

tl = TaskList()
tl.add(Task(0,"Walk the dog"))
tl.add(Task(0,"Clean desk",1))
tl.add(Task(0,"Wash sheets",0))
tl.add(Task(0,"Do homework",2))

for x in tl.getItems():
	print(x.id,x.desc)
