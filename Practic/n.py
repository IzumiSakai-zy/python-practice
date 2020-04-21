
class A(object):  # 继承了object的是新式类
    def dayin(self):
        print("a dayin")

    def buyin(self):
        print("a buyin")


class B:  # 没有继承object的是经典类
    def dayin(self):
        print("b dayin")

    def buyin(self):
        print("b buyin")


class C(A, B):
    pass


demo = C()
demo.buyin()
print(C.__mro__)  # method resolution order  类名.__mro__调用查看
print(dir(A))  # dir查看内置方法
print(dir(B))  # 经典类的方法少太多  但现在3.0解释器都是新式类


class Dog:
    def __init__(self, name):
        self.name = name

    def game(self):
        print("%s普通的玩耍" % self.name)


class XiaoTianQuan(Dog):
    def game(self):
        print("%s在天上玩耍" % self.name)


class Person:
    def __init__(self, name):
        self.name = name

    def game(self, playwith):
        playwith.game()  # 人类类中调用狗的方法。注意game后面的括号
        print("%s和%s一起玩耍" % (self.name, playwith.name))


dabai = Dog("dabai")
xiaotianquan = XiaoTianQuan("xiaotianquan")
xiaoming = Person("xiaoming")
xiaoming.game(xiaotianquan)


# python中一切皆是对象。类是类对象，类创建的对象是实例对象。每个创建的对象又叫
# 一个实例，创建的过程叫实例化。每个实例的属性有各自的内存地址，但是方法只有一个。全要引用类方法
class Tools(object):  # 类也有属性和方法
    count = 0  # 使用赋值语句定义类属性

    def __init__(self, name):
        self.name = name
        Tools.count += 1  # 记录创建了多少个类对象

    @classmethod  # 定义类方法
    def show_count(cls):  # 第一个参数必须是cls,相当于实例方法的self。调用时不用传递
        print(cls.count)

    @staticmethod  # 静态方法，即啥都属性都不需要的方法
    def static():
        print("这是一个静态方法")


# python属性查找机制——一级一级向上查找，使用实例任然可以调用类的属性。
# 实例任然可以调用类方法
# 如果通过实例调用类的属性并赋值，则相当于给实例新建了一个属性并赋值，
# 并不会影响到类的属性值。也根本不会向上搜索，相当于直接给实例创建实例属性并赋值
Tools.static()  # 直接类名调用静态方法


class Game(object):
    top_score = 0

    @staticmethod
    def show_help_information():
        print("这是帮助信息")

    @classmethod
    def show_top_score(cls):
        print(cls.top_score)

    def __init__(self, game_player):
        self.gamer = game_player


# __new__方法。1：在内存中创建一个新对象。2：返回对象的引用。3：把引用传给初始化方法进行初始化
class MusicPlayer(object):
    instance = None

    def __new__(cls, *args, **kwargs):
        print("调用new方法")
        if cls.instance is None:
            cls.instance = super().__new__(cls)  # super是一个特殊object实例，必须打括号。必须要传入cls
        return cls.instance

    def __init__(self):
        print("初始化")


player1 = MusicPlayer()
player2 = MusicPlayer()  # 每次创建对象就要执行一次初始化方法，如果想只执行一次可以类似添加判断
print(player1)
print(player2)  # 两个内存地址完全相同，单例创建完成
while True:
    try:
        num = int(input("请输入一个整数"))
        result = 3/num/(num-1)
        print(result)
        break
    except ZeroDivisionError:
        print("分母不能为零")
    except ValueError:
        print("请输入正确的整数")  # 捕获异常机制,try and except
    except Exception as result:
        print("未知错误 %s" % result)  # 捕获额外没有预料到的错误
try:  # try except的完整结构
    num = int(input("请输入一个整数"))
except ZeroDivisionError:
    print("分母不能为零")
except ValueError:
    print("请输入正确的整数")
except Exception as result:
    print("未知错误 %s" % result)
else:
    print("如果没有错，会执行的代码")
finally:
    print("无论是否有错，都会执行的代码")
# 异常传递机制：一级传一级，最后传到最外层主程序。所以只用主程序try就行了，不用内部每个都try

