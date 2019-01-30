# 练习:
#   写程序
#     1) 将如下信息形成一个字典 seasons
#       '键'        '值'
#        1      '春季有1,2,3月'
#        2      '夏季有4,5,6月'
#        3      '秋季有7,8,9月'
#        4      '冬季有10,11,12月'
#    2) 让用户输入一个整数代表这个季度,打印这个季度的信息,
#    如果用户输入的信息不在字典内,则打印"信息不存在"


# 方法1
# seasons = {}
# seasons[1] = '春季有1,2,3月'
# seasons[2] = '夏季有4,5,6月'
# seasons[3] = '秋季有7,8,9月'
# seasons[4] = '冬季有10,11,12月'

seasons = {
    1: '春季有1,2,3月',
    2: '夏季有4,5,6月',
    3: '秋季有7,8,9月',
    4: '冬季有10,11,12月',
}

print(seasons)

n = int(input("请输入季度: "))
if n in seasons:
    print(seasons[n])
else:
    print("信息不存在")

        
  