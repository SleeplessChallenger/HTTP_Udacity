from http.server import BaseHTTPRequestHandler, HTTPServer
# https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET

class HandlerServer(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)

		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.end_headers()
		# (above) must be called to complete an operation

		# (below) response body
		self.wfile.write(self.path[1:].encode())
		# wfile stands for writeable file


if __name__ == '__main__':
	server_address = ('', 8000)
	# 1. all addresses 2. port 8000
	server_obj = HTTPServer(server_address, HandlerServer)
	server_obj.serve_forever()
