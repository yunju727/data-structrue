n=int(input())
n_list=[]   #주어진 수
arr=[]   #주어진 수열
stack=[]   #push연산시 stack에 저장
answer_arr=[]
answer_oper=[]

for i in range(n,0,-1):
    x=int(input())
    arr.append(x)
    n_list.append(i)  #오름차순으로 stack에 넣으려고

for i in range(len(arr)):
    if n_list!=[]:  #숫자리스트가 안비어있으면
        if n_list[-1]<=arr[i]:  #비교하는 수열값보다 작아질때까지 stack 리스트에 넣는다.
            while n_list!=[] and n_list[-1]<=arr[i]:    #빈 리스트가 아니고 값보다 작거나 같을때까지 반복해서 stack에 넣는다.
                '''
                while문 조건에 n_list!=[]를 추가한 이유
                n_list의 값이 모두 stack으로 추가된 경우에는
                n_list는 빈리스트가 되는데 이때 while문에서 n_list[-1]로 인덱싱하면 인덱스 범위 오류가 뜸
                '''
                stack.append(n_list.pop())
                answer_oper.append('+')
            answer_arr.append(stack.pop())
            answer_oper.append('-')
        elif stack!=[] and stack[-1]==arr[i]:   #n리스트에서 값을 찾을 수 없는 경우에는 stack에서 값비교
            answer_arr.append(stack.pop())
            answer_oper.append('-')
        else:
            break
    elif stack!=[]: #n리스트가 비었고 stack이 안비어있으면
        if stack[-1]==arr[i]:   #같을 시에 추가
            answer_arr.append(stack.pop())
            answer_oper.append('-')
        else:   #다르면 그냥 그만둠. n리스트가 비었는데 스택의 마지막 요소가 다르면 만들수 없는 수열임.
            break

if len(answer_arr)==n:
    for i in answer_oper:
        print(i)
else:
    print("NO")