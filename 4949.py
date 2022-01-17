strlst=[]

while True:
    string=input()
    if string=='.':
        break
    strlst.append(string)

'''
case=0: pop에서 indexerror났을 때, 괄호 중 )나 ]로 시작한 경우
case=2: (]거나 [)인 경우
case=1: 아무 문제x for문 돌아갔을때
'''
for i in strlst:
    blank=[]
    case=1
    for j in i:
        if j=="(":
            blank.append(0)
        elif j==")":
            try:
                check=blank.pop()
                if check!=0:
                    case=2
                    break
            except IndexError:
                case=0
                break
        elif j=="[":
            blank.append(1)
        elif j=="]":
            try:
                check=blank.pop()
                if check!=1:
                    case=2
                    break
            except IndexError:
                case=0
                break
    if case==1 and blank==[]:
        print("yes")
    else:
        print("no")