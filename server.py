import http.server
import ssl
import os

HOST = 'localhost'
PORT = 4443

server_address = (HOST, PORT)

# setup http server
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)

# setup socket
httpd.socket = ssl.wrap_socket(httpd.socket,
                               server_side=True,
                               keyfile='ca_key.pem',
                               certfile='ca_cert.pem',
                               ssl_version=ssl.PROTOCOL_TLS)

# change current directory to serve server out of
web_dir = os.path.join(os.path.dirname(__file__), 'www')
os.chdir(web_dir)

# start server
httpd.serve_forever()
