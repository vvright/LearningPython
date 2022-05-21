# coding=utf-8
# 代码文件：ch09/ch9_6_1.py

class Animal:

    def __init__(self, name):
        self.name = name  # 实例变量name

    def show_info(self):
        return "动物的名字：{0}".format(self.name)

    def move(self):
        print("动一动...")

class Cat(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age  # 实例变量age

cat = Cat('Tom', 2)
cat.move()
print(cat.show_info())
