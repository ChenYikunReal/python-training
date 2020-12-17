# Python有趣的基础知识

1.格式化输出：
```python
your_name = "Bob"
my_name = "Sam"
print(f"Hello, {your_name}! I'm {my_name}")
```
输出结果：

```text
Hello, Bob! I'm Sam
```

2.格式化输出：

```python
print("Hello, my name is {}.".format("Sam"))
```
输出结果是：

```text
Hello, my name is Sam.
```

3.三种方法实现单行、多行注释：

法1：
单行注释：Shift + #（在代码的最前面输入，非选中代码进行注释）
多行注释：同单行一样在每一行的前面输入Shift+#

法2：
单行和多行一样的方式：选中需要注释的代码，Ctrl+/，写Java的时候就是常用的方法

法3：
输入''' '''或者""" """，将要注释的代码插在中间

4.Python与Java在*的非数值运算用法的对比：

首先看一下Java的'a'*10：
```java
System.out.println('a'*10);
```
得到：

```java
970
```
然后是Java的"a"*10：
```java
System.out.println("a"*10);
```
会报错的。

解释：
Java中'a'的类型为char，char实际上是一个数值按照其ASCII码值映射的字符，可以做数值运算。'a'的ASCII码值为97，相当于97*10=>970。
Java中的字符串不可以与数值相乘。

再看看Python：

```python
print('a'*10)
```
```python
print("a"*10)
```
得到：

```text
aaaaaaaaaa
```
```text
aaaaaaaaaa
```
解释：
""和''其实是等效的，*在Python里可以用来将字符/字符串复制n遍，这里是10遍。

5.Python与Java在+的非数值运算用法的对比：

首先看一下Java的'a'+10：
```java
System.out.println('a'+10);
```
得到：

```java
107
```
然后是Java的"a"+10：
```java
System.out.println("a"+10);
```
```java
a10
```

解释：
Java中'a'的类型为char，char实际上是一个数值按照其ASCII码值映射的字符，可以做数值运算。'a'的ASCII码值为97，相当于97+10=>107。
Java中的字符串的+相当于把10变为字符串与已有字符串连接，得到“a10”。

再看看Python：

```python
print('a'+10)
```
```python
print("a"*10)
```
都会报错。

即使这样：

```python
print("a", 10)
```
也是相当于打印两个变量，中间会有空格，始终不是一个变量。

解释：
""和''其实是等效的，在Python里字符串不能与数值直接相加。

6.""""""是可以的，“ “ “ ” ” ”是不对的。

7.直接将用户输入转化：
转成int：

```python
x = int(input())
```

转成float：

```python
y = float(input())
```
8.Python的print()从某种程度上相当于Java的System.out.println()或者说C#的Console.Writeline()，这是说执行后会换行。如果我们不想换行，可以这样：

```python
print("Hello, ", end=' ')
```
9.格式化的强化

```python
formatter = "{} {} {}"

print(formatter.format(7, 9, 8))
print(formatter.format("李华", "李刚", "李想"))
print(formatter.format(formatter, formatter, formatter))
print(formatter.format(True, True, False))
print(formatter.format("哈哈", "嘎嘎", "呵呵"))
```
结果：

```text
7 9 8
李华 李刚 李想
{} {} {} {} {} {} {} {} {}
True True False
哈哈 嘎嘎 呵呵
```
10.导入命令行参数

```python
from sys import argv

a, b, c, d = argv

print("a is: ", a)
print("b is: ", b)
print("c is: ", c)
print("d is: ", d)
```
可以在命令行运行的时候输入命令行参数：

```text
test.py BeiJing ShangHai GuangZhou ShenZhen
```
这个就好像Java里面

```java
public static void main(String[] args){}
```
这个语句的args[]数组。

传入的都是字符串，哪怕是1,2,3这样的数值。


11.一些Python的库介绍
| Python框架 | 主要用途简介 |
|--|--|
| Django | Web开发工具库 |
| Numpy | 大量的维度数组与矩阵运算的数学函数库 |
| Matplotlib | 数据可视化库，多与Numpy配合使用 |
| Scipy | 机器学习和数值分析库 |
| Pandas | 数据操纵和分析库 |
| PyGame | 游戏开发库，带图形界面和声音 |
| ScraPy | 网络爬虫库 |
| TensorFlow | 机器学习和数据可视化库 |
| Requests | 简单易用的HTTP库 |
| Kivy | 桌面应用和移动平台的用户界面库 |
| Natural Language Tool Kit | 自然语言处理库，可用于分析文本、垃圾邮件过滤、自动聊天机器人 |

