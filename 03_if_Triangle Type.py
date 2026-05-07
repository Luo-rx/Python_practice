# telephone = "123456"
# passwd = "xiao_123"

# user_telephone = input("请输入您的电话号码:")
# user_password = input("请输入您的账号密码:")

# if user_telephone == telephone and user_password == passwd :
#     print('登录成功')
# elif user_telephone != telephone and user_password == passwd :
#     print("手机号不正确")
# elif user_password != passwd and telephone == user_telephone :
#     print("密码错误")
# else :
#     print("手机号或密码不正确")



# 根据用户输入数字判断是奇数还是偶数
# user_num = int(input("请输入数字，我来判断他为奇偶数"))

# if user_num % 2 == 0 :
#     print(f"{user_num}为偶数")
# else :
#     print(f"{user_num}为奇数")



# 根据用户输入的年龄判断用户是否成年
# user_age = int(input("请输入您的年龄:"))

# if user_age >= 18 :
#     print("成年")
# else :
#     print("未成年")


# 根据用户输入的数字判断正负数
# user_num = int(input("请输入数字，我来判断正负数"))

# if user_num > 0 :
#     print(f"{user_num}为正数")
# elif user_num < 0 :
#     print(f"{user_num}为负数")
# else :
#     print(f"{user_num}不为正数也不为负数")


# 根据用户输入的分数判断用户是否及格
# user_score = int(input("请输入你的分数:"))
# passing_score = 60

# if user_score >= passing_score :
#     print("你过关")
# else :
#     print("不及格")


#判断三角形类型
A_side = int(input("请输入第一条边的边长"))
B_side = int(input("请输入第二条边的边长"))
C_side = int(input("请输入第三条边的边长"))

# 三角形不等式判断是否构成三角形:  任意两条边相加一定大于第三边
if A_side + B_side > C_side and A_side + C_side > B_side and B_side + C_side > A_side :
    if A_side == B_side != C_side or A_side == C_side != B_side or B_side == C_side != A_side :
        print("这是等腰三角形")
    elif A_side == B_side and A_side == C_side and B_side == C_side :
       print("这是等边三角形")
    elif A_side**2 + B_side**2 == C_side**2 or A_side**2 + C_side**2 == B_side**2 or B_side**2 + C_side**2 == A_side**2 :
       print("这是直角三角形")
    else :
       print("这是普通三角形")
    
else :
  print("这三条边不能构成三角形")