number = [1, 2, 3, 4, 5, 6, 7, 8]
s = 0
for i in number:
    s = s + i
    print(s)
first_tuple = ("坂井泉水", "izumi sakai", "泉水姐姐", "最美女摇滚")
print(first_tuple.index("泉水姐姐"))
print(first_tuple[2])
# tuple=(5)是一个整数，tuple=(5,)是一个元祖
xiaoMing = ("小明", 1.75, 56)
print("%s的身高是%.2f,体重是%dkg" % xiaoMing)
str = "%s的身高是%.2f,体重是%dkg" % xiaoMing  # 本身就是一个字符串
print(str)
number_tuple = tuple(number)  # 列表和元祖互相转化，列表=list
print(type(number_tuple))

banjingquanshui = {"name": "坂井泉水",
                   "Jpanese name": "izumi skakai"
                   }  # 字典数据是无序的
print(banjingquanshui)
print("+"*50)
print(banjingquanshui["name"])  # 取值
print("+"*50)
banjingquanshui["songs"] = "So together"  # 增加，修改。存在就修改，不存在就新增
banjingquanshui.pop("songs")  # 删除
print(banjingquanshui)
print(len(banjingquanshui))  # 查看键值对数量
banjingquanshui1 = banjingquanshui.update(banjingquanshui)  # 合并字典，相同键值对值会覆盖
# banjingquanshui.clear()#清空字典
for i in banjingquanshui:  # i是键值对中的键，也就是key
    print("%s-%s" % (i, banjingquanshui[i]))  # 迭代遍历字典
# list列表可以内嵌字典
# 字符串可以类比成列表
zifuchuan = "banjingquanshui"
for k in zifuchuan:
    print(k)
name = "banjingquanshui1"
print(name.isalnum())
print(name.isalpha())
