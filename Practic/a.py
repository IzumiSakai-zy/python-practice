import keyword
print(keyword.kwlist)
age = int(input("age"))
if age >= 18:
    print("允许进入网吧")
else:
    print("滚回家去")
print("比较运算符== !=(不等于) > < >=")
import math

print(math.pi)
print(3 != 2)  # 不等号的运用
"""a=1818
   len(a)
   数字型没有长度概念"""
a = math.cos(math.pi / 3)
print("%.2f" % a)
