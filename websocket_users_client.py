import asyncio

import websockets


async def client():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send('Привет, сервер!')

        for _ in range(5):
            message = await websocket.recv()
            print(message)


asyncio.run(client())
