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

def handle_request(client_socket):
    data = client_socket.recv(1024).decode()
    request = data.split()
    request_type = request[0]
    request_msg = request[1]
    
