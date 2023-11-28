from aiohttp import web
from aiohttp import ClientSession
import asyncio

import json

TOKEN = '6474731612:AAHweJKdEuGquYAEmsedrXAFLlnFlC5Zggs'
API_URL = f"https://api.telegram.org/bot{TOKEN}"

async def get_updates():
    async with ClientSession() as session:  
        async with session.get(f'{API_URL}/getUpdates') as response:
            updates = await response.json()
            await broadcast(updates)

async def send_message(chat_id: str, message) :
    async with ClientSession() as session:  
        async with session.get(f'{API_URL}/sendMessage?chat_id={chat_id}&text={message}') as response:
            updates = await response.json()
            print(updates)

async def broadcast(updates: dict) :
    for obj in updates.get('result',[]) :
        chat = obj.get('message').get('chat')
        chat_id = chat.get('id')
        message = 'Hello my Friend!'
        await send_message(chat_id=chat_id, message=message)



asyncio.run(get_updates())
