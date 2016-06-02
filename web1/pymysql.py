#coding:utf8

#import MySQLdb
#conn = MySQLdb.connect(host='127.0.0.1',user='root',passwd='1988chenyi@',db='mydbforcy')
#cur = conn.cursor()#获得指向数据库的指针
#cur.execute("select * from ktm_bsw_event")
#result = cur.fetchall()#获得每行的信息
#for res in result:
 #   print(res) #格式化输出 
    
# cur.close()
# conn.close()


import mysql.connector
import sys,os

conn = mysql.connector.connect(user="root",password="1988chenyi@",host="localhost",database="mydbforcy")
cursor = conn.cursor()
cursor.execute('select * from ktm_bsw_event')
result = cursor.fetchall()
for res in result:
    print(res)
cursor.close()
cursor.close()

