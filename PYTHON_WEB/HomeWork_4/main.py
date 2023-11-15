from http.server import HTTPServer, BaseHTTPRequestHandler 
import urllib.parse

class HTTPHandler(BaseHTTPRequestHandler) :
    def do_GET(self) :
        p_url = urllib.parse.urlparse(self.path)
        if p_url.path == "/" :
            self.send_html_file('index.html')
        elif p_url == '/contact' :
            self.send_html_file('contact.html')
        else :
            self.send_html_file('error.html', 404)

    def send_html_file(self, filename, status = 200) :
        self.send_response(status)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        with open(filename,'rb') as fh :
            self.wfile.write(fh.read())

def run(class_server = HTTPServer, class_handler = HTTPHandler) :
    server_address = ('', 8000)
    http = class_server(server_address, class_handler )
    try :
        http.serve_forever()
    except KeyboardInterrupt :
        http.server_close()

if __name__ == '__main__' :
    run()

        
