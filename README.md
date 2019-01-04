# CampusNetwork
login your account to ECNU campus network on a server OS (with no grahpic interface)
## 1.说明
* 由于校园网内的服务器无法直接访问外网，必须使用自己的学号登录后才可以。否则只能访问大部分linux源或者同是edu的网络（应该是有一个名单），可以使用apt/conda等
## 2.环境要求
* 现在一般都是python3  
* 使用没有图形界面的浏览器PhantomJS（已停止更新维护，使用最后发布的版本即可）一般`sudo apt install phantomjs`即可，如果另有问题（`phantomjs --version`无输出，需要手动设置无图形界面运行等）请自行百度，或：https://www.jianshu.com/p/0ea3739cf93e   
* 使用selenium模拟操作，最新版本不支持PhantomJS，所以要求3.8.0以前的版本。`pip install selenium==3.8.0`  
## 3.使用说明
`python ecnu.py`之后输入学号和密码  
 `python ecnu.py 123456(account) 123456(password)`  
 运行后会先判断是否已登录（尝试访问 www.baidu.com ），如果能打开则提示已登录，不再进行登录操作。  
