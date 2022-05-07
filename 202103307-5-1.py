class addrList:
    def __init__(self):
        self.current=0  #현재 사이트의 인덱스
        self.addr_lst=["www.hufs.ac.kr"]    #addr_lst는 현재 이동가능한 주소리스트.
        self.hist=["www.hufs.ac.kr"]    #hist리스트는 여태 방문한 사이트를 모두 관리(여러번 방문한 것들 중 가장 최근에 방문한 순서를 알기 위함)
        print(self.addr_lst[self.current])

    def go(self,addr):
        self.hist.append(addr)  #먼저 go를 하면 addr을 hist에 추가
        temp=self.addr_lst[0:self.current+1]+[addr] #go를 하면 현재사이트 이후의 사이트들은 없어져야 하므로 슬라이싱한것+새로 이동사이트로 리스트를 temp에 저장
        self.addr_lst=temp  #temp를 addr_lst에 저장한다.
        self.current=len(self.addr_lst)-1   #go를 하면 current 변수는 addr_lst의 가장 마지막 원소의 인덱스가 되어야함. 
        print(self.addr_lst[self.current])  #현재 있는 사이트를 출력
        return
    def forward(self):
        if self.current==(len(self.addr_lst)-1):return  #만약 현재 사이트의 인덱스=addr_lst의 갯수-1 이면 더이상 앞으로 이동할 페이지가 없으므로 아무것도 하지 않는다.
        else:   # 그렇지 않은경우
            self.current+=1 #current 변수에 1을 더한뒤,
            print(self.addr_lst[self.current])  # 앞으로 이동한 사이트를 출력
            return
    def backward(self):
        if self.current==0:return   #현재 사이트의 인덱스=0이면 전으로 이동할 페이지가 없으므로 아무것도 하지 않는다.
        else:
            self.current-=1 #current변수에 1을 뺀뒤,
            print(self.addr_lst[self.current])  #뒤로 이동한 사이트를 출력
            return
    def history(self):
        self.hist.reverse() #뒤집는 이유: 가장 최근에 방문한 사이트가 맨 앞에 있으니까
        temp=[] #중복을 없애기 위해 temp리스트를 생성
        for i in self.hist:
            if i in temp:continue   #hist의 원소가 이미 temp에 있으면 그냥 넘어간다.
            else:   #그렇지 않으면 temp에 해당 원소를 추가후 출력한다.
                temp.append(i)
                print(i)
        self.hist.reverse() #다시 뒤집는 이유: 원래대로 되돌려야 하니까, 만약 이렇게 안하면 history를 두번 호출하면 같은 결과가 아닌, 두번째 결과에선 뒤집힌 결과가 나옴.
        return
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