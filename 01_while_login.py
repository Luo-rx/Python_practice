user_one_name = "admin"
user_one_passwd = "666888"
user_two_name = "zhangsan"
user_two_passwd = "123456"
user_three_name = "taoge"
user_three_passwd = "888666"


# 登录状态为0，登录后为1
login_status = 0
while login_status != 1 :

    user_name_input = input("请输入用户名").strip()
    user_passwd_input = input("请输入密码").strip()

    if user_name_input == user_one_name and user_passwd_input == user_one_passwd :
        print(f"{user_one_name}，登陆成功")
        login_status = 1
    elif user_name_input == user_two_name and user_passwd_input == user_two_passwd :
        print(f"{user_two_name}，登陆成功")
        login_status = 1
    elif user_name_input == user_three_name and user_passwd_input == user_three_passwd :
        print(f"{user_three_name}，登陆成功")
        login_status = 1
    else :
       print("账号或密码错误,请重新输入")
