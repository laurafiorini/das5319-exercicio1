import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        num1 = input('Insira um numero: ')
        num2 = input('Insira outro numero: ')
        await websocket.send(str(int(num1)+int(num2)))
        await asyncio.sleep(random.random()*3)

start_server = websockets.serve(time, '127.0.0.1', 5678)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()