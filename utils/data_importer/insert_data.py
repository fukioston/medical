import pymysql
import csv
import pandas as pd

conn = pymysql.connect(
    host="127.0.0.1",
    port=3306,
    database="medical",
    charset="utf8",
    user="root",
    passwd="a6782533"
)
cursor = conn.cursor()

# 读取 CSV 文件并添加列名
csv_file = 'column_articles.csv'
csv_columns = ['id', 'catalog', 'article_name', 'img_url', 'content', 'uploader_id', 'upload_time', 'likes', 'click',
               'status']  # CSV 列名顺序
data = pd.read_csv(csv_file, header=None, names=csv_columns)

# 循环遍历 DataFrame，构建插入语句并插入数据库
for index, row in data.iterrows():
    insert_sql = "INSERT INTO column_articles ( catalog, article_name, img_url, content, uploader_id, upload_time, likes, click, status) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (
    row['catalog'], row['article_name'], row['img_url'], row['content'], row['uploader_id'], row['upload_time'],row['likes'], row['click'], row['status'])
    cursor.execute(insert_sql,values)


insert_sql_2 = "INSERT INTO user_userinfo(username,password,email,mobile_phone,profile_img,identity) VALUES(%s,%s,%s,%s,%s,%s)"
values_2 = ('admin','12345678','12345678','12345678910','doge.jpg','admin')
cursor.execute(insert_sql_2, values_2)
# 提交事务并关闭连接
conn.commit()
conn.close()
