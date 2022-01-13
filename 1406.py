import sys
input=sys.stdin.readline

leftstr=list(input().strip())

n=int(input())

rightstr=[]

for i in range(n):
    command=list(input().strip())
    if command[0]=='L' and leftstr!=[]:
        rightstr.append(leftstr.pop())
    elif command[0]=='D' and rightstr!=[]:
        leftstr.append(rightstr.pop())
    elif command[0]=='B' and leftstr!=[]:
        leftstr.pop()
    elif command[0]=='P':
        leftstr.append(command[2])
rightstr.reverse()
result_str="".join(leftstr+rightstr)
print(result_str)