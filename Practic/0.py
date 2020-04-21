price = float(input("苹果的单价："))
weight = float(input("苹果的重量："))
money = price * weight
type(money)
print("苹果%.2f元一斤，总重%.2f斤。应收%.2f￥元" % (price, weight, money))
print("数据是%.0f%%" % (price * 100))  # 出现格式字符串必须两个百分号表示百分号
print("%")  # 单独字符串则直接输出就行
student_number = 45
print("我的学号是%09d" % student_number)
