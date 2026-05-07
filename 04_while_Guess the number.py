import random

random_num = str(random.randint(1,100))

guess = 0

while guess != 1 :
    user_num = input("请输入数字").strip()
    if user_num == random_num :
        print("恭喜猜对")
        guess = 1
    elif user_num > random_num :
        print("很可惜猜大了,再来一遍！")
    elif user_num < random_num :
        print("很可惜猜小了，再来一遍！")
    else :
        print("请输入数字")