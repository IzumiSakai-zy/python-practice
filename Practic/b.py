age = int(input("What 's your age?"))
if 18 >= age >= 0:
    print("OK")
else:
    print("Not OK")
is_employee = True  # 赋值为布尔值
if not is_employee:
    print("No entering")
holiday = input("What's the date today?")
if holiday == "情人节":  # 必须加引号
    print("买玫瑰")
elif holiday == "生日":  # 必须加引号
    print("买蛋糕")
elif holiday == "平安夜":  # 必须加引号
    print("买苹果")

