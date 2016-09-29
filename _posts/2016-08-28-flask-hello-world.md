---
layout: post
title:  "flask入门 --- hello world"
category: [back-end]
tags: [python, flask, web app server, linux]
---

Flask是一个使用 Python 编写的轻量级 Web 应用框架。相当于python版的轻量级的tomcat。  
因其简单，用来学习python是个很好选择。  

<!-- more -->

#### 一、搭环境

因为版本兼容性问题，强制安装0.7.9版本的sqlalchemy

```
pip install flask
pip install flask-login
pip install flask-openid
pip install flask-mail
pip install flask-sqlalchemy
pip install sqlalchemy-migrate
pip install flask-whooshalchemy
pip install flask-wtf
pip install flask-babel
pip install flup
pip uninstall sqlalchemy
pip install sqlalchemy==0.7.9
```

#### 二、代码创建目录结构

```
app                 #源代码
 |---static         #存放诸如图片、JS或者CSS之类的文件
 |---templates
tmp
```

#### 三、源代码

##### 1.`app/__init__.py`

```python
from flask import Flask
app = Flask(__name__)
from app import views
```

##### 2.`app/views.py`

```python
from app import app
@app.route('/')    # route() 装饰器用于把一个函数绑定到一个 URL 
@app.route('/index')
def index():
    return "Hello World!"
```

##### 3.`run.py`

```python
from app import app
app.run(debug = True)     # 打开调试模式，那么服务器会在修改应用之后自动重启，并且当应用出错时还会提供一个 有用的调试器
```

#### 四、运行及效果

```
chmod a+x run.py
python run.py
```

打开浏览器，输入127.0.0.1:5000，效果如图：  
![](/image/flask-hello-world.jpg)

---

参考文献：http://www.oschina.net/translate/the-flask-mega-tutorial-part-i-hello-world
