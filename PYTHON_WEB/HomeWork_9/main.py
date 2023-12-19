import subprocess
import json
from models import Author, Quote
from mongoengine import connect

# Запуск Scrapy для скрапінгу сайту та збереження даних у файли
subprocess.run(['scrapy', 'runspider', 'quotes_spider.py', '-o', 'quotes.json'])

# Завантаження даних з файлу quotes.json у MongoDB
username = 'alexandrchonka'
password = '7cxbWsKKJ0TQdY7A'
cluster_url = 'cluster0.cvqzmdk.mongodb.net'
database_name = 'mongo_demo'
connect(
    db=database_name,
    username=username,
    password=password,
    host=f'mongodb+srv://{username}:{password}@{cluster_url}/{database_name}?retryWrites=true&w=majority'
)
with open('quotes.json') as f:
    quotes_data = json.load(f)
    for quote_data in quotes_data:
        author = Author.objects(fullname=quote_data['author']).first()
        if not author:
            author = Author(fullname=quote_data['author'])
            author.save()

        quote = Quote(
            author=author,
            quote=quote_data['quote'],
            tags=quote_data['tags']
        )
        quote.save()

print("Data loaded into MongoDB.")