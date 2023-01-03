# Mongodb vs Python3 3.8.10

- [Mongodb vs Python3 3.8.10](#mongodb-vs-python3-3810)
    - [MongoDB](#mongodb)
    - [Intsall Mongodb](#intsall-mongodb)
    - [Create database](#create-database)
    - [Creating a Collection (Table)](#creating-a-collection-table)
    - [Insert Document (Row)](#insert-document-row)
    - [Find](#find)
    - [Query with regex](#query-with-regex)
    - [Sort](#sort)
    - [Delete Document](#delete-document)
    - [Drop Collection](#drop-collection)
    - [Update](#update)
    - [Limit](#limit)


### MongoDB
| Mysql  | MongoDB                     |
|--------|-----------------------------|
| Table  | Collection                  |
| Row    | Document                    |
| Column | Field                       |
| Join   | Embedded documents, linking |

### Intsall Mongodb
* direct to local - follow [here](https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/)
``` php
$ sudo apt-get install gnupg
$ wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ echo "mongodb-org hold" | sudo dpkg --set-selections
$ echo "mongodb-org-database hold" | sudo dpkg --set-selections
$ echo "mongodb-org-server hold" | sudo dpkg --set-selections
$ echo "mongodb-mongosh hold" | sudo dpkg --set-selections
$ echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
$ echo "mongodb-org-tools hold" | sudo dpkg --set-selections
$ sudo systemctl enable mongod
```
* install with docker- follow [here](https://github.com/lvdund/docker-learning)
```php
$ docker pull mongo
$ docker run -d -p 2718:27017 -v ~/localPath:/data/db --name mongo-test mongo:latest
# 2718 - port of localhost
```

### Create database
```py
# tạo đối tượng MongoClient, sau đó chỉ định URL kết nối với địa chỉ IP chính xác và tên của cơ sở dữ liệu muốn tạo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
print(myclient.list_database_names())
```
* Trong MongoDB, cơ sở dữ liệu không được tạo cho đến khi nó có nội dung

### Creating a Collection (Table)
* Trong MongoDB, một collection không được tạo cho đến khi nó có nội dung
```py
import pymongo
myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['mydatabase']
mycol = mydb["customers"]
print(mydb.list_collection_names())
```

### Insert Document (Row)
1. Insert Into Collection
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)    
```
* Nếu bạn không chỉ định trường `_id` thì MongoDB sẽ thêm một trường cho bạn và gán một id duy nhất cho mỗi tài liệu.
* Trong ví dụ trên, không có trường `_id` nào được chỉ định, vì vậy MongoDB đã gán một `_id` duy nhất cho bản ghi (tài liệu).
2. Insert Multiple Documents:
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)
```
* Phương thức `insert_many()` trả về một đối tượng `InsertManyResult`, đối tượng này có thuộc tính, `insert_ids`, chứa id của tài liệu được chèn.
3. Insert Multiple Documents, with Specified IDs
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mylist = [
  { "_id": 1, "name": "John", "address": "Highway 37"},
  { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
  { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]
x = mycol.insert_many(mylist)
print(x.inserted_ids)
```

### Find
* sử dụng các phương thức find() và find_one() để tìm dữ liệu trong collection
1. Find One - trả về lần xuất hiện đầu tiên trong vùng chọn:
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

x = mycol.find_one()
print(x)
```
2. Find All
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find():
    print(x)
```
3. Find
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

for x in mycol.find({},{ "address": 0 }):
    print(x)
```

### Query with regex
* tìm những documents mà trường "address" bắt đầu bằng chữ "S", hãy sử dụng regular expression  {"$regex": "^S"}
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)
```

### Sort
```py
mydoc = mycol.find().sort("name")
mydoc = mycol.find().sort("name", -1)
```

### Delete Document
* `delete_one()` - Lưu ý: Nếu truy vấn tìm thấy nhiều tài liệu, thì chỉ lần xuất hiện đầu tiên bị xóa.
```py
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)
```
* `delete_many()`
```py
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")
```
* Delete All Documents in a Collection
```py
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")
```

### Drop Collection
* Phương thức drop() trả về true nếu bộ sưu tập được loại bỏ thành công và trả về false nếu bộ sưu tập không tồn tại.
```py
mycol.drop()
```

### Update
* can update a record, or document as it is called in MongoDB, by using the `update_one()` method
* Lưu ý: Nếu truy vấn tìm thấy nhiều bản ghi, thì chỉ bản ghi đầu tiên được cập nhật
```py
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)
```
* Update Many
```py
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }

x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")
```

### Limit
```py
# Limit the result to only return 5 documents:
myresult = mycol.find().limit(5)
for x in myresult:
    print(x)
```