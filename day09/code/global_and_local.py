# global_and_local.py

# 此示例示意全局变量和局部变量
a = 100  # 全局
b = 200  # 全局

def fx(c):  # fx也是全局,它绑定一个函数
    d = 400  # c,d是局部变量
    a = 9999  # 此处是在创建新的局部变量,不是在修改全局变量
    print(a, b, c, d)  # 9999 200 300 400

fx(300)
print(a, b)  # 100 200
# print(c, d)  # c,d变量在此作用域内不存在
