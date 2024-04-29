from socket import *

my_host = '127.0.0.1'
my_port = 50009

sock_obj = socket(AF_INET, SOCK_STREAM)
sock_obj.bind((my_host, my_port))
sock_obj.listen(1)

print('Aguardando cliente...')
connection, address = sock_obj.accept()
print(f'Server conectado por: {address}')

while True:
    data = connection.recv(1024)
    if data.decode() == 'X':
        print('Conexao encerrada pelo cliente.')
        break
    print(f'Cliente enviou: \n{data.decode()}')
    
    resposta = input('Escreva uma resposta (digite "X" para encerrar):\n')
    connection.send(resposta.encode())

    if resposta == 'X':
        print("Encerrando...")
        break

connection.close()