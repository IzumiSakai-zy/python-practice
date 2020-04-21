def wuNaoKaiGenHao(a, b, d):
    c = (a + b) / 2
    while (c ** 2 - d) < -0.000000000001 or (c ** 2 - d) > 0.000000000001:
        c = (a + b) / 2
        if a ** 2 < d and d < c ** 2:
            b = c
            print(c)
        else:
            a = c
            print(c)
        if (c ** 2 - d) > -0.000000000001 and (c ** 2 - d) < 0.000000000001:
            print("程序结束")
            break


wuNaoKaiGenHao(5, 6, 35)
