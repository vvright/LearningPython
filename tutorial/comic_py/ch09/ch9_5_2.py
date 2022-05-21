# coding=utf-8
# 代码文件：ch09/ch9_5_2.py

class Account:
    __interest_rate = 0.0568  # 类变量利率__interest_rate

    def __init__(self, owner, amount):
        self.owner = owner      # 创建并初始化公有实例变量owner
        self.__amount = amount  # 创建并初始化私有实例变量__amount

    def __get_info(self):
        return "{0} 金额：{1} 利率：{2}。".format(self.owner,
                                        self.__amount,
                                    Account.__interest_rate)

    def desc(self):
        print(self.__get_info())
    

account = Account('Tony', 800000.0)
account.desc()
account.__get_info() # 发生错误 

