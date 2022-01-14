K=int(input())

jamin=[]

for i in range(K):
    x=int(input())
    if x!=0:
        jamin.append(x)
    else:
        if x!=[]:
            jamin.pop()

print(sum(jamin))