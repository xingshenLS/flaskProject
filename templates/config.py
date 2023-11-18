#数据库连接配置
import pymysql

conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='LarryAndSally04',
        database='login'
    )
