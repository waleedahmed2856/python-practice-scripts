num = 5
list1 = [0, 1]

for i in range(num - 2):
    number = list1[-1] + list1[-2]
    list1.append(number)

print(list1)
