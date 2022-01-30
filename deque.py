class deque:
    	def __init__(self,s):
		self.items=list(s)
		self.front=0
	def append(self,c):
		self.items.append(c)
	def appendleft(self,c):
		self.itmes.insert(self.front,c)
	def pop(self):
		try:
			return self.items.pop()
		except IndexErorr:
			return False
	def popleft(self):
		if self.front>=len(self.items):
			return False
		else:
			x=self.items[self.front]
			self.front+=1
			return x
	def __len__(self):
		return len(self.items)-self.front
	def right(self):
		try:
			return self.items[-1]
		except IndexError:
			return False
	def left(self):
		if self.front>=len(self.items):
			return False
		else:
			return self.items[self.front]

def check_palindrome(s):
	dq=deque(s)
	palindrome=True
	while len(dq)>1:
		if dq.popleft()!=dq.pop():
			palindrome=False
	return palindrome

x=input()
print(check_palindrome(x))