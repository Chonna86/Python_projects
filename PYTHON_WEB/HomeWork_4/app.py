import pathlib
import urllib.parse
import mimetypes
from http.server import HTTPServer, BaseHTTPRequestHandler
from threading import Thread
import socket
from json_handler import server as json_socket_server


BASE_DIR = pathlib.Path()

def send_data_via_socket(message):
    host = socket.gethostname()
    port = 3000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    try:
        while message:
            sent_bytes = client_socket.send(message)
            message = message[sent_bytes:]  
    except Exception as e:
        print(f"Error sending data via socket: {e}")
    finally:
        client_socket.close()

class HttpHandler(BaseHTTPRequestHandler):
    
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            data = self.rfile.read(content_length)
            send_data_via_socket(data)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Data received successfully.')
        except Exception as e:
            print(f"Error processing POST request: {e}")
            self.send_error(500, 'Internal Server Error')

    def do_GET(self):
        pr_url = urllib.parse.urlparse(self.path)
        path = pr_url.path
        if path == '/':
            self.index()
        elif path == '/message':
            self.message()
        else:
            if path:
                file = BASE_DIR.joinpath(path[1:])
                if file.exists():
                    self.send_static(file)
            self.error_page()

    def index(self):
        self.send_html_file('index.html')

    def message(self):
        self.send_html_file('message.html')

    def error_page(self):
        self.send_html_file('error.html', status=404)

    def send_html_file(self, filename, status=200):
        try:
            self.send_response(status)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open(filename, 'rb') as fd:
                self.wfile.write(fd.read())
        except FileNotFoundError:
            self.send_error(404, f'File not found: {filename}')
        except Exception as e:
            self.send_error(500, f'Internal Server Error: {str(e)}')

    def send_static(self, file):
        try:
            self.send_response(200)
            mt = mimetypes.guess_type(self.path)
            if mt:
                self.send_header('Content-type', mt[0])
            else:
                self.send_header('Content-type', 'text/plain')
            self.end_headers()
            with open(file, 'rb') as fd:
                self.wfile.write(fd.read())
        except Exception as e:
            self.send_error(500, f'Internal Server Error: {str(e)}')

def run(server_class=HTTPServer, handler_class=HttpHandler):
    server_address = ('', 3000)
    http = server_class(server_address, handler_class)
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        http.server_close()

if __name__ == '__main__':
    json_handler = Thread(target=json_socket_server)
    json_handler.start()
    print('Start server...')
    run()