import sys         # 引入 sys 模块

nums = [1, 2, 3, 4]
it = iter(nums)    # 创建迭代器对象

while True:
    try:
        print(next(it), end=" ")
    except StopIteration:
        sys.exit()
