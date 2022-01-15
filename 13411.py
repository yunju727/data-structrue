import math
n=int(input())

robot=[]

for i in range(n):
    x=list(map(int,input().split()))
    x.append(i+1)
    robot.append(x)


for i in robot:
    d=i[0]*i[0]+i[1]*i[1]
    s=math.sqrt(d)/i[2]
    i.append(s)

robot=sorted(robot,key=lambda x: (x[4],x[3]))


for i in robot:
    print(i[3])