user_input_quantity = 0
list_one = []

while user_input_quantity < 10 :
    while True :
        try:
            user_input_content = int(input(f'请输入数字(将记录十,目前为{user_input_quantity}次)'))
            break
        except ValueError :
            print("输入无效，请重新输入一个整数")
    list_one.append(user_input_content)
    user_input_quantity += 1
print("好的，数据收集完成，接下来我将按照大小进行排序，并且告诉你其最大值和最小值")

list_one.sort()

# list_one_max = list_one[-1]
# list_one_min = list_one[0]

list_one_max = max(list_one)
list_one_min = min(list_one)

list_one_length = len(list_one)
list_one_average = 0

for i in list_one :
    list_one_average += i 
list_one_average = list_one_average / list_one_length

print(f"按照从小到大排序:{list_one}，最大值为{list_one_max}，最小值为{list_one_min}，平均值为{list_one_average}")