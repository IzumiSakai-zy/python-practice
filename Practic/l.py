"""python中的引用"""
a = 1
print(id(1))
print(id(a))
b = a
print(id(a))
print(id(b))
a = 2
print(id(2))
print(id(a))
print(id(b))
# 字符串变量也是一模一样的
c = True
print(id(c))
d = True
print(id(d))  # True,False保存地址是固定的
"""可变与不可变类型:
   可变就是在不改变内存地址的前提下修改其中的内容，只有列表和字典可变
   不可变就是修改内容必须新建内存重新修改，占用更多内存。数字，字符串，波尔，元祖不可变"""
dic = {"name": "banjingquanshui", 1: "数字", (1, 2, 3): "元祖"}
# 列表，字典不能作为键（KEY），字符串，数字，元祖可以
hash(("数字", "字符串", "元祖", "不能是列表字典"))
# 哈希函数输入内容返回一个特征码。字典中的Key实际要首先哈希一下方便增删改
# 局部变量：定义在函数内部的变量，不同函数可以使用相同的局部变量；
# 全局变量：定义在函数外部都可以访问的变量
# 函数内部不允许修改全局变量 。可以在全局和函数内定义同一个变量，但它们没有任何关系
name = "banjingquanshui"


def demo():
    global name
    name = "坂井泉水"
    age = 40
    return name, age  # 虽然没有括号，本质上返回是一个数组


name, age = demo()  # 居然还能这样定义
print(demo()[1])  # glable关键字修改全局变量,引用元祖数据
# 函数无法使用调用语句下面的全局变量
# 全局变量命名以gl_开头
s = 2
t = 4
s, t = t, s
print("s=%d,t=%d" % (s, t))  # python独有数据交换
def demo(list1):
    list1.append("quanshuijieje")
    print(list1)
    print("函数结束")
gl_list1 = [1, 2, 3]
demo(gl_list1)
print(gl_list1)
# 列表字典在函数中调用了方法比如list.append(pop)会影响到变量引用的内存地址中的值
# 导致所有引用该内存的变量全部发生变化
# list+=list（列表）实际上是调用了extend方法，修改内存地址的值。+=不会做相加在赋值的操作。但数字和字符串是相加在赋值的操作
def gender_judge(name, class1 = 18, gender= True):
    default = "男生"
    if not gender:
        default = "女生"
    print("%s是%d班的，是一个%s" % (name, class1, default))
gender_judge("小明", class1=5) #  或者直接输入5，但是缺省默认变量赋值指定下更好
#  缺省变量使用方法。此参数一般放在末尾
def multy_args(num, *args, **kwargs):
    print(num)
    print(args)
    print(kwargs)
multy_args(1,23,4,name="quanshuijiejie") #  多值参数使用
#  multy_args(*list,**dic)拆包语法，不然list个dic会被认为是第一个列表变量的两个元素
def digui(addition):
    print(addition)
    if addition>=100:
        return
    digui(addition+1)
digui(90) #  递归即自己调用自己，必须加判断否则死循环
s = 0
def sum_up(goal):
    global s
    s += goal
    if goal == 1:
        print(s)
        return #  后面接值就返回值，没有接值就中断不返回任何值
    sum_up(goal-1)
sum_up(100) #  递归案例并复习函数内修改全局变量
def sum_up2(sum):
    if sum == 1:
        return 1
    temp = sum_up2(sum-1)
    return sum + temp
print(sum_up2(100)) #  看不懂，逻辑比较困难




