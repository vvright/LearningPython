# coding=utf-8
# 代码文件：ch15/ch15_4_5.py

import sqlite3

i_id = input('请输入【学号】：')
i_name = input('请输入【姓名】：')
i_sex = input('请输入【性别】（1表示男，0表示女）：')
i_birthday = input('请输入【生日】（yyyyMMdd）：')

try:
# 1. 建立数据库连接
    con = sqlite3.connect('school_db.db')
# 2. 创建游标对象
    cursor = con.cursor()
# 3. 执行SQL更新操作
    sql = 'UPDATE student SET s_name=?,s_sex=?,s_birthday=? WHERE s_id=?'
    cursor.execute(sql, [i_name, i_sex, i_birthday, i_id])

# 4. 提交数据库事务
    con.commit()
    print('更新数据成功。')
except sqlite3.Error as e:
    print('更新数据失败：{}'.format(e))
    # 4. 回滚数据库事务
    con.rollback()
finally:
# 5. 关闭游标
    if cursor:
        cursor.close()
# 6. 关闭数据连接
    if con:
        con.close()
