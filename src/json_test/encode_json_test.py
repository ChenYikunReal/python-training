import json

# 将Python对象转JSON字符串（元组会当成数组）
s = json.dumps(['Sam', {'favorite': ('coding', None, 'game', 25)}])
# ["Sam", {"favorite": ["coding", null, "game", 25]}]
print(s)
# 简单的Python字符串转JSON
s2 = json.dumps("\"foo\bar")
# "\"foo\bar"
print(s2)
# 简单的Python字符串转JSON
s3 = json.dumps('\\')
# "\\"
print(s3)
# Python的dict对象转JSON，并对key排序
s4 = json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)
# {"a": 0, "b": 0, "c": 0}
print(s4)
# 将Python列表转JSON，
# 并指定JSON分隔符：逗号和冒号之后没有空格（默认有空格）
s5 = json.dumps([1, 2, 3, {'x': 5, 'y': 7}], separators=(',', ':'))
# 输出的JSON字符串中逗号和冒号之后没有空格
# '[1,2,3,{"4":5,"6":7}]'
print(s5)
# 指定indent为4，意味着转换的JSON字符串有缩进
s6 = json.dumps({'Python': 5, 'Kotlin': 7}, sort_keys=True, indent=4)
print(s6)
# 使用JSONEncoder的encode方法将Python转JSON
s7 = json.JSONEncoder().encode({"names": ("孙悟空", "齐天大圣")})
# {"names": ["\u5b59\u609f\u7a7a", "\u9f50\u5929\u5927\u5723"]}
print(s7)
f = open('a.json', 'w')
# 使用dump()函数将转换得到JSON字符串输出到文件
json.dump(['Java', {'Python': 'excellent'}], f)
