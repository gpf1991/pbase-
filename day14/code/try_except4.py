# try_except3.py

# 此示例示意用try-except 语句来捕获异常,处理错误,将程序由
# 异常状态转换为正常状态

def div_apple(n):
    print("%d个苹果您想分给几个人?" % n)
    s = input('请输入人数: ')
    count = int(s)  # <-- 可以能触发ValueError错误
    result = n / count  # <-- 可能触发ZeroDivisionError错误
    print("每个人分了", result, '个苹果')

try:
    div_apple(10)
    print("分苹果成功")
except ValueError:
    print("分苹果失败,苹果被收回!")
except:
    print("除ValueError类型之外的错误发生了")
    print("错误已捕获并转为正常状态")

# except ValueError:
#     print("分苹果失败,苹果被收回!")
# except ZeroDivisionError:
#     print("分苹果失败,苹果被收回!")


print('程序正常结束')





