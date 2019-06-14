#获取数据库中grid数据库的文件

from pymongo import MongoClient
#实现大文件存储
import gridfs

#链接数据库
conn =MongoClient("localhost",27017)

#获取数据库对象
db=conn.grid

#获取gridfs对象
fs=gridfs.GridFS(db)

#获取grid库中集合的对象
files=fs.find()

#分别取每个文件名称
for file in files:
    if file.filename=="mj.jpg":
        #创建文件　并绑定文件对象f（file.filename获取数据库文件的对象文件名字）
        with open(file.filename,"wb") as f:
            #丛数据库读取内容
            data=file.read()
            #写入到本地
            f.write(data)

