# coding=utf-8
# 代码文件：ch09/ch9_4_5.py

class Account:
    interest_rate = 0.0668  # 类变量利率

    def __init__(self, owner, amount):
        self.owner = owner  # 定义实例变量账户名
        self.amount = amount  # 定义实例变量账户金额

    # 类方法
    @classmethod
    def interest_by(cls, amt):
        # print(self.owner)
        return cls.interest_rate * amt

interest = Account.interest_by(12000.0)
print('计算利息：{0:.4f}'.format(interest))
