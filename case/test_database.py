"""
    目标：自动化测试中操作项目数据库
    案例：
        判断用户id（1）是否收藏了id为2的文章
        1- 未收藏 0-收藏
"""

# 导包 pymysql
import pymysql

# 获取连接对象
conn = pymysql.Connect(
            host="127.0.0.1",
            user="root",
            passwd="123456",
            db="srs")
# 获取游标对象
cursor = conn.cursor()
# 执行方法 sql
sql = "select * from tbstudent"
cursor.execute(sql)
# 获取结果并进行断言 0-收藏
# print(cursor.fetchone())
result = cursor.fetchone()

# 断言 0为收藏
# assert 0 == result[0]

# 关闭游标对象
cursor.close()
# 关闭连接对象
conn.close()


