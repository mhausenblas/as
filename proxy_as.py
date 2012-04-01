from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, urllib, urllib, string, cgi, time
from os import curdir, sep

class ProxyASHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		parsed_path = urlparse.urlparse(self.path)
		target_url = parsed_path.path[1:]
		if self.path == '/': self.serve_content('index.html')
		if self.path.startswith("/r/"): self.serve_URL(target_url[2:], parsed_path.query)
		if self.path.endswith(".html"): self.serve_content(target_url, media_type='text/html')
		if self.path.endswith(".js"): self.serve_content(target_url, media_type='application/javascript')
		if self.path.endswith(".css"): self.serve_content(target_url, media_type='text/css')
		return
		
	def serve_content(self, p, media_type='text/html'):
		try:
			f = open(curdir + sep + p)
			self.send_response(200)
			self.send_header('Content-type', media_type)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()
			return
		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)
		
	def serve_URL(self, turl, q):
		print('GETing %s' %turl)
		self.send_response(200)
		self.send_header('Content-type', 'application/json')
		self.end_headers()
		data = urllib.urlopen(turl + '?' + q)
		self.wfile.write(data.read())

if __name__ == '__main__':
	from BaseHTTPServer import HTTPServer
	server = HTTPServer(('localhost', 6969), ProxyASHandler)
	print 'Starting AS server ... use {Ctrl+C} to shut-down ...'
	server.serve_forever()