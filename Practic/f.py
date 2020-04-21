def print_multy():
    """打印一个乘法口诀表"""  # 给函数写注释
    i = 1
    while i <= 9:
        t = 1
        while t <= i:
            print("%d*%d=%d" % (t, i, i * t), end="\t")
            # 横向制表符。end必须加None or String
            t += 1
        i += 1
        print()
    print("Welcome\npython")  # 换行符
    print("That\'s my son")
    return "郑大少的函数"


print(print_multy())
