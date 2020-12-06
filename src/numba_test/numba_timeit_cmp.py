from numba_test import for_fun1, for_fun2
from timeit import Timer

'''
for_fun1()
0.07777590000000001
for_fun2()
49.8972476
'''
print('for_fun1()')
for_fun1()
print(Timer('for_fun1()', 'from numba_test import for_fun1').timeit())
print('for_fun2()')
for_fun2()
print(Timer('for_fun2()', 'from numba_test import for_fun2').timeit())
