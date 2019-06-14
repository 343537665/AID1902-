#将数据存入数据库

from pymongo import MongoClient
#实现大文件存储
import gridfs

#链接数据库
conn =MongoClient("localhost",27017)

#获取数据库对象
db=conn.grid

#获取Ｇridfs对象
fs=gridfs.GridFS(db)

f= open("mj.jpg","rb")

#将内容写入数据库
fs.put(f.read(),filename="mj.jpg")

conn.close()