import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)

# key是"food" value是"mutton" 将键值对存入redis缓存
r.set('name', 'sam', ex=3)

# mutton 取出键food对应的值
print(r.get('name'))
