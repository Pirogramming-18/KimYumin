from random import randint

num = 0

def brGame(num):

        check = num
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
                for i in range(check+1,num+1):
                    print("player :",i)

                return num
                
    
    
                
       
if __name__ == "__main__":
  
  
    while(1):
        computer = randint(1,3)
        num += computer
        if(num >= 31):
            print("player win!")
            break
        for i in range(num-computer+1,num+1):
            print("computer",i)

        num = brGame(num)
        if(num >= 31):
            print("computer win")
            break
    
        
        
  