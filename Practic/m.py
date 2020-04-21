#  类名字用大驼峰命名法
print(dir(3))  # 查看python内部可以调用的方法名。变量，函数，数据都是对象
class Cat:
    def __init__(self, wanted):
        print("创建类时解释器会自动调用初始化函数")
        self.wanted = wanted  # 增加属性
    def love(self):
        print("爱%s" % self.wanted)
    def eat(self):
        print("小猫吃鱼")
    def drink(self):
        print("小猫喝水")
    def __del__(self):
        print("对象离开前解释器自动调用方法")
    def __str__(self):
        return "我爱%s" % self.wanted
    # 当不希望打印对象名为内存地址时可创建此方法，此方法只能返回字符串类型

Tom = Cat(wanted="Jeffy")  # 创建对象也是引用内存地址
Tom2 = Tom  # 这两只猫是同一只猫
print(Tom2)  # 打印__str__方法内容
Tom.love()  # 第一个面向对象实例
print("*"*50)  # 因为全局变量del调用在分割线之下


class Person:
    def __init__(self, weight, name="Xiaoming"):
        self.weight = weight
        self.name = name
    def run(self):
        self.weight -= 0.5
    def eat(self):
        self.weight -= 1
    def __str__(self):
        return "%s已经" % self.name+str(self.weight)+"kg了"
Xiaoming = Person(weight=57)
Xiaoming.eat()
Xiaoming.run()
print(Xiaoming)
"""家具案例：房子包含户型、占地面积、家具列表、剩余面积属性。能够增加家具动作。
            家具包含名字、占地面积属性，无动作。
             房子定义类时不用传递剩余面积属性，因为初始剩余面积等于占地面积。
             方法即减少剩余面积(free_area-=item.area)，增加列表(list.append(item.name))"""
class Gun:
    def __init__(self, name, bullet):
        self.name = name
        self.bullet = bullet
        self.free_bullet =bullet
    def change(self):
        self.free_bullet = self.bullet
    def fire(self):
        if self.free_bullet>0:
            self.free_bullet -= 1
        else:
            print("没子弹了")
            self.change()
    def __str__(self):
        return "name:%s-shengyu:%d" %(self.name, self.free_bullet)
class Soldier:
    def __init__(self, name, gun = None):
        self.name = name
        self.gun = gun
    def get_gun(self,name ):
        self.gun = name
    def shoot(self):
        self.gun.fire()
    def zhuangdan(self):
        self.gun.change()
Ak_47 = Gun("Ak_47", 35)
wangmou = Soldier("wangmou")
wangmou.get_gun(Ak_47)
wangmou.shoot()
print(Ak_47)
# is&is not和==区别。 前者判断内存地址是否相同，后者判断变量值是否相同。比如a=[1,2,3]
# b=[1,2] b=b.append(3).  a is b = False a==b = True

class Money:
    def __init__(self):
        self.__amount = 1000  # 定义私有属性或者私有方法，前面加双下划线
        self.kind = "金钱"
    def tell(self):
        print("我有%d￥" % self.__amount)
dollar = Money()
dollar.tell()
#  print(dollar.__amount) 会报错，外部不能访问私有属性
#  但可以强行调用 dollar._Money__amount就能调用，私有全是伪私有
class JingQian(Money):
    def none(self):
        pass
    def rewrite(self):
        print("这是一个方法重写")
        super().tell()  # 还是会依旧调用父类的方法
        print("还可以写其他的代码")
# 继承语法。子类继承父类所有方法和属性（重复代码不用敲）
# 方法的重写，子类的方法和父类的方法有不同，
# 可以直接在子类重新定义相同名的方法，会覆盖父类方法
# 子类依然不能调用和使用父类的私有方法和属性，私有只有自己能用
# 子类不能直接访问父类私有属性和方法，但是可以通过调用父类公用方法间接访问私有属性和方法
class Army(Gun, Soldier):  # 多继承语法
    pass  # 如果多个父类的方法相同，则首先调用先继承的父类
