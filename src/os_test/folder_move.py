import os
import shutil

# 列出当前目录下的所有文件
path = './'
files = os.listdir(path)

# 遍历文件
for f in files:
    # 以扩展名为目录名
    folder_name = path + f.split('.')[-1]
    # 不存在该目录，则创建
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        # 移动文件到目录
        shutil.move(f, folder_name)
    else:
        shutil.move(f, folder_name)

