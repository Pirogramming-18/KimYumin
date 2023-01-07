#함수 이름은 변경 가능합니다.
name_list = []
score1_list = []
score2_list = []
grade_list = []

##############  menu 1
def Menu1(name,score1,score2) :
    name_list.append(name)
    score1_list.append(score1)
    score2_list.append(score2)
    #사전에 학생 정보 저장하는 코딩 

##############  menu 2
def Menu2() :
    for i in range(len(name_list)):
        grade = (score1_list[i]+score2_list[i])/2
        if grade >= 90:
            grade_list.append('A')
        elif 90 > grade >= 80:
            grade_list.append('B')
        elif 80 >  grade >= 70:
            grade_list.append('C')
        else:
            grade_list.append('D')
    
    #학점 부여 하는 코딩

##############  menu 3
def Menu3() :
    print("name mid final grade")
    for i in range(len(name_list)):
        print(f"{name_list[i]} {score1_list[i]} {score2_list[i]} {grade_list[i]}")
   
##############  menu 4
def Menu4(name):
    a = name_list.index(name)
    del name_list[a],score1_list[a],score2_list[a]
    #학생 정보 삭제하는 코딩

#학생 정보를 저장할 변수 초기화
print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            name,score1,score2=input().split()
            score1 = int(score1)
            score2 = int(score2)
            if name in name_list:
                raise Exception
            
        except:
            print("error")
        
        else:
            Menu1(name,score1,score2)
            
        
            
        #학생 정보 입력받기
        #예외사항 처리(데이터 입력 갯수, 이미 존재하는 이름, 입력 점수 값이 양의 정수인지)
        #예외사항이 아닌 입력인 경우 1번 함수 호출 

    elif choice == "2" :
        try:
            if(name_list == None):
                raise Exception
            Menu2()
            
            
        except:
            print("No student data")
            
        else:
            print("Grading to all students")
        
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우 2번 함수 호출
        #"Grading to all students." 출력

    elif choice == "3" :
        try:
            if(len(name_list) == len(grade_list)):
                Menu3()
            else:
                raise Exception
        except:
            print("Error")
        #예외사항 처리(저장된 학생 정보의 유무, 저장되어 있는 학생들의 학점이 모두 부여되어 있는지)
        #예외사항이 아닌 경우 3번 함수 호출

    elif choice == "4" :
        try:
            if(name_list == None):
                raise Exception
            name = input()
            if(name not in name_list):
                print("Not exist name!")
                
            else:
                Menu4(name)
                print(f"{name} student information is deleted.")
            
        
        except:
            print("No Student Data")
        #예외사항 처리(저장된 학생 정보의 유무)
        #예외사항이 아닌 경우, 삭제할 학생 이름 입력 받기
        #입력 받은 학생의 존재 유무 체크 후, 없으면 "Not exist name!" 출력
        #있으면(예를 들어 kim 이라 하면), 4번 함수 호출 후에 "kim student information is deleted." 출력

    elif choice == "5" :
        print("Exit Program!")
        break
        #프로그램 종료 메세지 출력
        #반복문 종료

    else :
        print("Wrong number. Choose again.")
        #"Wrong number. Choose again." 출력