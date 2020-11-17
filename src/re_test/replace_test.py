import re

phone = "2004-959-559 # 这是一个电话号码"

# sub起到了替换的功能
# 移除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

# 移除非数字的内容
num = re.sub(r'\D', "", phone)
print("电话号码 : ", num)
