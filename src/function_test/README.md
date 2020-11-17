# 函数

![](/images/python-function.png)

1.函数的多个返回值会被封装成元组。

2.可以为函数设置参数的默认值。

3.函数修饰器方法：
```python
def funA(fn):
    print('A')
    fn()
    return 'A'

@funA
def funB():
    print('B')

print(funB)
```
相当于`funA(funB)`

被修饰的函数总是被替换成@符号所引用的函数的返回值，因此被修饰的函数由@所引用的函数的返回值决定——如果@所引用的函数的返回值是函数，那么被修饰的函数在替换之后还是函数。




