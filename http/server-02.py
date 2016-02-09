import SimpleHTTPServer
import SocketServer
# ---------------------------------------------------
class GetHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        print self.headers
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
    def do_POST(self):
        print self.headers
        SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)
# ---------------------------------------------------
PORT    = 8000
Handler = GetHandler
httpd   = SocketServer.TCPServer(("", PORT), Handler)
# ---------------------------------------------------
print "serving at port", PORT
httpd.serve_forever()