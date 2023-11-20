import pathlib
import urllib.parse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
import socket

BASE_DIR = pathlib.Path()

def send_data_via_socket(message):
    host = socket.gethostname()
    port = 3001

    client_socket = socket.socket()
    client_socket.connect((host, port))
  
    while message:
        sent_bytes = client_socket.send(message)
        message = message[sent_bytes:]  # Зчитати нові дані з повідомлення
        
    client_socket.close()



class HttpHandler(BaseHTTPRequestHandler) :

    def do_POST(self) :
        data = self.rfile.read(int(self.headers['Content-Length']))
        send_data_via_socket(data)
        self.send_response(200)
        self.send_header('Location', '/contact')
        self.end_headers()

    def do_GET(self) :
        pr_url = urllib.parse.urlparse(self.path)
        path = pr_url.path
        if path == '/' :
            self.index()
        elif path == '/message' :
            self.message()
        else :
            if path :
                file = BASE_DIR.joinpath(path[1:])
                if file.exists():
                    self.send_static(file)
            self.error_page()


    def index(self) :
        self.send_html_file('index.html')

    def message(self) :
        self.send_html_file('message.html')

    def error_page(self) :
        self.send_html_file('error.html',status=404)


    def send_html_file(self, filename, status=200):
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename, 'rb') as fd:
            self.wfile.write(fd.read())  

    
    def send_static(self, file):
        self.send_response(200)
        mt = mimetypes.guess_type(self.path)
        if mt:
            self.send_header('Content-type', mt[0])
        else:
            self.send_header('Content-type', 'text/plain')
        self.end_headers()
        with open(file, 'rb') as fd:  # ./assets/js/app.js
            self.wfile.write(fd.read())




def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()


if __name__ == '__main__':
    print('Start server...')
    run()