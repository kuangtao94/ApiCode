# Json字符串进行新增操作
import json
import os

# os.path.dirname(__file__)：表示当前目录
path = os.path.join(os.path.dirname(os.path.dirname(__file__)),'data/login.json')

# 定义读取文件方法
def read_a():
    # 打开文件
    with open(path,'r') as fp:
        # 读取返回文件
        return fp.read()
# loads 反序列化，str装换为python对象
temp = json.loads(read_a())

# 向Temp对象中新增对象
temp.update(
    {'id':'123',"name":"ad"}
)

# dumps序列化：Python对象转换为Json对象
new = json.dumps(temp)

# str数据追加
with open(path,'w+') as fp:
    fp.write(new)
