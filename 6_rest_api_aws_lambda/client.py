import json
import requests

API_ROUTE = 'https://mrl0vy3w26.execute-api.sa-east-1.amazonaws.com/api/'

print("Iniciando calculadora...\n")

num1 = input('Insira o primeiro numero:\n')
num2 = input('Insira o segundo numero:\n')

op = input('Selecione a operacao: [soma] [sub] [mult] [div]\n')

result = json.loads(requests.get(f'{API_ROUTE}{op}/{num1}/{num2}').text)

print(f'\nResultado:\n{result}')

