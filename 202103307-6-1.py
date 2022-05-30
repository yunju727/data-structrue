class Student:
    def __init__(self,st_no,name):
        self.st_no=st_no
        self.name=name

class Course:
    def __init__(self):
        self.st_list=[] #Student 객체를 원소로 하여, 관리하는 리스트 생성
    def register(self,no,name): #수강 신청 함수
        self.st_list.append(Student(no,name))   #st_list에 학생객체를 원소로 추가한다.
    def cancel(self,no):    #수강 취소
        idx,check=0,False   #idx는 매개변수로 받은 학번의 위치를 나타내는 인덱스를 저장, check는 해당 학생의 유무를 저장
        for i in range(len(self.st_list)):
            if self.st_list[i].st_no==no:   #만약 매개변수로 받은 학번을 가지는 학생이 있으면
                idx,check=i,True    #idx는 해당 학생의 index, check는 True로 저장후 break문으로 반복문 빠져나간다.
                break
        if check:self.st_list.pop(i)
        else:return False
    def info(self,no):  # 매개변수로 입력받은 학번을 가지는 학생의 정보를 출력
        for i in range(len(self.st_list)):  
            if self.st_list[i].st_no==no:
                print(self.st_list[i].st_no,self.st_list[i].name)
                break
            else:pass
    def print_students(self):   #모든 학생들의 정보를 학번순으로 출력
        n=len(self.st_list)
        print(n)
        self.st_list.sort(key=lambda x:x.st_no) #lambda함수를 사용하여 st_list를 학번순으로 정렬한다.
        for i in range(n):print(self.st_list[i].st_no,self.st_list[i].name)
    def quit(self):
        return False


quitCode=True
course=Course()
while quitCode:
    command=input().split()
    if command[0]=="N":course.register(command[1],command[2])
    elif command[0]=="C":course.cancel(command[1])
    elif command[0]=="R":course.info(command[1])
    elif command[0]=="P":course.print_students()
    elif command[0]=="Q":quitCode=course.quit()