12.虽然python的命名多采用下划线（_），但是类的命名建议采用驼峰式。

13.建议采用比较一致的方式组织函数或者类的方法，比如：函数A参数为(x, y, z)，B也需要用到x, y, z，那相对来讲写成(x, y, z)总比(y, z, x)易于管理。

14.亲，好好写注释，好好写文档！！

15.代码内部适当留白，应该有必要的空格或者空行以增强可读性。

16.像JavaScript这种原型（prototype）语言中，类和对象除了用法以外没多少不同，对象从某种程度上可以看做类的副本，然而Python里面类很像创建对象的模板，这点和Java类似。

17.super和__init__的搭配使用：

```text
super(Child, self).__init__()
```
在Java里就是相当于：
```java
super();
```
~~（这么说也不是太准确其实）~~ 

18.大部分可以使用继承的场合都可以使用组合取代或者简化，而多重继承则需要不惜一切地避免。
（Java没有多继承并利用Interface来补充缺乏多继承的灵活性，这个设计真的强）

19.python有这样的写法：class className(object)，这个语法吧，写也行不写也行，一般还是懒得写。这就好像Java里所有的类都是java.lang.Object的子类，然而并没有必要去写:
```java
public class A extends Object {}
```
这玩意自己决定吧……

20.Python面向对象里的self就可以用Java里的this来理解，只不过两门编程语言还是有语法使用上的差别的。

21.Python中有一种“key-value”的模式，应用广泛。
这个东西不要仅仅想到“字典”数据结构，再想想，是不是模块啊，类啊也是通过"XXX.key"的方式调用出"value"的呢？
这个概念是一个广泛应用的概念。

22.模块（module）的一些说明：

 - 模块是包含函数和变量的Python文件(.py)
 - 可以导入这些文件（import）
 - 可以使用.操作符访问模块中的函数和变量
 - 类与模块也是异曲同工的，只不过一个面向过程，一个面向对象

23.collections.OrderedDict是可排序的字典结构。
字典这东西，Java也有java.util.Dictionary，可以用Java里的java.util.Map类比，都是“ket-value”。
至于能排序的Dic，Java的java.util.TreeMap说的直白点儿，不就是红黑树支持的排序Map吗……

24.Python这个“切片”是真的强，Java就必须顺着来，Python就无所谓，可以正着来也能倒着来，还能一端“开放不限界”。不过，“左闭右开”是通用的。

25.通用的经验：不要等全部开发完再测试，单元测试、模块化的测试应该及时的做好啊~~

26.Java里面啊，想给用户输入加提示信息就非得先Sytem.out.print()一下，Python就可以直接在input()里加入参数，这个参数其实是打印给用户看的。

```python
x = input("请输入一个数字")
```

27.Python的输入还是挺方便的，input()省事啊……
先看看Python的写法：
```python
x = input()
```
看看Java的写法：
```java
import java.util.Scanner;

        //类和方法省却了……直接写代码
        Scanner scan = new Scanner(System.in);
        String x = scan.next();
        scan.close();
```

差距啊……人生苦短，我用Python……

28.for循环写起来更简洁，而且用于for each写法显得更简单。
But，while确实是可以对任何对象进行循环，适用面较广。
while最恶心的是它有可能一直“停不下来”。
比如说，在Java中，我总是被这样的写法恶心到炸裂：
```java
while(scan.hasNext()) {
    String a = scan.next();
}
```
这操作，啥时候是个尽头啊……我的天……
建议：

 - 少使用while循环，大部分的时候for循环能用的话是更优选择。
 - 检查好while循环的判断语句，确保有False存在的可能性，防止死循环。
 - 如果不能确定，在while循环的开始和结尾打印出需要测试的值，看看变化。

while(true)可以写具有某种退出条件的“无限循环”——某些想一直跑下去的命令行程序就需要一个while(true)的大循环。

不过，之前有看过Java编译后的结果，for(;;)和while(true)其实是等效的，只不过编译的过程目前我就不晓得了。

29.列表和数组的区别需要因编程语言而异。
从传统的、经典的定义看来，二者很不同，但是现在的很多编程语言有一些与传统规定不同的地方。
Ruby里面列表、数组统称数组。
而伟大的Python里面列表、数组统称列表。
不用问，问就是规定……

30.in range()这个操作不只是用于for i in range(x)，还可以这么玩：

