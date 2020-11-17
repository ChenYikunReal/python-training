# doctest模块确认代码的结果是否与文档一致
import doctest


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)


# 自动验证嵌入测试
doctest.testmod()
