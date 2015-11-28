from flask import Flask, Markup
app = Flask(__name__)
#---------------------------------------------

print Markup('<strong>Hello %s!</strong>') % '<blink>hacker</blink>'
print "---"
print Markup.escape('<blink>hacker</blink>')
print "---"
print Markup('<em>Marked up</em> &raquo; HTML').striptags()
#---------------------------------------------
