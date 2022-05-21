# coding=utf-8
# 代码文件：ch09/ch9_4_4.py

class Account:
    interest_rate = 0.0568  # 类变量利率interest_rate

    def __init__(self, owner, amount):
        self.owner = owner      # 创建并初始化实例变量owner
        self.amount = amount    # 创建并初始化实例变量amount

account = Account('Tony', 800000.0)

print('账户名：{0}'.format(account.owner))
print('账户金额：{0}'.format(account.amount))
print('利率：{0}'.format(Account.interest_rate))
