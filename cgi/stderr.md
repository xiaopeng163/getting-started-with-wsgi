# stderr

stderr信息可以写到apache的log里。 例如：

``` python
$ more /usr/lib/cgi-bin/stderr.py 
#!/usr/bin/env python
import sys
print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""

# test stderr
sys.stderr.write('this is log test for apache')
```

And you will see this log in `/var/log/apache2/error.log` when you run this script in browser.