class Stack:
	def __init__(self):
		self.items=[]
	def push(self,val):
		self.items.append(val)
	def pop(self):
		try:
			return self.items.pop()
		except IndexError:
			return False
	def __len__(self):
		return len(self.items)
	def isEmpty(self):
		return len(self.itmes)==0
	def istop(self):
		try:
			return self.items[-1]
		except IndexError:
			return False
	

def compute_postfix(postfix):
	operand=Stack()
	postfix_lst=postfix.split()
	for token in postfix_lst:
		if token in '+-*/^':
			x=operand.pop()
			y=operand.pop()
			if token=='+':
				operand.push(x+y)
			elif token=='-':
				operand.push(y-x)
			elif token=='*':
				operand.push(x*y)
			elif token=='/':
				operand.push(y/x)
			else:
				result=1
				for i in range(x):
					result*=y
				operand.push(result)
		else:
			operand.push(int(token))
	return operand.pop()

postfix=input()
result=compute_postfix(postfix)
print("%.4f"%result)