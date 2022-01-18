case=[]

while True:
    x=list(map(int,input().split()))
    if x==[0,0,0]:
        break
    case.append(x)

for i in case:
    result=0
    result+=(i[2]//i[1])*i[0]
    if i[2]%i[1]>=i[0]:
        result+=(i[0])
    else:
        result+=(i[2]%i[1])
    print("Case %d: %d"%(case.index(i)+1,result))