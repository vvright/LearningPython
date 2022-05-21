# coding=utf-8
# 代码文件：ch15/ch15_4_6.py

import sqlite3

i_id = input('请输入要删除学生的【学号】：')

try:
# 1. 建立数据库连接
    con = sqlite3.connect('school_db.db')
# 2. 创建游标对象
    cursor = con.cursor()
# 3. 执行SQL删除操作
    sql = 'DELETE FROM student WHERE s_id=?'
    cursor.execute(sql, [i_id])

# 4. 提交数据库事务
    con.commit()
    print('删除数据成功。')
except sqlite3.Error as e:
    print('删除数据失败：{}'.format(e))
    # 4. 回滚数据库事务
    con.rollback()
finally:
# 5. 关闭游标
    if cursor:
        cursor.close()
# 6. 关闭数据连接
    if con:
        con.close()
