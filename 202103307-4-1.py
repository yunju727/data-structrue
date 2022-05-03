class Node:
    def __init__(self, element):
        self.data = element
        self.link = None


class LinkedStack:  # 연결구조 스택
    def __init__(self):
        self.top = None
        self.size = 0

    def isEmpty(self):
        return self.top == None

    def push(self, e):  # 새로 들어온 것을 top에 쌓는다(맨 위에 올린다.)
        newNode = Node(e)  # e(data값)값을 Node로 저장
        newNode.link = self.top  # 현재 top에 있는 값을 link값으로 갖게 한 뒤
        self.top = newNode  # newNode를 self.top으로 설정한다.
        self.size += 1  # 스택에 노드(원소)가 추가되었으므로 size변수를 +1 한다.

    def pop(self):  # 삭제연산
        if self.size == 0:  # size가 0이면 삭제할 노드가 없으므로 False반환
            return False
        e = self.top.data  # e에 스택의 맨위에 있는 값을 저장한다.
        # self.top을 top 바로 밑에있는 값(self.top.link)으로 설정해준다.
        self.top = self.top.link
        self.size -= 1  # 원소가 삭제되었으므로 size변수를 -1한다.
        return e    # 삭제된 데이터값을 반환한다.

    def __len__(self):  # len함수를 쓰면 size를 반환하도록 구현했다.
        return self.size


operand = LinkedStack()  # 피연산자 스택
postfix = input().split()
operator = '+-*//%'  # 연산자
case = 1    # postfix계산을 끝까지 잘 마쳤는지 확인하기 위한 변수이다. ;를 만나면 case변수를 0으로 만든다.
for i in postfix:
    if i == ';':
        case = 0
        break
    elif i in operator:  # 연산자(operator)를 만난 경우, 피연산자 스택에 맨 위의 두 값을 빼낸다.
        if len(operand) >= 2:  # 그런데 두개의 값을 빼내려면 피연산자 스택의 원소가 2개 이상이어야한다.
            back = int(operand.pop())
            front = int(operand.pop())
        else:  # 피연산자 스택의 원소가 2개 미만인 경우 연산을 그만둔다.
            break
        if i == '+':    # 해당하는 연산자에 맞는 계산을 해준다.
            operand.push(front+back)
        elif i == '-':
            operand.push(front-back)
        elif i == '*':
            operand.push(front*back)
        elif i == '//':
            operand.push(front//back)
        elif i == '%':
            operand.push(front % back)
    else:  # 피연산자를 만난경우, 피연산자 스택에 push해준다.
        operand.push(i)

# 연산을 마친 뒤
if operand.size == 1:  # 만약 피연산자 스택의 사이즈가 1이면
    if case == 1:  # 피연산자 스택의 사이즈값이 1이더라도, 끝까지 postfix연산을 마치지 않은경우, error출력
        print('error')
    else:  # 끝까지 postfix연산을 마친 경우 스택에 남아있는값(1개) 출력
        print(operand.pop())
else:  # 피연산자 스택의 사이즈가 1이 아닌경우 error출력
    print('error')
