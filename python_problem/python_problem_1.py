num = 0

while(1):
    a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    if not isinstance(a,int):
        print("정수를 입력하세요")
        continue
    elif a not in list(range(1,4)):
        print("1,2,3 중 하나를 입력하세요")
        continue
    else:
        num += a
        break

for i in range(1,num+1):
    print("playerA :",i)
num2 = 0 
while(1):
    a = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
    if not isinstance(a,int):
        print("정수를 입력하세요")
        continue
    elif a not in list(range(1,4)):
        print("1,2,3 중 하나를 입력하세요")
        continue
    else:
        num2 += num+a
        break

for i in range(num+1,num2+1):
    print("playerB :",i)