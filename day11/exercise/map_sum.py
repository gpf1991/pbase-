#   1. 求 1**2 + 2**2 + 3**2 + ... + 9**2 的和
#   2. 求 1**3 + 2**3 + 3**3 + ... + 9**3 的和
#   3. 求 1**9 + 2**8 + 3**7 + ... + 9**1 的和


# 1. 求 1**2 + 2**2 + 3**2 + ... + 9**2 的和
# 方法1
def pow2(x):
    return x ** 2
s = 0
for x in map(pow2, range(1, 10)):
    s += x
print("1) 和是:", s)

# 方法2
print("1) 和是:", sum(map(lambda x: x**2, range(1, 10))))

# 2. 求 1**3 + 2**3 + 3**3 + ... + 9**3 的和
print("2) 和是:", sum(map(lambda x: x**3, range(1, 10))))

# 3. 求 1**9 + 2**8 + 3**7 + ... + 9**1 的和
print(sum(map(pow, range(1, 10), range(9, 0, -1))))


