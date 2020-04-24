#가위 바위 보 게임
# while 구문 이용해 삼세판 구현하기

value = input("안내면 진다 가위, 바위, 보!")
import random
list_a = ["가위","바위", "보"]
com = random.choice(list_a)
print(com)

hit = 0
while hit < 3:
    if value == com:
        print("비겼습니다.")
        break
    elif value=="가위" and com=="바위":
        hit = hit + 1
        print("%d번 졌습니다." %hit)
    elif value=="바위" and com=="보":
        hit = hit + 1
        print("%d번 졌습니다." %hit)
    elif value=="보" and com=="가위":
        hit = hit + 1
        print("%d번 졌습니다." %hit)
    else:
        hit = hit + 1
        print("%d번 이겼습니다." %hit)
    if hit == 3:
       print("게임이 종료되었습니다.")
       break

coffee = 10
money = 300
while money:
    print("커피를 줍니다.")
    coffee = coffee -1
    print("남은 커피양은 %d개 입니다." %coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다.")
        break
