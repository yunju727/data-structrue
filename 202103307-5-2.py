class Node:
    def __init__(self,e=None):
        self.addr=e
        self.next=None
        self.back=None

#이중 연결 리스트 구현 - 삽입, 삭제, 탐색 연산까지.

class DLinkedList:
    def __init__(self):
        self.head=Node()   #head는 빈 노드로 설정한다.
    def isEmpty(self):
        return self.head.addr==None
    def size(self): #원소 개수를 반환해주는 함수
        if self.isEmpty():return 0  #isEmpty가 0이면 0개
        x=self.head #head에서부터 원소개수를 센다
        c=0 #c에 원소 개수를 저장
        while x.addr!=None: #x의 데이터가 None일때 까지 센다.
            c+=1
            x=x.next
        return c
    def getNode(self,location): #location에 위치한 node를 찾는다
        if location<0:return None   #location이 0보다 작으면 None을 반환
        node=self.head  #head에서 부터 시작
        while location>0 and node!=None:    #locatoin이 0보다 크고, node가 None이 아닐때 까지 반복
            node=node.next
            location-=1 #반복문을 한 번 돌 때, location을 1씩 줄인다
        return node
    def getEntry(self,location):    #location에 위치한 node의 데이터를 반환해준다.
        node=self.getNode(location) #getNode로 location에 위치한 node를 저장한다.
        if node==None:return None   #그런데 node가 None인 경우, 노드에 저장된 데이터는 없으므로 None을 반환한다.
        else:return node.addr   #
    def insert(self,e,location):    #location에 위치한 노드의 앞에 e의 데이터를 가진 노드를 삽입
        newNode=Node(e) #매개변수로 받은 데이터값을 가지는 Node를 생성한다.
        loc=self.getNode(location)  #getNode를 이용하여 삽입할 위치에 있는 Node를 찾아준다.
        newNode.back=loc.back   #삽입될 노드의 뒷노드를 loc의 뒷 노드로 설정
        newNode.next=loc    #삽입될 노드의 다음 노드를 loc 으로 설정 
        if loc.back==None:  #loc의 뒤에 위치한 노드가 없으면 loc이 현재 헤드노드인 것이므로
            self.head=newNode   #head노드를 삽입할 노드로 바꾼다.
        else:   #그렇지 않으면
            loc.back.next=newNode   #loc의 뒷노드의 next가 삽입할 노드를 가리키도록 한다.
        loc.back=newNode    #loc의 뒤에 연결될 노드를 삽입할 노드로 바꾼다.
    def remove(self,location):  #location에 위치한 노드를 삭제
        loc=self.getNode(location)  #getNode를 통해 location에 위치한 노드를 얻는다.
        if loc.back==None:  #loc이 헤드노드이면
            self.head=loc.next  #헤드노드를 loc의 다음노드로 바꿔준다.
            if loc.next!=None:  #loc의 다음노드가 존재하면
                loc.next.back=None  #loc의 다음노드의 back을 None으로 바꾸어 준다.
        else:   #loc이 헤드노드가 아니면
            loc.back.next=loc.next  #loc의 뒷 노드의 next를 loc의 다음노드를 가리키게 한다.
            if loc.next!=None:  #loc의 다음 노드가 존재하면
                loc.next.back=loc.back  #loc의 다음노드의 back을 loc의 뒷노드로 바꾸어 준다.
    def printList(self):    #연결리스트의 원소를 -로 구분하여 출력한다.
        node=self.head
        while node!=None:
            print(node.addr,end='-')
            node=node.next
        print()

class addrList:
    def __init__(self):
        self.addr_lst=DLinkedList()
        self.current=0  #현재 사이트의 인덱스
        self.hist=DLinkedList()    #hist리스트는 여태 방문한 사이트를 모두 관리(여러번 방문한 것들 중 가장 최근에 방문한 순서를 알기 위함)
        self.addr_lst.insert("www.hufs.ac.kr",0)
        self.hist.insert("www.hufs.ac.kr",0)
        print(self.addr_lst.getEntry(0))

    def go(self,addr):
        self.hist.insert(addr,(self.hist.size()))  #먼저 go를 하면 addr을 hist에 추가
        self.addr_lst.insert(addr,self.current+1)  #self.current에 1을 더하는 이유: insert를 사용하면 self.current의 전에 삽입이 되기 때문이다.
        loc=self.current+2
        while loc<self.addr_lst.size():
            self.addr_lst.remove(loc)
        self.current=self.addr_lst.size()-1   #go를 하면 current 변수는 addr_lst의 가장 마지막 원소의 인덱스가 되어야함. 
        print(self.addr_lst.getEntry(self.current))  #현재 있는 사이트를 출력
        return
    def forward(self):
        if self.current==(self.addr_lst.size()-1):return  #만약 현재 사이트의 인덱스=addr_lst의 갯수-1 이면 더이상 앞으로 이동할 페이지가 없으므로 아무것도 하지 않는다.
        else:   # 그렇지 않은경우
            self.current+=1 #current 변수에 1을 더한뒤,
            print(self.addr_lst.getEntry(self.current))  # 앞으로 이동한 사이트를 출력
            return
    def backward(self):
        if self.current==0:return   #현재 사이트의 인덱스=0이면 전으로 이동할 페이지가 없으므로 아무것도 하지 않는다.
        else:
            self.current-=1 #current변수에 1을 뺀뒤,
            print(self.addr_lst.getEntry(self.current))  #뒤로 이동한 사이트를 출력. self.addr_lst.getNode(self.current).back.addr을 쓰지 않는이유: 이렇게하면 값만 출력되고 현재 위치한 사이트의 인덱스(self.current)는 변화하지 않기 때문.출력후 self.current에 +1을 해주면 해결된다.
            return
    def history(self):
        loc=self.hist.size()-1  #끝에서 부터 시작한다.
        temp=[]
        node=self.hist.getNode(loc) #맨 뒤에 위치한 노드를 찾아낸다.
        while node!=None:   #back의 링크를 따라 Node가 none일 때 까지 뒤로 이동하면서 중복을 확인한 후 출력.
            if node.addr in temp:
                node=node.back
                continue
            else:
                print(node.addr)
                temp.append(node.addr)
                node=node.back
    def quit(self):return False


addrlst=addrList()
breakP=True
while breakP:
    cmd=input().split()
    if cmd[0]=="go":addrlst.go(cmd[1])
    elif cmd[0]=="forward":addrlst.forward()
    elif cmd[0]=="backward":addrlst.backward()
    elif cmd[0]=="history":addrlst.history()
    elif cmd[0]=="quit":breakP=addrlst.quit()
    elif cmd[0]=="printList":addrlst.addr_lst.printList()