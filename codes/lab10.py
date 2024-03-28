list = [1, 3, 5, 14, 22, 48]
flag = False
for i in list:
    if i % 2 != 0:
        flag = True
        break

if flag is True:
    print('В массиве есть нечетное число')
else:
    print('В массиве все числа четые')