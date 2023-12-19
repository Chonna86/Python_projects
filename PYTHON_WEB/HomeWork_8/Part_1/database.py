import json
from mongoengine import connect
from models import Author, Quote

def connect_to_database(uri):
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

def load_data_into_database():
    with open('authors.json', 'r') as file:
        authors_data = json.load(file)

    with open('quotes.json', 'r') as file:
        quotes_data = json.load(file)

    for author_data in authors_data:
        author = Author(**author_data)
        author.save()

    for quote_data in quotes_data:
        author_name = quote_data['author']
        author = Author.objects(fullname=author_name).first()
        if author:
            quote_data['author'] = author
            quote = Quote(**quote_data)
            quote.save()











