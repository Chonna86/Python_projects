import pika
from mongoengine import connect
from models import Contact

# Підключення до MongoDB
connect('mongodb+srv://alexandrchonka:7cxbWsKKJ0TQdY7A@cluster0.cvqzmdk.mongodb.net/?retryWrites=true&w=majority')

# Параметри RabbitMQ
rabbitmq_uri = 'amqp://guest:guest@localhost:5672/'
queue_name = 'contacts_queue'

# Підключення до RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(rabbitmq_uri))
channel = connection.channel()
channel.queue_declare(queue=queue_name)

def send_email(contact):
    # Ваш код для відправлення email
    print(f"Sending email to {contact.full_name} at {contact.email}")

def send_sms(contact):
    # Ваш код для відправлення SMS
    print(f"Sending SMS to {contact.full_name} at {contact.phone_number}")

def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    contact = Contact.objects(id=contact_id).first()

    if contact:
        if contact.preferred_channel == 'email':
            send_email(contact)
        elif contact.preferred_channel == 'sms':
            send_sms(contact)

        # Оновлення логічного поля
        contact.message_sent = True
        contact.save()

    ch.basic_ack(delivery_tag=method.delivery_tag)

# Призначення функції обробки повідомлень для черги
channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Consumer: Waiting for messages. To exit press CTRL+C")
channel.start_consuming()