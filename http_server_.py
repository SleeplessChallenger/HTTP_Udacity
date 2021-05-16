from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
# https://docs.python.org/3/library/http.server.html#http.server.SimpleHTTPRequestHandler.do_GET


class HandlerServer(BaseHTTPRequestHandler):

	def do_GET(self):
		# or we can put the whole form (see below)
		form = '''<!DOCTYPE html>
		  <title>Message Board</title>
		  <form method="POST" action="http://localhost:8000/">
		    <textarea name="message"></textarea>
		    <br>
		    <button type="submit">Post it!</button>
		  </form>
		'''


		self.send_response(200)

		self.send_header('Content-type', 'text/html; charset=utf-8')
		self.end_headers()

		self.wfile.write(form.encode())


		# (below) response body
		# self.wfile.write('HTTPはどうですか？'.encode())
		# wfile stands for writeable file


	def do_POST(self):
		weight = int(self.headers.get('content-length', 0))
		data = self.rfile.read(weight).decode()
		query = urllib.parse.parse_qs(data)
		msg = query.get('message', None)[0]
		if not msg:
			self.send_response(404)
			raise KeyError('No meesage in the request!')
		
		self.send_response(200)
		self.send_header('Content-type', 'text/plain; charset=utf-8')
		self.end_headers()
		self.wfile.write(msg.encode())


if __name__ == '__main__':
	server_address = ('', 8000)
	# 1. all addresses 2. port 8000
	server_obj = HTTPServer(server_address, HandlerServer)
	server_obj.serve_forever()
