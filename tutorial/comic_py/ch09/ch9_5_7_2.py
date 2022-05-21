# coding=utf-8
# 代码文件：ch09/ch9_5_3_2.py

class Dog:

    # 构造方法
    def __init__(self, name, age, sex='雌性'):
        self.name = name # 创建和初始化实例变量name
        self.__age = age # 创建和初始化私有实例变量__age

    # 实例方法
    def run(self):
        print("{}在跑...".format(self.name))

    @property
    def age(self):  # 替代get_age(self):
        return self.__age

    @age.setter
    def age(self, age):  # 替代set_age(self, age)
        self.__age = age

dog = Dog('球球', 2)
print('狗狗年龄：{}'.format(dog.age))
dog.age = 3 # dog.set_age(3)
print('修改后狗狗年龄：{}'.format(dog.age))
