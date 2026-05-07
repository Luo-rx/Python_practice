total = 0
for i in range(1,101,2) :
    total += i
else :
    print(f"1-100所有奇数和为{total}")

# total = sum(range(1, 100, 2))
# print(total)

total_two = 0
for ii in range(100,501) :
    if ii % 3 == 0 :
        total_two += ii
else :
    print(total_two)