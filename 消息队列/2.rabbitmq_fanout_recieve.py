import pika

credentials = pika.PlainCredentials('mytest', 'mytest')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='192.168.157.132', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='logs',
                         exchange_type='fanout',durable=True)

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

'''
exchange 一直再广播你的队列收不到就收不到了
'''