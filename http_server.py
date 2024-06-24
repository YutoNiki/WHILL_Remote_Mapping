# http_server.py
import http.server
import socketserver
import os

PORT = 8000

class SimpleHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(os.path.join('static', 'index.html'), 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_error(404)
            self.end_headers()

if __name__ == "__main__":
    handler = SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", PORT), handler)
    print(f"Serving HTTP on port {PORT}")
    httpd.serve_forever()

