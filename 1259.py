'''
def ispalindrome(x):
	y=list(x)
	y.reverse() #y는 아예 뒤집은 것
	if ''.join(y)==x:   #뒤집힌게 원본과 같으면 회문
		print("yes")
	else:
		print("no")
'''
#재귀함수 이용
def isPalindrome(x,i=0):    #x는 리스트, i는 인덱스번호(매개변수로 주어지지 않았을 때는 0으로 초기화)
    if i>=len(x):   #만약에 i가 x의 길이보다 크거나 같으면 인덱스 에러가 나므로 그만두고, True 반환
        return True
    elif x[i]==x[-1]:   #아닌경우 i번째 요소와 마지막 요소를 비교하고, 같으면 맨마지막 요소 삭제
        x.pop()
        i+=1    #인덱스번호는 1더해준다
        return isPalindrome(x,i)
    else:   #아닌경우 False반환
        return False


while True:
    user=list(input())
    if user==['0']:break
    if isPalindrome(user):
        print("yes")
    else:
        print("no")