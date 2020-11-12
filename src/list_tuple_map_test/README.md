# 列表、元组、字典

1.序列封包和序列解包：
- 序列封包：多个值赋给一个变量
- 序列解包：一个列表或者元组赋给多个变量

2.list和tuple的*运算符表示重复而不是逐一乘以一个值

3.list()可将range、tuple转为list

4.append()和extend()
- append() : 将增加的部分作为整体嵌套进去
- extend() : 将增加的部分作为个体追加到尾部

5.删除元素应该用`del`语句而不是什么delete()
```python
a = [2, 4, 6, 8, 20]
del a[1:3]
```

6.修改列表数据可以直接使用切片整体赋值

7.append()可以起到push()即入栈的作用

8.pop()出栈时也一样会返回出栈的值

9.list的sort()很方便 默认升序
```python
a = ['C++', 'Java', 'Python', 'Ruby', 'JavaScript']
a.sort(key=len, reverse=True)
```

10.dict()创建字典时，key的字符串不需要引号，直接用即可

11.判断字典是否含有某个key可以使用`in`或者`not in`而不是containsKey()之类的方法

12.字典新增k-v对可以直接赋值

13.for...in循环可以起到foreach的作用来遍历集合

14.for...in遍历字典的范例
```python
dic = {'Chinese':95, 'Math':98, 'English':97}
for key, value in dic.items():
    print('Key:', key)
    print('value', value)
```

15.zip()压缩多个列表生成一个可迭代对象，于是便可以使用一个for循环同时遍历N个关联列表

16.reversed()可以翻转序列；sorted()可以将序列排序。
