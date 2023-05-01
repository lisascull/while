n = int(input('enter number N'))
i = 0
while i <= n:
    if i % 3 == 0:
        print(i)
    i += 1

n = int(input('enter number N'))
sum = 0
i = 0
while i <= n:
    if i % 3 == 0:
        sum += i
    i += 1
print('Сума чисел, які діляться на 3: ', sum)