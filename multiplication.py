# 打印10以内的乘法表
i = 1
print('-' * 50)
while i < 11:
    n = 1
    while n <=10:
        print("{:5d}".format(i * n), end = ' ')
        n += 1
    print()     # 目的是跳行
    i += 1
print('_' * 50)

