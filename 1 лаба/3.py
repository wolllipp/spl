i = [11, 5, 7, 3, -55, 77, 33, 99, -88]
max2 = max([x for x in i if x % 2 == 0] or [i[0]])
print(max2)

arr2 = [x for x in i if x >= 0]
arr3 = [x for x in i if x < 0]
arr = arr2 + arr3

print(arr)


