# Environ

可以通过os.environ获取服务器的环境信息：

``` python
$ more /usr/lib/cgi-bin/environ.py 
#!/usr/bin/env python
import os
print "Content-Type: text/html"
print
print "<html>\n"

for i in os.environ:
    print '<h3>%s => %s</h3>'%(i,os.environ[i])
print '</body>'
print '</html>'
```

浏览器输入 `http://IP/cgi-bin/environ.py`， 可以得到类似输出：

```
CONTEXT_DOCUMENT_ROOT => /usr/lib/cgi-bin/
SERVER_SOFTWARE => Apache/2.4.10 (Ubuntu)
CONTEXT_PREFIX => /cgi-bin/
SERVER_SIGNATURE =>
Apache/2.4.10 (Ubuntu) Server at 192.168.157.137 Port 80
REQUEST_METHOD => GET
SERVER_PROTOCOL => HTTP/1.1
QUERY_STRING =>
PATH => /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HTTP_USER_AGENT => Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36
HTTP_CONNECTION => keep-alive
SERVER_NAME => 192.168.157.137
REMOTE_PORT => 57977
SERVER_PORT => 80
SERVER_ADDR => 192.168.157.137
DOCUMENT_ROOT => /var/www/html
SCRIPT_FILENAME => /usr/lib/cgi-bin/environ.py
SERVER_ADMIN => webmaster@localhost
HTTP_HOST => 192.168.157.137
SCRIPT_NAME => /cgi-bin/environ.py
REQUEST_URI => /cgi-bin/environ.py
HTTP_ACCEPT => text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
GATEWAY_INTERFACE => CGI/1.1
REMOTE_ADDR => 192.168.157.1
HTTP_ACCEPT_LANGUAGE => en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2
REQUEST_SCHEME => http
HTTP_ACCEPT_ENCODING => gzip, deflate, sdch
```

其中一些`HTTP_`开头的，还有类似`REQUEST_METHOD`,`QUERY_STRING`等对于处理HTTP请求很有帮助。 接下来的章节会详细讲解。