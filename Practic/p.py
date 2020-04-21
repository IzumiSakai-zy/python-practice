import the_first_package

the_first_package.printletter.send_text("hahah")  # 包的调用
# 用python打开，读取，关闭文本文档
file = open("Textmessage.txt")  # a,w,r等多种打开方式
text = file.read()
# file.write("hahah")
print(text)
file = open("Textmessage.txt")
text = file.read()  # 读不到内容了
file.close()
# 文件指针即文件从哪里开始读。open-a方法是文本指针在文档开头，-a放在末尾
# read方法结束后在文档的末尾，再次调用read方法是就读不到内容了
# w重写。r只读。a追加。
file1 = open("Textmessage.txt")
while True:
    content = file1.readline()
    if not text:
        break
    print(content)
file1.close()  # 分行读取文本，每次调用readline方法后指针会跳到下一行开始
# *-* coding:utf8 *-*  让python2解释器仍然支持中文
print(eval(input("请输入一道算术题:")))
# eval函数，把一段字符串去掉引号当成可执行代码运算，非常强大
