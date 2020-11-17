import random

# 列表中随机抽一个枚举值
print(random.choice(['apple', 'pear', 'banana']))

# 100以内随机抽10个整数
print(random.sample(range(100), 10))

# 抽一个随机浮点数
print(random.random())

# 6以内随机抽一个整数
print(random.randrange(6))
