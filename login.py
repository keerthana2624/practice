import socket
import psycopg2

host = 'localhost'
port = 8080
server_socket = socket.socket()
server_socket.bind((host, port))
server_socket.listen()

print(f'The server is listening on http://{host}:{port}')

dbname = "postgres"
user = "postgres"
password = "Rakesh062"
host = "localhost"
port = "5432"

connection = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cursor = connection.cursor()


def render_page(page_name):
    with open(f'{page_name}.html', 'r') as file:
        html_content = file.read()
    headers = "HTTP/1.1 200 OK\r\n"
    headers += "Content-Type: text/html\r\n\r\n"
    headers += html_content
    return headers


def handle_request(client_socket):
    data = client_socket.recv(1024).decode()
    request = data.split()
    request_type = request[0]
    request_msg = request[1]
    
    if request_msg == '/' and request_type == 'GET':
    response = render_page('login')
    client_socket.send(response.encode())



while True:
    client_socket, client_address = server_socket.accept()
    handle_request(client_socket)
