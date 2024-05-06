import socket
import time

port = 6001
host = 'localhost'

s = socket.socket()
s.bind((host, port))
s.listen(1)

while True:
    conn, addr = s.accept()
    print(f'Conectado por: {addr}')

    filename='FT_teste.xlsx'

    print(f'60 segundos restantes para editar o arquivo `{filename}`')

    time.sleep(30)

    print(f'30 segundos...')

    time.sleep(20)

    print(f'10 segundos...')

    time.sleep(10)

    print('Enviando arquivo...')

    f = open(filename, 'rb')
    l = f.read(1024*16)

    while(l):
        conn.send(l)
        l = f.read(1024*16)

    f.close()

    print('Envio completo')
    conn.close()
    print('Conexao fechada')
    break
    