```python
x = int(input("请输入一个整数，将检查其是否在1~5"))
print(x in range(1, 6))
```
其实我想，这才是本意吧……

31.Python是有 not or （或非）和 not and （与非）的，不过可不能那么写啊……

```text
not(a and b)
not(a or b)
```
这样才是正解（前提是a，b均为布尔型变量）

32.UTF-8支持中文编码的，不过它的编码是这样的：（概述）
大部分常用的编码用8位编码，如果不够再换用16位、32位表示。
UTF-8的标准还是挺常用的。
不过Windows系统中文编码貌似用的是GBK而非UTF-8，搞不好可是会乱码的啊~~

33.readline()读文件，关键在于读“\n”。同样的，该函数返回结果带有“\n”换行符，这个是需要注意的。
print的话可以加一个end=' '参数。

34.open文件指定字符集是可以的啊,比如：

```python
lang = open("lang.txt", encoding="utf-8")
```

35.有这样一个东西：*args

```python
def f(*args):
    pass
```
其实就是和argv那东西挺像，只不过这是函数调用，那是命令行参数传入程序。

36.看这样的写法：

```txt
data = open(file).read()
```
这样的话就没法运行close()了，因为read()一旦运行，文件就会被Python关掉……

37.exists是个好东西啊

```python
from os.path import exists
```
上面的语句可以调出来exists。

```txt
print(f"这个文件存在吗？{exists(file)}")
```
这样可以先判一下文件存在不存在，这是挺重要的东西，可以提前排错。

Java给我印象很深的一个是：instanceof
用这个instanceof确实能在ClassCast的时候安全一些。


38.Python增量赋值语法：

```txt
var = var + 1
```
或者是

```txt
var += 1
```
但是下面的语句会报错：

```txt
var++
```

这就比较起Java、C等编程语言，是一个需要适应的点，毕竟没有简便的++var和var++了啊！
不过，Java里非整型变量不能直接自增自减。
Python毕竟不是直接定义了类型，所以这么写也是可以理解的啊。

39.Python运算符有一些和Java、C等编程语言不同的点：
它支持整除（//）、非整除（/）和指数（**）两种运算。
Java里想做指数运算就比这个麻烦得多：

```java
double result = Math.pow(a, b);
```

40.eval()、int()、float()、str()函数可以直接用于input()函数内部，也可以另作他用。
看下面的示例：

```python
print(int("23"))
print(float("23"))
print(eval("23"))
print(str(23))
print(eval("23.5"))
x = 5
print(eval("23 + (2 *x)"))
```
输出：

```python
23
23.0
23
23
23.5
33
```
归纳：

 - int()可以将字符串转换成整型
 - float()可以将字符串、整型转换成浮点型
 - str()可以将数值型转换成字符串
 - eval()可以计算相应表达式，赋值为相应的数值类型（整型或浮点型）

41.下面是表示字符串内行连续的两种方式，请看下面的示例：

```python
a = "Hello, " + \
	"World!"
```

```python
b = ("Hello, " + 
	"World ~ Again!")
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120183708988.PNG)

而Java由于是{} 、[] 、() 、; 、，这些起到分隔作用的来决定，String的对象可以这么写：

```java
String a = "Hello, " + 
	"World!";
```

42.Python的print()有两个需要记住的参数：
sep=“” 和 end=""
看下面的例子：

```python
print("Hello", "World", sep="**")
print("Hello", "World", sep="")
print("1", "+", "2", "=", "3", sep=" ")
print("Hi", "Sam", sep="#", end=" ")
```
输出结果

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120184509519.PNG)

总结：
sep="sepString"中，sepString替换了分隔符Space（" "）
end="endString"中，endString替换了换行符Enter（"\n"）

43.Python输出域内对齐
如果字符串长度没达到指定的长度，则不够的部分用空白补齐；否则（超出长度），对齐无效。
对齐方式三种：

 - ljust(n)：左对齐
 - rjust(n)：右对齐
 - center(n)：居中对齐

看下面的例子：

```python
print("012345678901234567890123456789")
print("Rank".ljust(5), "Player".center(22), "HR".rjust(3), sep="")
print("1".ljust(5), "XiaoBiao".center(22), "100".rjust(3), sep="")
print("2".ljust(5), "XiaoChi".center(22), "98".rjust(3), sep="")
print("3".ljust(5), "XiaoDai".center(22), "93".rjust(3), sep="")
print("4".ljust(5), "XiaoSha".center(22), "60".rjust(3), sep="")
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120185952455.PNG)

