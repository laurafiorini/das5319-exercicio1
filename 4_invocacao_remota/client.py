import xmlrpc.client

s = xmlrpc.client.ServerProxy('http://localhost:8005')

num1 = input('1o num: ')
num2 = input('2o num: ')

print(f'Soma: {s.add(int(num1), int(num2))}')
print(f'Multiplicacao: {s.multiply(int(num1), int(num2))}')
print(f'Potencia: {s.power(int(num1), int(num2))}')
print(f'Divisao: {s.divide(int(num1), int(num2))}')
print(f'Subtracao: {s.subtract(int(num1), int(num2))}')