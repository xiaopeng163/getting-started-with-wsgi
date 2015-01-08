# 准备工作

## 1. 安装Apache

安装不同的操作系统，使用相应的包管理工具进行安装。本文以`Ubuntu 14.10`为例。

```
$ sudo apt-get install apache2
```
    
启动apache服务，打开浏览器，确认出现Apache2 Ubuntu Default Page.


## 2. 配置Apache

### 1) Enable CGI mod

```
 $ ls /etc/apache2/mods-enabled/ | grep cgi
 $ sudo ln -s /etc/apache2/mods-available/cgid.load /etc/apache2/mods-enabled/
 $ sudo ln -s /etc/apache2/mods-available/cgid.conf /etc/apache2/mods-enabled/
 $ ls /etc/apache2/mods-enabled/ | grep cgi
 cgid.conf
 cgid.load
```

### 2) Configure site

```
$ more /etc/apache2/sites-available/000-default.conf 
...
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
<Directory "/usr/lib/cgi-bin/">
    AllowOverride None
    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
    Require all granted
</Directory>
```

### 3) Restart apache service

```
$ sudo service apache2 restart
```

