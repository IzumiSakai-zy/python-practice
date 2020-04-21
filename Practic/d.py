print("100"*10)
i = 0
s = 0
while i <= 100:
    print(i)
    s += i
    i += 1
    if i == 10:
        break
print(s)
# 赋值运算符（+、-、*、/、//、%、** + =）
a = 0
b = 0
while b <= 10:
    b += 1
    if b == 4:
        continue
    print(b)
