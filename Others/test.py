import aiohttp
import asyncio

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    url = 'https://www.google.com'
    data = await fetch_data(url)
    print(data)

# Запуск цикла событий asyncio и выполнение асинхронной программы
asyncio.run(main())