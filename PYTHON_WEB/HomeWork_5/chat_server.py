import asyncio
import websockets
import json
from main import fetch_exchange_rates_for_last_days, write_to_log

async def exchange_command_handler(websocket, path):
    async for command in websocket:
        if command.startswith('exchange'):
            try:
                _, num_of_days_str = command.split()
                num_of_days = int(num_of_days_str)
                exchange_rates = await fetch_exchange_rates_for_last_days(num_of_days)
                response = json.dumps(exchange_rates, indent=2)
            except ValueError:
                response = 'Invalid command. Usage: exchange <num_of_days>'
        else:
            response = 'Unknown command'

        await websocket.send(response)
        await write_to_log(command)

if __name__ == '__main__':
    start_server = websockets.serve(exchange_command_handler, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()