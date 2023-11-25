import asyncio
import websockets

async def exchange_command_client():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        command = input("Enter command: ")
        await websocket.send(command)
        response = await websocket.recv()
        print(response)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(exchange_command_client())