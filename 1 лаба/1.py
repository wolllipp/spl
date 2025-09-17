print ("Введите число:")
a = int(input())
print ("Делители числа:")
i = 1
while i <= a:
    if a % i == 0:
        print(i)
    i+=1

