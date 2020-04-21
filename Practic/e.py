i = 1
while i <= 5:
    print("*" * i)
    i += 1
print("*", end="大少")  # 不加默认是换行符
print("*")
row = 1
clo = 1
while row <= 5:
    while clo <= row:  # 换成(6-row)则可打印倒三角
        print("*", end="")
        clo += 1
    clo = 1
    row += 1
    print()
