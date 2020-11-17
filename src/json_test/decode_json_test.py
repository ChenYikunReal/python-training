import json

# 将JSON字符串恢复成Python列表
result1 = json.loads('["Sam", {"favorite": ["coding", null, "game", 25]}]')
# ['Sam', {'favorite': ['coding', None, 'game', 25]}]
print(result1)

# 将JSON字符串恢复成Python字符串
result2 = json.loads('"\\"foo\\"bar"')
# "foo"bar
print(result2)


# 定义一个自定义的转化函数
def as_complex(dct):
    if '__complex__' in dct:
        return complex(dct['real'], dct['imag'])
    return dct


# 使用自定义的恢复函数
# 自定义回复函数将real数据转成复数的实部，将imag转成复数的虚部
result3 = json.loads('{"__complex__": true, "real": 1, "imag": 2}', object_hook=as_complex)
# (1+2j)
print(result3)
# 打开a.json文件
f = open('a.json')
# 从文件流恢复JSON列表
result4 = json.load(f)
# ['Java', {'Python': 'excellent'}]
print(result4)
