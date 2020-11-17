import pymysql

# 打开文件
f = open('./config.txt', 'r')

# \n换行符需要删掉
username = f.readline()[:-1]
password = f.readline()[:-1]
database_name = f.readline()[:-1]

# 打开数据库连接 数据从配置文件中来 配置文件会被ignore掉
db = pymysql.connect("localhost", username, password, database_name)

# 关闭文件连接
f.close()

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# SQL插入语句
# 如果报错，MySQL命令行输入：SET @@global.sql_mode= '';即可
sql = "INSERT INTO user_login(user_id, username, password, telephone, vip) VALUES ('%d', '%s','%s','%s','%d')" \
      % (10012, 'Baolan', '123456', '13141314', 1)

# print(sql)

try:
    # 执行sql语句
    cursor.execute(sql)
    # 执行sql语句
    db.commit()
    # 表示执行成功
    print("执行成功")
except:
    # 发生错误时回滚
    db.rollback()
    # 表示执行失败
    print("执行失败")

# 关闭数据库连接
db.close()
