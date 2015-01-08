# 调试CGI

## 数据出错了怎么办？

假如我们有如下脚本：

``` python
$ more /usr/lib/cgi-bin/debug.py      
#!/usr/bin/env python
print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World! %s </h2>
</body>
</html>
"""% str(1/0)
```

命令行运行：

``` 
$ /usr/lib/cgi-bin/debug.py 
Content-Type: text/html

Traceback (most recent call last):
  File "/usr/lib/cgi-bin/debug.py", line 10, in <module>
    """% str(1/0)
ZeroDivisionError: integer division or modulo by zero
```

此时在浏览器里访问 `http://IP/cgi-bin/debug.py`， 没有数据返回。

我们可以通过apache的error log来发现错误：

```
$ more /var/log/apache2/error.log
[Wed Jan 07 18:38:45.978988 2015] [cgid:error] [pid 1419:tid 140246223935232] [client 192.168.157.1:57684] 
AH01265: attempt to invoke directory as script: /usr/lib/cgi-bin/
Traceback (most recent call last):
  File "/usr/lib/cgi-bin/debug.py", line 10, in <module>
    """% str(1/0)
ZeroDivisionError: integer division or modulo by zero
```

但是这对于开发调试非常不便，有没有更好的方法呢？


## cgitb — Traceback manager for CGI scripts

cgitb was originally designed to display extensive traceback information in HTML for CGI scripts.

To enable this feature, simply add this to the top of your CGI script:

``` python
import cgitb
cgitb.enable()
```

Then you can use `cgitb.enable` or `cgitb.handler`. Please see https://docs.python.org/2/library/cgitb.html for detail.

修改下我们的debug.py脚本：

``` python
$ more /usr/lib/cgi-bin/debug.py      
#!/usr/bin/env python
import cgitb
cgitb.enable()
print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World! %s </h2>
</body>
</html>
"""% str(1/0)
```

或者

``` python
$ more /usr/lib/cgi-bin/debug.py      
#!/usr/bin/env python
import cgitb
cgitb.enable()
print "Content-Type: text/html"
print
try:
    print """\
    <html>
    <body>
    <h2>Hello World! %s </h2>
    </body>
    </html>
    """% str(1/0)
except:
    cgitb.handler()
```

此时，debug信息会显示在浏览器上面，方便调试。

生产环境中出于安全的考虑，一般会关掉debug的功能。