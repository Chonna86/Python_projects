from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from urllib.parse import urlparse, parse_qs

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        query_params = parse_qs(parsed_path.query)

        
        value = float(query_params.get('value', [0])[0])
        from_unit = query_params.get('from', [''])[0]
        to_unit = query_params.get('to', [''])[0]
        measurement_type = query_params.get('type', [''])[0]
        system = query_params.get('system', [''])[0]

        
        converted_value = convert_value(value, from_unit, to_unit, measurement_type, system)

        
        if converted_value is None:
            self.send_response(422)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'error': 'Conversion not possible'}
        else:
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {'converted_value': converted_value}

        self.wfile.write(json.dumps(response).encode('utf-8'))

def convert_value(value, from_unit, to_unit, measurement_type, system):
    conversion_factors = {
        'length': {
            'm': 1.0,
            'ft': 3.28084,  # 1 meter = 3.28084 feet
        },
        'volume': {
            'm3': 1.0,
            'barrel': 6.28981,  # 1 cubic meter = 6.28981 barrels
        },
        'pressure': {
            'psi': 1.0,
            'bar': 0.0689476,  # 1 psi = 0.0689476 bar
        },
    }

    if system == 'SI':
        pass
    elif system == 'US':
        pass

    try:
        converted_value = value * conversion_factors[measurement_type][from_unit] * conversion_factors[measurement_type][to_unit]
        return converted_value
    except KeyError:
        return None  



def converted_value(value, from_unit, to_unit, measurement_type, system):
    if measurement_type == 'pressure':
        return converted_value(value, from_unit, to_unit, system)
    else:
        return None  


if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = HTTPServer(server_address, SimpleRequestHandler)
    print('Starting server...')
    httpd.serve_forever()