非常遗憾的是，我们用中文就不怎么理想：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120190022539.PNG)

44.格式化数值（主要是浮点数）输出
| 语句 | 输出 | 说明 |
|--|--|--|
| print("{0:10d}".format(12345678)) | 12345678 | 数字是个整型 |
| print("{0:10,d}".format(12345678)) | 12,345,678 | 添加千分符 |
| print("{0:10.2f}".format(1234.5678)) | 1234.57 | 四舍五入 |
| print("{0:10,.2f}".format(1234.5678)) | 1,234.57 | 四舍五入并添加千分符 |
| print("{0:10,.3f}".format(1234.5678)) | 1,234.568 | 四舍五入并添加千分符 |
| print("{0:10.2%}".format(12.345678)) | 1234.57% | 转换为百分数、四舍五入并添加千分符 |
| print("{0:10,.3%}".format(12.345678)) | 1,234.568% | 转换为百分数、四舍五入并添加千分符 |


45.列表的split()和join()方法

- split()：将字符串分割生成列表
- join()：将列表元素拼接成字符串

看下面的例子：

```python
print("a,b,c".split(","))
print("a**b**c".split("**"))
print("a\nb\nc".split())
print("a b c".split())
```
查看输出：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120191243636.PNG)

注意，split()方法没传参数，参数默认是空白字符，这个空白字符可以是Space、Tab、Enter
接着看例子：

```python
hello = ["H", "e", "l", "l", "o"]
print(hello)
print(" ".join(hello))
world = ["W", "o", "r", "l", "d"]
print(", ".join(world))
```
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120191644504.PNG)

这种操作是非常常见的，而Python的支持也使其变得十分简单。
这方面Java也有支持（IDEA打开）：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120193129568.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg5NjMxOA==,size_16,color_FFFFFF,t_70)![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120193144126.PNG?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80Mzg5NjMxOA==,size_16,color_FFFFFF,t_70)
上面的代码是我自己以前写着玩的某一个项目的部分代码（写的挺烂），不过可见Java里这种切分与组合还是很重要的！

46.注意下面的语句：

```python
list1 = ["1", "2"]
list2 = list1
del list1[-1]
print(list2)
```

![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120191936965.PNG)


可见：这里是浅复制！！这里是比较深的知识，在Java里深拷贝也是比较有趣的知识，建议感兴趣的读者了解一下。
浅复制可以简单地解释为：这两个对象指向同一块内存空间，一个改变则全都改变。

47.Python里面，切片等操作也是不能索引越界的呀！
否则会爆出IndexError（只不过Python允许负数索引，即“倒着找”）。
Java则是IndexOutOfBoundsException那种异常。
看下面的例子：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120192556904.PNG)
![在这里插入图片描述](https://img-blog.csdnimg.cn/20191120192604543.PNG)
48.Python一些分析string内部字符后返回True/False的方法：
| 方法 | 返回True的条件 |
|--|--|
| str1.isdigit() | str1的所有字符都是数字 |
| str1.isalpha() | str1的所有字符都是字母 |
| str1.isalnum() | str1的所有字符都是字母或者数字 |
| str1.islower() | str1的所有字符都是小写字母 |
| str1.isupper() | str1的所有字符都是大写字母 |
| str1.isspace() | str1的所有字符都是空白字符 |


49.Python也有一个判断类型的神奇方法——isinstance()：
语法格式：
```txt
isinstance(item, dataType)
```
返回布尔类型

50.简化表达式条件：

（1）先看一个例子：
```txt
(state == "A") or (state == "B") or (state == "C") or (state == "D")
```
可以简化为：

```txt
state in ["A", "B", "C", "D"]
```

（2）下面的表达式：

```txt
(x > 10) and (x <= 20)
```
可以写成：

```txt
10 < x <= 20
```
~~（这是C、Java等语言不能写的，我大Python就是行，牛不牛？）~~ 


（3）还有下面的语句：

```txt
(x >= 20) or (x <= 10)
```
可以利用德.摩根律转换为：

```txt
not(10 < x < 20)
```

51.Python的集合（Set）的重要方法：

 - add()：增
 - discard()：删
 - clear()：清空

还有这样的方法
set([...]) / set((...))可以将列表或者元组转换成无序集合

Python还支持集合论的基本操作——交/并/差 等：

 - set1.union(set2)：并集
 - set1.intersection(set2)：交集
 - set1.difference(set2)：差集
