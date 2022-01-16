paper=list(map(int,input().split()))

n=int(input())
garo=[]
sero=[]
for i in range(n):
    command=list(map(int,input().split()))
    if command[0]==0:   #0이면 가로 자르기
        garo.append(command[1])
    elif command[0]==1:
        sero.append(command[1])

garo.sort(reverse=True)
sero.sort(reverse=True)

garo_len=[]
sero_len=[]
if garo==[]:
    garo_len.append(paper[1])
else:
    for i in range(len(garo)+1):
        if i==0:
            garo_len.append(paper[1]-garo[i])
        elif i==len(garo):
            garo_len.append(garo[-1])
        else:
            garo_len.append(garo[i-1]-garo[i])
if sero==[]:
    sero_len.append(paper[0])
else:
    for i in range(len(sero)+1):
        if i==0:
            sero_len.append(paper[0]-sero[i])
        elif i==len(sero):
            sero_len.append(sero[-1])
        else:
            sero_len.append(sero[i-1]-sero[i])

garo_len.sort(reverse=True)
sero_len.sort(reverse=True)

print(garo_len[0]*sero_len[0])