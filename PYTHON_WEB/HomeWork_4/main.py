from http.server import HTTPServer, BaseHTTPRequestHandler 
import urllib.parse

class HTTPHandler(BaseHTTPRequestHandler) :
    def do_GET(self) :
        p_url = urllib.parse.urlparse(self.path)
        if p_url.path == "/" :
            self.send_html_file('index.html')
        elif p-url == '/contact' :
            self.send_html_file('contact.html')
        else :
            
