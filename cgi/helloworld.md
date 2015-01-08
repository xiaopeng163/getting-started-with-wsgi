# Hello World！

## CGI Script

Put this python script into cgi-bin directory, and make it executable(`chmod 755`)

``` python
$ more /usr/lib/cgi-bin/helloworld.py 
#!/usr/bin/env python
print "Content-Type: text/html"
print
print """\
<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
"""
```

Makesure you can run the script directly like this:

``` python
$ /usr/lib/cgi-bin/helloworld.py      
Content-Type: text/html

<html>
<body>
<h2>Hello World!</h2>
</body>
</html>
```

## Test it within Browser

Open browser with `http://IP/cgi-bin/helloworld.py`, and you will see `Hello World!`.
