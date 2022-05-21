# coding=utf-8
# 代码文件：ch09/ch9_7_1.py

class Animal:
    def speak(self):
        print('动物叫，但不知道是哪种动物叫！')

class Dog(Animal):
    def speak(self):
        print('小狗：旺旺叫...')

class Cat(Animal):
    def speak(self):
        print('小猫：喵喵叫...')

an1 = Dog()
an2 = Cat()
an1.speak()
an2.speak()
