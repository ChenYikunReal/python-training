# Python多线程吐槽

为啥不想学Python多线程？

因为Python多线程编程并不能真正利用多核的CPU！

《Python参考手册》有云：
>在大多数系统上，Python同时支持消息传递和基于线程的并发编程。尽管大多数程序员熟悉的往往是线程接口，但实际上Python线程受到的限制有很多。尽管最低限度是线程安全的，但Python解释器还是采用了内部的GIL(Global Interpreter Lock, 全局解释器锁定)，在任意指定的时刻只允许单个Python线程执行，无论系统上存在多少个可用的CPU核心。这限制了Python程序实际只能在单个处理器上运行。尽管GIL经常是Python社区中争论的热点，但可以预见的将来它都不可能消失。

所以，说的不好听点儿，学它干啥？换门语言再去尝试并发编程的原理吧！