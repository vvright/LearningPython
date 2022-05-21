# coding=utf-8
# 代码文件：ch09/ch9_6_2.py

class Horse:
    def __init__(self, name):
        self.name = name  # 实例变量name

    def show_info(self):
        return "马的名字：{0}".format(self.name)

    def run(self):
        print("马跑...")

class Donkey:
    def __init__(self, name):
        self.name = name  # 实例变量name

    def show_info(self):
        return "驴的名字：{0}".format(self.name)

    def run(self):
        print("驴跑...")

    def roll(self):
        print("驴打滚...")

class Mule(Horse, Donkey):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age  # 实例变量age

m = Mule('骡宝莉', 1)
m.run() # 继承父类Horse方法
m.roll() # 继承父类Donkey方法
print(m.show_info()) # 继承父类Horse方法
