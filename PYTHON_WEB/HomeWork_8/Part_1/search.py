import re
import redis
from mongoengine import connect
from models import Author, Quote

# З'єднання з базою даних MongoDB Atlas
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

# Підключення до Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

def search_quotes(query):
    if query.startswith('name:'):
        # Пошук за ім'ям автора
        author_name = query[len('name:'):].strip()
        cached_result = redis_client.get(f'name:{author_name}')
        if cached_result:
            return cached_result
        else:
            author = Author.objects(fullname__istartswith=author_name).first()
            if author:
                quotes = Quote.objects(author=author)
                result = '\n'.join([f'{quote.quote} - {quote.tags}' for quote in quotes])
                redis_client.set(f'name:{author_name}', result)
                return result
            else:
                return 'No matching author found.'

    elif query.startswith('tag:'):
        # Пошук за тегом
        tag = query[len('tag:'):].strip()
        cached_result = redis_client.get(f'tag:{tag}')
        if cached_result:
            return cached_result
        else:
            quotes = Quote.objects(tags__icontains=tag)
            result = '\n'.join([f'{quote.quote} - {quote.tags}' for quote in quotes])
            redis_client.set(f'tag:{tag}', result)
            return result

    elif query.startswith('tags:'):
        # Пошук за набором тегів
        tags = query[len('tags:'):].strip().split(',')
        cached_result = redis_client.get(f'tags:{",".join(tags)}')
        if cached_result:
            return cached_result
        else:
            quotes = Quote.objects(tags__in=tags)
            result = '\n'.join([f'{quote.quote} - {quote.tags}' for quote in quotes])
            redis_client.set(f'tags:{",".join(tags)}', result)
            return result

    elif query == 'exit':
        exit()
    else:
        return 'Invalid command'
