### Variable
```py
# input
a = input()             # a is string
b = int(input())        # b is int

# print
print("a = {0} \n b = {1}".format(a, b))
print("In ra 10 lan" *10)
# print inline
print("...", end = " ")
```

### Python Collections (Arrays)
1. `List`: là một bộ sưu tập được sắp xếp và thay đổi. Cho phép các thành viên trùng lặp.
    * được sử dụng để lưu trữ nhiều mục trong một biến duy nhất
    * được sắp xếp theo thứ tự, có thể thay đổi và cho phép các giá trị trùng lặp
    * can change, add, and remove items in a list after it has been created
    * can have items with the same value
    * can contain different data types
2. `Tuple`: là một tập hợp được sắp xếp theo thứ tự và không thể thay đổi. Cho phép các thành viên trùng lặp.
    * được sắp xếp theo thứ tự và không thể thay đổi và cho phép các giá trị trùng lặp
    * không thể thay đổi, thêm hoặc xóa các mục sau khi bộ đã được tạo
3. `Set`: là một bộ sưu tập không có thứ tự, không thể thay đổi* và không được lập chỉ mục. Không có thành viên trùng lặp.
    * không có thứ tự, không thể thay đổi*, không được lập chỉ mục và không cho phép các giá trị trùng lặp
    * are unchangeable, but you can remove and/or add items whenever you like
    * item có thể xuất hiện theo thứ tự khác nhau mỗi khi bạn sử dụng chúng và không thể được tham chiếu bằng index/key
4. `Dictionary`: là một bộ sưu tập được đặt hàng** và có thể thay đổi. Không có thành viên trùng lặp.
    *  sử dụng để lưu trữ các giá trị dữ liệu trong key:value
    *  được sắp xếp theo thứ tự*, có thể thay đổi và không cho phép trùng lặp
    *  có thể thay đổi, nghĩa là chúng ta có thể thay đổi, thêm hoặc bớt các mục sau khi tạo từ điển
```py
# list
list1 = [1, 2, 3, 4]    # append - pop - insert - sort
list2 = ["abc", 34, True, 40, "male"]
# tuple
tuple1 = ("apple",)     # 1 item bắt buộc phải có dấu ,
tuple2 = ("apple", "banana", "cherry")
# set
set1 = {"apple", "banana", "cherry", "apple"}
set2 = {"abc", 34, True, 40, "male"}
# dict
dict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
```
### Error
```py
try:
    ...
except:
    ...
```

### Command
```python
# if else
if true or true:
    ...
elif true and true:
    ...
elif not true:
    ...
else:
    ...         # vs None: is None || is not None

# break continue

# for
for i in range(0, 5):       # i : 0, 1, 2, 3, 4
    ...
for i in range(5):
    ...
for i in range(0, 5, 2):    # i : 0, 2, 4
    ...

# While
while true:
    ...
```

### Function
```py
def func1():
    ...
```

### File I/O
```py
file = open("file.txt", "w")
/*
 * "w": write
 * "r": read
 * "a": append
 */
file.close()                        # have to close

with open("file.txt", "w") as f:    # no need to close
    f.write("lvd\n")
```

### Class
```py
class Student:
    def __init__(self):
        self.name = None
        self.age = None
    def grade(self):
        return (self.age - 7)
s1.Student()
s1.age = 10
print(s1.grade())
```

### Lambda function
* là một hàm ẩn danh nhỏ
* Syntax    `lambda arguments : expression`
* expression được thực thi và kết quả được trả về
```py
# ex1
x = lambda a, b : a * b
print(x(5, 6))              # -> 30 (=5*6)
# ex2
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))        # 22
```

### Class/Object
```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)
print(p1)
```

### Inheritance
```py
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()
```

### Iterators

### Scope

### Modules
```py
import json
import mymodule as mx

```

### Json
| Python | JSON   |
|--------|--------|
| dict   | Object |
| list   | Array  |
| tuple  | Array  |
| str    | String |
| int    | Number |
| float  | Number |
| True   | true   |
| False  | false  |
| None   | null   |
```py
import json
# ex1
x1 =  '{ "name":"John", "age":30, "city":"New York"}'    # x is json
y1 = json.loads(x)                                       # y is dictionary
# ex2
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
y = json.dumps(x)           # y is json string
                           
```