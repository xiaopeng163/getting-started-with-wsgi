# 准备工作

## 1. 安装Apache

安装不同的操作系统，使用相应的包管理工具进行安装。本文以`Ubuntu`为例。

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
ScriptAlias /cgi-bin/ /usr/lib/cgi-bin/
<Directory "/usr/lib/cgi-bin/">
    AllowOverride None
    Options +ExecCGI -MultiViews +SymLinksIfOwnerMatch
    Require all granted
</Directory>
```

### 3) Restart apache service

