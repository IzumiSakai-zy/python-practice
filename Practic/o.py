def with_draw():
    amount = int(input("请输入你要提现的金额"))
    if amount%100 == 0:
        return  amount
    error = Exception("请输入整百数", "thank you")
    raise error
try:
    print(with_draw())
except Exception as result:
    print(result)
# 主动抛出错误并且try。首先创建exception实例，在raise出实例，在try


import c as AnotherName  # 可以给导入的工具包起一个别名。仅用于本文件，本质没有变
AnotherName.judge(1,1)
from f import print_multy  # 部分导入,就相当于本来就写在这个文件里面一样
print_multy()
#  导入相同的方法名时，后者会把前者重写。或者不想重写可以通过取别名区分
from a import *  # 也是全部导入，且使用时不需要写导入模块名。
                # 相当于本就写在这个文档，但是不推荐，容易相同方法重写
# python模块搜索顺序，现在当前目录在在python目录。故当前目录下创建了random文件import random会失效
print(__name__)  # __name__模块在本文件下值永远是字符串__main__,
                 # 但被导入其他文件在其他文件执行时就是__模块名。
                 # 可用于判断在模块中不执行源文件的测试代码
if __name__ =="__main__":
    print("测试代码")
# python的包。由多个python模块和一个名为__init__的文件组成
import pri

