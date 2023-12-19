import json
from mongoengine import connect
from models import Author, Quote

def connect_to_database(uri):
    uri = 'mongodb+srv://alexandrchonka:7cxbWsKKJ0TQdY7A@cluster0.cvqzmdk.mongodb.net/?retryWrites=true&w=majority'
    connect(host=uri)

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











