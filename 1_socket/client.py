from socket import *

server_host = '127.0.0.1'
server_port = 50009

sock_obj = socket(AF_INET, SOCK_STREAM)
sock_obj.connect((server_host, server_port))

while True:
    msg = input('Escreva uma mensagem (digite "X" para encerrar):\n')
    sock_obj.send(msg.encode())
    if msg == "X":
        print("Encerrando...")
        break

    data = sock_obj.recv(1024)
    if data.decode() == 'X':
        print('Conexao encerrada pelo servidor.')
        break
    print(f'Servidor enviou:\n{data.decode()}')

sock_obj.close()