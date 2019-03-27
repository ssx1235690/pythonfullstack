import pika

class recieve():
    def __init__(self,msg='ndyd 996',que_nam='hello'):
        self.credentials = pika.PlainCredentials('mytest', 'mytest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.157.132',credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=que_nam)

    def callback(self,ch, method, properties, body):
        print(" [x] Received %r" % body)

    def start(self):
        self.channel.basic_consume(self.callback,
                          queue='hello',
                          no_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
song=recieve()
song.start()