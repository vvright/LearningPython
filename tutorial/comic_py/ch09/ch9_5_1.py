# coding=utf-8
# 代码文件：ch09/ch9_5_1.py

class Account:
    __interest_rate = 0.0568  # 类变量利率__interest_rate

    def __init__(self, owner, amount):
        self.owner = owner      # 创建并初始化公有实例变量owner
        self.__amount = amount  # 创建并初始化私有实例变量__amount


    def desc(self):
        print("{0} 金额：{1} 利率：{2}。".format(self.owner,
                                        self.__amount,
                                    Account.__interest_rate))


account = Account('Tony', 800000.0)
account.desc()

print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.__amount)) # 错误发生
print('利率：{0}'.format(Account.__interest_rate)) # 错误发生
