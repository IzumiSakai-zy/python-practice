print((1, 2, 3, 4, 5)[1:3])  # 切片
str = "quanshuijiejie"
print(str[2:8])  # 切片
print(["name-banjingquanshui", "age-40", "gender-fomale"] * 4)  # 相乘变成一个列表元祖，但字典不能
print((1, 2) + (3, 4, "43"))  # 加号拼接
print(4 in [1, 2, 3, 4])
print(4 not in [1, 2, 3, 4])  # in和not in
for num in [1, 2, 3]:
    print(num)
    # if num==2:
    #   break
else:
    print("会执行吗？")
# for-else完整结构，当for遍历完后即执行else，只有当for未执行完强行break才不执行else
# 一般不会用到，专门为for遍历寻找准备
find_example = {"name": "banjingquanshui", "age": 40}
print(find_example["age"] == 40)  # 寻找字典中的某个值
