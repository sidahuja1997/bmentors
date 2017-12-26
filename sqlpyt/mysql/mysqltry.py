import pymysql
conn=pymysql.connect(user='root',passwd='mysql',host='127.0.0.1',port=3306,database='mysql')
cur=conn.cursor()
cur.execute("CREATE TABLE teacher(teacher_id INT,teacher_name VARCHAR);")

