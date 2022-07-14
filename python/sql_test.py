import pymysql
from soupsieve import select

# 打开数据库连接
con = pymysql.connect(host="localhost", port=3306, user='root',
                      password='123456', database='mydb', charset='utf8')

# 使用 cursor() 方法创建一个游标对象
cursor = con.cursor()

# SQL查询语句
sql = "select * from student;"

# 使用 execute()  方法执行 SQL 查询，返回行数
cow_count = cursor.execute(sql)
print("SQL语句执行影响的行数%d" % cow_count)

# 使用 fetchone() 方法获取单条数据.
#data = cursor.fetchone()

# 使用 fetchall() 方法获取全部数据
data = cursor.fetchall()
for line in data:
    print("Database version : %s " % line)

# 关闭数据库连接
con.close()
