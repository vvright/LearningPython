# coding=utf-8
# 代码文件：ch15/ch15_4_3.py

import sqlite3

istr = input('请输入生日（yyyyMMdd）：')

try:
# 1. 建立数据库连接
    con = sqlite3.connect('school_db.db')
# 2. 创建游标对象
    cursor = con.cursor()
# 3. 执行SQL查询操作
    sql = 'SELECT s_id, s_name, s_sex, s_birthday FROM student WHERE s_birthday < ? '
    cursor.execute(sql, [istr])
# 4. 提取结果集
    result_set = cursor.fetchall()
    for row in result_set:
        print('学号：{0} - 姓名：{1} - 性别：{2} - 生日：{3}'
                        .format(row[0], row[1], row[2], row[3]))

except sqlite3.Error as e:
    print('数据查询发生错误：{}'.format(e))
finally:
# 5. 关闭游标
    if cursor:
        cursor.close()
# 6. 关闭数据连接
    if con:
        con.close()
