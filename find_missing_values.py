lis = [1,2,3,7,12,15]
list2 = []
for i in range(lis[-1]):
    if i+1 not in lis:
        list2.append(i+1)
print(list2)
