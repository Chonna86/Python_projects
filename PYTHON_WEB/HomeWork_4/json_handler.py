import json
import urllib.parse
from pathlib import Path
import socket
from datetime import datetime

BASE_DIR = Path()

def save_data_to_json(data):
    
    data_parse = urllib.parse.unquote_plus(data.decode())
    data_parse = {key: value for key, value in [el.split('=') for el in data_parse.split('&')]}

   
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    data_parse['timestamp'] = timestamp

    
    json_file_path = BASE_DIR.joinpath('D:\PythonProjects\MY_PYTHON_WAY\PYTHON_WEB\HomeWork_4\storage')

    
    with open(json_file_path, 'a', encoding='utf-8') as fd:
        json.dump({timestamp: data_parse}, fd, ensure_ascii=False)
        fd.write('\n')

def server():
    print('JSON HANDLER STARTED...')
    host = socket.gethostname()
    port = 5000

    with socket.socket() as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1000000)
        conn, address = server_socket.accept()

        print(f'Підключення від {address}')

        while True:
            data = conn.recv(100).decode()
            save_data_to_json(data)
            if not data:
                break

        conn.close()

