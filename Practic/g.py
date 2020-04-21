import f

f.print_multy()
print("hello_python\nhello_python\nhello_python")


def sum_up(sum1, sum2):
    """对两个数字求和"""
    print("%d+%d=%d" % (sum1, sum2, sum1 + sum2))
    return sum1 + sum2  # return后面不能在写代码了


c = sum_up(30, 25)
print(c)


def sum_up2():
    """对两个数字求和"""
    a = int(input("加数1"))
    b = int(input("加数2"))
    print("%d+%d=%d" % (a, b, a + b))
    sum_up(1, 1)  # 函数内调用函数


sum_up2()
