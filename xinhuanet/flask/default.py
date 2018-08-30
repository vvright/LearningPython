# -*- coding:utf-8 -*-

from flask import Flask

app = Flask(__name__)


@app.route("/")
def default():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>课程主页</title>
        <style>
        .center {
            margin: auto;
            width: 25%;
            border: 3px solid #73AD21;
            padding: 10px;
        }
        
        img {
            display: block;
            margin: auto;
            width: 15%;
        }
        </style>
    </head>
    <body>
        <div>
            <img src="http://www.bjfu.edu.cn/images/head_l.png"/>
            <center>北京林业大学信息学院</center>
            <center>用Python快速开发企业应用</center>
        </div>
        <div style="text-align:center">
            <h1>我的第一个标题</h1>
            <p>我的第一个段落。</p>
            <a href="http://www.runoob.com">这是一个链接</a>
            <a href="http://www.w3school.com">这是一个链接</a>
            <a href="http://www.quanzhanketang.com">这是一个链接</a>
            <br/>
        </div>
        <div class="center">
              <p><b>注意: </b>使用 margin:auto 无法兼容 IE8, 除非 !DOCTYPE 已经声明。</p>
              <form action="">
              <table border="1">
                <tr>
                    <th>标题</th>
                    <th>Header 2</th>
                </tr>
                <tr>
                    <td>课程：</td>
                    <td><input name=""></td>
                </tr>
                <tr>
                    <td>row 2, cell 1</td>
                    <td><input name=""></td>
                </tr>
                 <tr>
                    <td><input type="submit" name="submit"></td>
                    <td><input type="button" name="cancel" value="取消"></td>
                </tr>
            </table>
            </form>
        </div>
    </body>
    </html>
    '''


#    '''
#    \<html\>
#        \<head\>default\<\/head\>
#    \<body\>
#        \<div\>
#            \<center\>北京林业大学信息学院\<\/center\>
#        \<\/div\>
#    \<\/body\>
#    \<\/html\>
#    '''


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='80')
