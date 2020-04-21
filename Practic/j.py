my_favorite_singer = "banjingquanshui"
my_favorite_singer.isspace()  # 判断是否全是空格，\t,\n
print(my_favorite_singer.isdigit())
print(my_favorite_singer.isdecimal())
print(my_favorite_singer.isnumeric())
# 这三个方法都不能判断小数
print(my_favorite_singer.startswith("ban"))  # 判断是否以指定的字符串开始
print(my_favorite_singer.endswith("shui"))  # 判断是否义指定的字符串结束
print(my_favorite_singer.find("ji"))  # 查找指定字符串,和index方法差不多
print(my_favorite_singer.replace("shui", "shuisister"))  # 替换,字符串本身没有改变
print(my_favorite_singer)
list = ["登鹳雀楼", "王之涣", "白日依山尽", "黄河入海流", "欲穷千里目", "更上一层楼"]
for poem in list:
    print("|%s|" % poem.center(10))  # center对齐
for poem in list:
    print("|%s|" % poem.ljust(10))  # 左对齐，右对齐换成r
del list[0]  # 或者del (list[0])
print(max(list))  # 最大值
print(1 >= 1)
print(len(list))
