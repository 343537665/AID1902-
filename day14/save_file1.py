#小文件从数据库中提取方案

from pymongo import MongoClient

#bson模块：存储小文件，
import bson.binary

#链接数据库
conn =MongoClient("localhost",27017)

#获取数据库对象
db=conn.image

#获取集合MM对象
myset=db.MM

#提取图片(是一个字典｛1个名字：1个是内容｝)
img=myset.find_one({"filename":"mj.jpg"})

#将内容写入本地
with open("mj.jpg","wb") as f:
    #通过键data获取值（图片内容）
    # 通过键filename获取值（图片名字）
    f.write(img["data"])

conn.close()
