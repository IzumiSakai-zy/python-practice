def print_line(str, rows, lines):
    """
    :param str: 需要打印的字符
    :param times: 打印的次数
    :param lines:打印的行数
    """
    i = 1
    while i <= lines:
        print(str * (rows - i+1))
        i += 1
# append,insert,extend,pop,remove,count,sort
print_line("%", 5, 5)  # 模块名也是一个标志符
print("="*50)
quanshui = ["坂井泉水", "姐姐", 3, [3, 2, "HAH"]]
print(quanshui[2])  # 列表取值
print("="*50)
print(quanshui.index("姐姐"))  # 取索引
quanshui[2] = "最美的泉水姐姐"  # 修改
quanshui.append("izumi sakai")  # 增加
quanshui.insert(3, "hold me")  # 插入(有指定位置的增加)。"hold me"成为列表的索引3
print(quanshui)
print("="*50)
songs = ["Don't you see", "Goodbye my loneness"]
quanshui.extend(songs)  # 追加，拓展。按照顺序增在末尾，quanshui变大
print(quanshui)
print(songs)
print("$"*50)
quanshui.remove("hold me")  # 删除
quanshui.pop(0)  # 默认删除最后一个
del quanshui[2]  # del 命令将变量从内存中删除
print(len(quanshui))  # 查看数据多少
print(quanshui.count("姐姐"))  # 查看某个数据出现的次数
# quanshui.clear()
quanshui.sort()  # quanshui.sort(reverse=True)分别为正序排序和反序排序
print(quanshui)
