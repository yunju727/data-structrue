class Queue:
    MAX_QSIZE = 10  # resize의 성능을 보려고 10으로 설정하였다.

    def __init__(self):
        self.items = [None]*self.MAX_QSIZE
        self.front = 0
        self.rear = 0
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, e):  # 삽입(enqueue)연산
        if self.size == len(self.items):  # 큐가 꽉 차면
            # 2배의 사이즈로 resize(resize함수는 매개변수로 받은 값만큼 사이즈를 조정한다.)
            self.resize(2*len(self.items))
            self.items[self.rear] = e  # resize 후 끝에 원소 추가
            # rear에 해당하는 자리에 원소가 찼으므로 rear을 +1해준다.
            self.rear = (self.rear+1) % (len(self.items))
            self.size += 1  # 원소가 추가되었으므로, size를 +1한다.
        else:  # 큐에 자리가 남아있으면
            self.items[self.rear] = e   # rear에 원소를 추가
            # rear 인덱스에 원소가 찼으므로, rear을 +1해준다.
            self.rear = (self.rear+1) % (len(self.items))
            self.size += 1

    def dequeue(self):  # 삭제연산(dequeue)
        if self.isEmpty():  # 비어있으면 삭제 할 것이 없으므로 False를 반환
            return False
        else:  # 비어있지 않으면
            e = self.items[self.front]  # 맨 앞의 원소를 변수에 담는다.
            # 원형 큐이므로, front에 1을 더한 뒤, 길이로 나눈 나머지를 front가 된다.
            self.front = (self.front+1) % (len(self.items))
            self.size -= 1  # 삭제연산이므로 size가 1개 줄어든다.
            return e  # 삭제된 원소의 값을 반환한다.

    def resize(self, cap):  # 사이즈 재설정(resize)
        olditems = self.items  # 현재 큐에 담겨있는것들을 리스트변수에 담는다.
        self.items = [None]*cap  # 빈 큐의 크기를 늘린다
        walk = self.front   # 가장 처음 인덱스
        for k in range(self.size):  # for문을 통해서 olditems에 있던 것을 넣어준다.
            self.items[k] = olditems[walk]
            walk = (walk+1) % len(olditems)
        self.front = 0  # 새로운 큐에 넣어줬으므로 front를 0으로 초기화 한다.
        self.rear = self.size  # rear은 맨 마지막 원소 다음의 빈 칸의 인덱스이므로 self.size가 된다.

    def __len__(self):  # 사이즈를 반환해준다.
        return self.size


DP = []  # 차례대로 심사가 끝나는 시간을 넣는다.
line = Queue()  # 줄은 큐로 받는다.
n = int(input())
for i in range(n):  # enqueue를 통해서 각 사람들의 [앞사람 기준을 기준으로 한 도착시간, 심사시간]을 넣어준다.
    line.enqueue(list(map(int, input().split())))
arrivetime = 0  # 도착시간(for문을 돌면서 각 사람들의 도착시간을 더해서 각 사람들이 정확히 몇분에 도착했는지 체크한다.)
totalwaiting = 0  # 각 사람들의 기다린 시간의 총 합
for i in range(n):  # 심사 시작
    if i == 0:  # 만약 첫번째로 온 사람이면 기다리는 시간이 없고, 끝나는 시간이 심사시간과 같다.
        person = line.dequeue()  # 줄에서 가장 먼저 빠져나와 상담을 한다.
        DP.append(person[1])    # 심사시간=끝나는 시간이므로, DP리스트에 상담시간만을 추가해준다.
        arrivetime += person[0]  # 다음 사람의 도착시간을 구해야 하므로, 첫번째로 온 사람의 도착시간을 더해준다.
    else:  # 첫번째 사람이 아니면
        person = line.dequeue()
        # 도착시간을 더해서 저장한다. 이렇게 되면 정확히 몇분에 각 사람들이 도착했는지 알 수 있다.
        arrivetime += person[0]
        # 심사 시작시간은 도착시간과 앞에 심사를 받은사람이 끝나는 시간 중 더 늦은(큰) 시간에 시작하게 된다.
        starttime = max(arrivetime, DP[i-1])
        # DP에 줄에서 빠져나와 상담을 들어가는 사람의 심사가 끝나는 시간을 append한다.
        DP.append(starttime+person[1])
        waiting = starttime-arrivetime  # 기다리는 시간 = 심사시작시간-도착시간
        if waiting < 0:  # 그런데 이때 도착시간이 심사시작시간보다 많이 늦은 경우 음수값을 갖게되는데 이 경우, 기다리는 시간이 없으므로 0으로 본다.
            waiting = 0
        totalwaiting += waiting  # totalwaiting변수에 기다린시간을 더해준다.


def answer(x, n):  # 반올림함수
    gop = 1
    for i in range(n):
        gop *= 10
    x = int(x*gop+0.5)/gop
    return x


print("%.2f" % answer(totalwaiting/n, 2))  # totalwaiting에 n을 나누어서 반올림한 후 출력한다.
