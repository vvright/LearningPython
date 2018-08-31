# -*- coding:utf-8 -*-

from flask import Flask, request, render_template
app = Flask(__name__)


@app.route("/")
def default():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>博客主页</title>
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
              <form action="/login" method="post">
              <table border="1">
                <tr>
                    <th>标题</th>
                    <th>内容</th>
                </tr>
                <tr>
                    <td>用户：</td>
                    <td><input type="text" name="username"></td>
                </tr>
                <tr>
                    <td>密码：</td>
                    <td><input type="password" name="password"></td>
                </tr>
                 <tr>
                    <td>
                    <input type="submit" name="submit">
                    <input type="button" name="cancel" value="取消" onclick="#">
                    </td>
                </tr>
            </table>
            </form>
        </div>
        <div class="center">
            <a href="/articles">查看所有文章</a>
        </div>
    </body>
    </html>
    '''


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] == u'北京林业大学':
            if request.form['password'] == u'123456':
                return u"欢饮您" + request.form['username']
            else:
                return request.form['username'] + u'密码不正确'
        else:
            return u'该用户不存在：'+ request.form['username']
    else:
        return u'HTTP方法不正确'


@app.route('/articles')
def show_articles():
    return render_template('articles.html')


@app.route('/register')
def register():
    return render_template('register.html')

#    '''

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port='80')
