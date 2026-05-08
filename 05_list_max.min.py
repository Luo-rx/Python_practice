list_one = []
total = 0
# 获取用户输入并判断是否为整数
while True :
    try :
        user_input_quantity = int(input("您要对几组数字进行计算？(请输入正整数)"))
        if user_input_quantity <= 0 :
            print("请输入正整数")
        else:
            break
    except ValueError :
        print("输入错误，请重新输入，要求为正整数")

# 根据用户提供的user_input_quantity对列表添加元素
while total < user_input_quantity :
    while True :
        try :
            user_input = int(input(f'请输入数字，我将收集{user_input_quantity}次，目前为{total}次'))
            break
        except ValueError :
            print("输入无效，请重新输入")
    list_one.append(user_input)
    total += 1

print(f"{user_input_quantity}个数字已获取成功")

list_one_max = max(list_one)
list_one_min = min(list_one)
list_one_sum = sum(list_one)
list_one_length = len(list_one)

#列表内索引为奇偶数的元素奇偶数和
list_odd_sum = sum(list_one[0::2])
list_even_sum = sum(list_one[1::2])


#列表内元素为奇偶数的奇偶数和
list_element_odd = 0
list_element_even = 0

#if第一个判断为奇数加，else为偶数加
for element_odd in list_one :
    if element_odd % 2 != 0 :
        list_element_odd += element_odd
    else:
        list_element_even += element_odd

average = list_one_sum / list_one_length

while True :
    user_choice = input("接下来你希望我计算什么？请输入:最大值（max）、最小值（min）、平均值（average）、求和（sum）、退出程序（q）").strip()
    match user_choice :
        case "最大值" | "max" :
            print(f"这{user_input_quantity}个数字的最大值为{list_one_max}")
        case "最小值" | "min" :
            print(f"这{user_input_quantity}个数字的最小值为{list_one_min}")
        case "平均值" | "average" :
            print(f"这{user_input_quantity}个数字的平均值为{average:.2f}")
        case "求和" | "sum" :
            user_sum_choice = input("求总和(sum)、求位于奇/偶数位的数字总和(list_odd_sum/list_even_sum)、求所输入数字的奇/偶数总和(list_element_odd/list_element_even)")
            if user_sum_choice in ("求位于奇数位的数字总和" , "list_odd_sum") :
               print(f"求位于奇数位的数字总和为{list_odd_sum}")
            elif user_sum_choice in ("求位于偶数位的数字总和" , "list_even_sum") :
                print(f"求位于偶数位的数字总和为{list_even_sum}")
            elif user_sum_choice in ("求所输入数字的奇数总和" , "list_element_odd") :
                print(f"求所输入数字的奇数总和为{list_element_odd}")
            elif user_sum_choice in ("求所输入数字的偶数总和" , "list_element_even") :
                print(f"求所输入数字的偶数总和为{list_element_even}")  
            elif user_sum_choice in ("求总和" , "sum") :
                print(f"总和为{list_one_sum}")
            else:
                print("输入错误，请重新输入")
        case "退出程序" | "退出" | "q" :
            print("程序已退出")
            break
        case _:
            print("无效指令，请重新输入")
