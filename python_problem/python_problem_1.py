num = 0
num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
while(1):
    if not isinstance(num,int):
        print("정수를 입력하세요")
        num = map(int,input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    elif num not in list(range(1,4)):
        print("1,2,3 중 하나를 입력하세요")
        num = map(int,input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    else:
        break
