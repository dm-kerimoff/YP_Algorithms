def binary(num1, num2):
    # реверс
    num1 = num1[::-1]
    num2 = num2[::-1]

    # добавим недостающие нули
    len_max = max(len(num1), len(num2))
    num1 += '0' * (len_max - len(num1))
    num2 += '0' * (len_max - len(num2))

    flag = 0 #счётчик переполнения
    res = []

    for i in range(len(num1)):
        value = int(num1[i]) + int(num2[i]) + flag
        flag = value // 2
        res.append(value % 2)

    if flag == 1:
        res.append(1)
    res = res[::-1]
    return res

num1 = input()
num2 = input()
print(''.join(map(str, binary(num1, num2))))
