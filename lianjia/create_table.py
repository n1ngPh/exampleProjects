import pymysql

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='mysql', charset='utf8')
cursor = db.cursor()
sql = """CREATE TABLE lianjia3 (
         title VARCHAR(200),
         link VARCHAR(200),
         location VARCHAR(200),
         rent VARCHAR(200),
         apartment_type VARCHAR(200),
         apartment_layout VARCHAR(200),
         orientation VARCHAR(200),
         publish_time VARCHAR(200),
         floor VARCHAR(200),
         created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);"""

cursor.execute(sql)
db.commit()
db.close()