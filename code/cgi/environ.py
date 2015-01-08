#!/usr/bin/env python
import os
print "Content-Type: text/html"
print
print "<html>\n"

for i in os.environ:
    print '<h3>%s => %s</h3>' % (i, os.environ[i])
print '</body>'
print '</html>'
