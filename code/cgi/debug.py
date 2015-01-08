#!/usr/bin/env python
import cgitb
print "Content-Type: text/html"
print
try:
    print """\
<html>
<body>
<h2>Hello World! %s </h2>
</body>
</html>
""" % str(1/0)
except:
    cgitb.handler()