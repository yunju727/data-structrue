class Stack:
    def __init__(self):
	    self.stack=[]
	
	def push(self,val):
		self.stack.append(val)
	
	def pop(self):
		try:
			self.stack.pop()
		except IndexError:
			return False
	
	def top(self):
		try:
			return self.stack[-1]
		except:
			return False
	
	def __len__(self):
		return len(self.stack)
	
	def isEmpty(self):
		return len(self)==0

# pseudo code
def parChecker(parSeq):
	k=Stack()
	for i in parSeq:
		if i=="(":
			k.push(i)
		elif i==")":
			if k.isEmpty()==True:
				return False
			else:
				k.pop()
	if len(k)>0:
		return False
	else:
		return True
	
x=input()

print(parChecker(x))