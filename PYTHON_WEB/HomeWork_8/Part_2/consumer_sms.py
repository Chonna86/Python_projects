import pika
from mongoengine import connect
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
sms_queue_name = 'sms_contacts_queue'

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
channel = connection.channel()
channel.queue_declare(queue=sms_queue_name)

def send_sms(contact):
    # Ваш код для відправлення SMS
    print(f"Sending SMS to {contact.full_name} at {contact.phone_number}")

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects(id=contact_id).first()

    if contact:
        send_sms(contact)

        # Оновлення логічного поля
        contact.message_sent = True
        contact.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Призначення функції обробки повідомлень для черги
channel.basic_consume(queue=sms_queue_name, on_message_callback=callback)

print("Consumer (SMS): Waiting for messages. To exit press CTRL+C")
channel.start_consuming()