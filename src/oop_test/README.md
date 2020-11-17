# 面向对象

1.定义空类需要`pass`的支持：
```python
class Empty:
    pass
```

2.删除已有的实例变量需要使用`del`，已经del的对象不能再被使用，否则会报错`AttributeError`。

3.实例方法的第一个形参不一定要命名为`self`，但是约定俗成的就是`self`。

4.构造实例需要new对象，但是语法并不是`new Class()`，而是`Class()`。

5.类中直接定义的变量是类变量，而`__init__`中定义的变量是实例变量。

6.动态添加的实例方法不会默认绑定第一个参数`self`，即需要手动传入调用者作为第一个参数；想要自动绑定，需要借助types模块下的MethodType进行包装，即`p.func = MethodType(func, p)`。

7.自动绑定的第一个参数self总是指向调用该方法的对象。<br/>
根据第一个参数出现位置的不同，第一个参数所绑定的对象略有区别：
- 在构造方法中引用该构造方法正在初始化的对象。
- 在普通实例方法中应用调用该方法的对象。

8.类调用实例方法不会默认传入self，其实本质上`User.func(u)`相当于`u.func()`。

9.用`@classmethod`修饰的是类方法，`@staticmethod`修饰的是静态方法。

10.Python没有private，使用双下划綫`__`可以实现数据隐藏。

11.Python支持多继承机制，语法格式是`class SubClass(ParentClass1, ParentClass2)`，前一个父类优先级更高。

12.Python也支持方法重写。

13.`__slots__`属性的值是一个元组，该元组的所有元素列出了该类的实例允许动态添加的所有属性名和方法名。

14.`__bases__`属性可以查看该类的所有直接父类，它会返回所有直接父类组成的元组。