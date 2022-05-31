class Student:
    def __init__(self,no,name,dept,grade,result=None):
        self.st_no=no
        self.name=name
        self.dept=dept
        self.grade=grade
        self.result=result

class TNode:
    def __init__(self,s,left=None,right=None):  #s는 student
        self.key=s.st_no
        self.value=[s.name,s.dept,s.grade,s.result]
        self.left=left
        self.right=right

class Course:
    count=0
    def __init__(self):
        self.root=None

    
    def search(self,key):
        return self.searchSubtree(self.root,key)
    
    def searchSubtree(self,node,key):
        if node==None:return None
        elif key==node.key:return node
        elif key<node.key:return self.searchSubtree(node.left,key)
        else:return self.searchSubtree(node.right,key)
    
    def minNode(self,node):
        if node.left==None:return node
        else:return self.minNode(node.left)
    
    def register(self,s):   #s가 student객체
        self.root=self.insertSubtree(self.root,s)
    
    def insertSubtree(self,node,s):
        if node==None:return TNode(s)
        elif s.st_no<node.key:node.left=self.insertSubtree(node.left,s)
        elif s.st_no>node.key:node.right=self.insertSubtree(node.right,s)
        else:pass
        return node
    
    def withdraw(self,key):
        self.root=self.deleteSubtree(self.root,key)
    
    def deleteSubtree(self,node,key):
        if node==None:return None
        if key<node.key:
            node.left=self.deleteSubtree(node.left,key)
            return node
        elif key>node.key:
            node.right=self.deleteSubtree(node.right,key)
            return node
        else:
            if node.right==None:# 오른쪽 서브트리가 없는경우
                return node.left
            if node.left==None: #왼쪽 서브트리가 없는 경우
                return node.right
        minR=self.minNode(node.right)
        node.key=minR.key
        node.value=minR.value
        node.right=self.deleteSubtree(node.right,minR.key)
        return node
    
    def modify(self,key,result):
        student=self.search(key)
        if student==None:return None
        else:
            student.value[3]=result
            return True

    def deptcount(self,v,dept):
        self.deptprint(v.left,dept)
        if v.value[1]==dept:
            count+=1
        self.deptprint(v.right,dept)
        return count

    
    def deptprint(self,v,dept):
        if v!=None:
            self.deptprint(v.left,dept)
            if v.value[1]==dept:
                print(v.key,end=' ')
                for i in v.value:
                    if i==None:continue
                    else:print(i,end=' ')
                print()
            self.deptprint(v.right,dept)

    def infoprint(self,v):
        if v!=None:
            self.infoprint(v.left)
            print(v.key,end=' ')
            for i in v.value:
                if i==None:continue
                else:print(i,end=' ')
            print()
            self.infoprint(v.right)

lec=Course()

while True:
    cmd=input().split()
    if cmd[0]=='Q':break
    elif cmd[0]=='N':
        tmp=lec.search(cmd[1])
        if tmp!=None:
            print('error1')
        else:
            s=Student(cmd[1],cmd[2],cmd[3],cmd[4])
            lec.register(s)
    elif cmd[0]=='G':
        tmp=lec.search(cmd[1])
        if tmp==None:print('error2')
        else:
            lec.modify(cmd[1],cmd[2])
    elif cmd[0]=='C':
        tmp=lec.search(cmd[1])
        if tmp==None:print('error2')
        else:
            lec.withdraw(cmd[1])
    elif cmd[0]=='R':
        tmp=lec.search(cmd[1])
        if tmp==None:print('error2')
        else:
            print(tmp.key,end=' ')
            for i in tmp.value:
                if i==None:continue
                else:
                    print(i,end=' ')
    elif cmd[0]=='D':
        lec.deptprint(lec.root,cmd[1])
    elif cmd[0]=='P':
        lec.infoprint(lec.root)

