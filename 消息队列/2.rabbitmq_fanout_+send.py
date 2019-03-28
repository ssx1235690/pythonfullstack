import pika
import sys

credentials = pika.PlainCredentials('mytest', 'mytest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.157.132', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout',durable=True)

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()