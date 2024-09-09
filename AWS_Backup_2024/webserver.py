from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # get the page
        path = self.path
        if path == '/':
            with open('temp-plot.html', 'rb') as page:
                self.wfile.write(page.read())
        elif path == '/about':
            with open('welcome.html', 'rb') as page:
                self.wfile.write(page.read())

while True:
	try:
		server = HTTPServer(('10.10.17.140', 9999), Server)
		server.serve_forever()
	except:
		print('error')
		server.server_close()


