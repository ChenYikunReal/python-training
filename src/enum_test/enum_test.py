import enum

# 定义Season枚举类
Season = enum.Enum('Season', ('SPRING', 'SUMMER', 'FALL', 'WINTER'))
# 直接访问指定枚举
print(Season.SPRING)
# 访问枚举成员的变量名
print(Season.SPRING.name)
# 访问枚举成员的值
print(Season.SPRING.value)

# 根据枚举变量名访问枚举对象
# Season.SUMMER
print(Season['SUMMER'])
# 根据枚举值访问枚举对象
# Season.FALL
print(Season(3))

# 遍历Season枚举的所有成员
for name, member in Season.__members__.items():
    print(name, '=>', member, ',', member.value)


# 继承Enum
class Orientation(enum.Enum):
    # 为序列值指定value值
    EAST = '东'
    SOUTH = '南'
    WEST = '西'
    NORTH = '北'

    def info(self):
        print('这是一个代表方向【%s】的枚举' % self.value)


print(Orientation.SOUTH)
print(Orientation.SOUTH.value)
# 通过枚举变量名访问枚举
print(Orientation['WEST'])
# 通过枚举值来访问枚举
print(Orientation('南'))
# 调用枚举的info()方法
Orientation.EAST.info()
# 遍历Orientation枚举的所有成员
for name, member in Orientation.__members__.items():
    print(name, '=>', member, ',', member.value)
