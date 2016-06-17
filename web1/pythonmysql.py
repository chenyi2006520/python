import mysql.connector

conn = mysql.connector.connect(user="root",password="1988chenyi@",db="mydbforcy",host="localhost")
cursor = conn.cursor()
cursor.execute("select * from ktm_bsw_event")
resualts = cursor.fetchall();
for res in resualts:
    print(res)
    
cursor.close()
conn.close()