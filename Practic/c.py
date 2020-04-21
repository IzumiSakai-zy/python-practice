def judge(player, computer):
    if ((player == 1 and computer == 2)
            or (player == 2 and computer == 3)
            or (player == 3 and computer == 1)):
        print("恭喜你胜利了")
    else:
        print("非常遗憾你输了")


while True:
    player = int(input("【1=石头，2=剪刀，3=布】你要出的拳是： "))
    import random
    computer = random.randint(1, 3)
    print("你要出的拳是[%d] - 电脑出的拳是[%d]" % (player, computer))
    if player == computer:
        print("再来一次")
        print("="*50)
        continue
    judge(player, computer)
    break

