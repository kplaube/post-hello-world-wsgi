from wsgiref.simple_server import make_server
from app import my_first_wsgi_app

HOST = 'localhost'
PORT = 8001

httpd = make_server(HOST, PORT, my_first_wsgi_app)
httpd.handle_request()
