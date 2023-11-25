import aiohttp
import asyncio
import argparse
from datetime import datetime, timedelta
import json
from aiofile import AIOFile

async def fetch_exchange_rate(date, currencies=['EUR', 'USD']):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            exchange_rates = data.get('exchangeRate', [])
            result = {}
            for currency in currencies:
                for rate in exchange_rates:
                    if rate['currency'] == currency:
                        result[currency] = {
                            'sale': rate['saleRateNB'],
                            'purchase': rate['purchaseRateNB']
                        }
            return result

async def fetch_exchange_rates_for_last_days(num_of_days, currencies=['EUR', 'USD']):
    today = datetime.now()
    results = []
    for i in range(num_of_days):
        date = (today - timedelta(days=i)).strftime('%d.%m.%Y')
        exchange_rate = await fetch_exchange_rate(date, currencies)
        results.append({date: exchange_rate})
    return results

async def write_to_log(command):
    async with AIOFile('log.txt', 'a') as afp:
        await afp.write(f'{datetime.now()} - {command}\n')

async def main():
    parser = argparse.ArgumentParser(description='Отримання курсів валют з API ПриватБанку')
    parser.add_argument('days', type=int, help='Кількість днів для отримання курсів валют')
    args = parser.parse_args()

    exchange_rates = await fetch_exchange_rates_for_last_days(args.days)
    print(json.dumps(exchange_rates, indent=2, ensure_ascii=False))

    await write_to_log(f'exchange {args.days}')

if __name__ == '__main__':
    asyncio.run(main())