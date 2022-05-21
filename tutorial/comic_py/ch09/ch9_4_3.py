# coding=utf-8
# 代码文件：ch09/ch9_4_3.py

class Dog:
    # 构造方法
    def __init__(self, name, age, sex='雌性'):
        self.name = name # 创建和初始化实例变量name
        self.age = age   # 创建和初始化实例变量age
        self.sex = sex   # 创建和初始化实例变量sex

    # 实例方法
    def run(self):
        print("{}在跑...".format(self.name))

    # 实例方法
    def speak(self, sound):
        print('{}在叫，"{}"!'.format(self.name, sound))


dog = Dog('球球', 2)
dog.run()
dog.speak('旺 旺 旺')