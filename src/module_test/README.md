# 模块化

1.导入模块的方法：
- `import module1[as rename1], module2[as rename2], ...`：本质是将`module_name`中的全部代码加载到内存并执行，然后将整个模块内容赋值给与模块同名的变量，该变量的类型是module，而在该模块中定义的所有程序单元都相当于该module对象的成员。
- `from module import name1[as rename1], name2 [as rename2], ...`：本质是将`module_name`中的全部代码加载到内存并执行，然后只导入指定变量、函数等程序单元，而不会将整个模块导入。

2.`__all__`变量指定了模块可导出的成员。

3.`dir()`可以查看模块的内容。

4.模块的`__file__`属性可以查看到指定模块的源文件路径。

5.使用`__doc__`查看模块的文档内容。
