from faker import Faker
from mongoengine import connect
import pika
from models import Contact

# Підключення до MongoDB
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

# Параметри RabbitMQ
rabbitmq_uri = 'amqp://guest:guest@localhost:5672/'
email_queue_name = 'email_contacts_queue'
sms_queue_name = 'sms_contacts_queue'

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
email_channel = connection.channel()
sms_channel = connection.channel()

# Оголошення черг для email та SMS
email_channel.queue_declare(queue=email_queue_name)
sms_channel.queue_declare(queue=sms_queue_name)

fake = Faker()

# Генерація та запис фейкових контактів у базу даних та черги RabbitMQ
for _ in range(10):  # 10 фейкових контактів
    contact = Contact(
        full_name=fake.name(),
        email=fake.email(),
        phone_number=fake.phone_number(),
        preferred_channel='email' if fake.boolean() else 'sms'
    )
    contact.save()

    # Отримання ObjectID новоствореного контакту
    contact_id = str(contact.id)

    # Відправка ObjectID у відповідну чергу RabbitMQ
    if contact.preferred_channel == 'email':
        email_channel.basic_publish(exchange='', routing_key=email_queue_name, body=contact_id)
    elif contact.preferred_channel == 'sms':
        sms_channel.basic_publish(exchange='', routing_key=sms_queue_name, body=contact_id)

print("Producer: Contacts generated and sent to the queues.")

# Закриття з'єднань
connection.close()