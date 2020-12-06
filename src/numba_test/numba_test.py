import numpy as np
from numba import jit


@jit(nopython=True)  # jit，numba装饰器中的一种
def for_fun1():
    j = 0
    for i in range(1000):
        j += i


def for_fun2():
    j = 0
    for i in range(1000):
        j += i


@jit(nopython=True)
def go_fast1(a):  # 首次调用时，函数被编译为机器代码
    trace = 0
    # 假设输入变量是numpy数组
    for i in range(a.shape[0]):  # Numba 擅长处理循环
        trace += np.tanh(a[i, i])
    return a + trace


def go_fast2(a):
    trace = 0
    # 假设输入变量是numpy数组
    for i in range(a.shape[0]):  # Numba 擅长处理循环
        trace += np.tanh(a[i, i])  # numba喜欢numpy函数
    return a + trace  # numba喜欢numpy广播


# 因为函数要求传入的参数是nunpy数组
# x = np.arange(100).reshape(10, 10)
