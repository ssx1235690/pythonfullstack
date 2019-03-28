import pika,time,threading
class send():
    def __init__(self,que_nam='hello'):
        self.credentials = pika.PlainCredentials('mytest', 'mytest')
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.157.132',credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=que_nam,durable=True) #只是指出队列持久化
    def action(self,msgj='ndyd 996'):
        while True:
            self.channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=msgj,
                               properties=pika.BasicProperties(delivery_mode=2)
                                       )
            time.sleep(0.5)
            print(" [x] Sent %s" %msgj)
    def lll(self):
        li=[]
        for i in range(1,1000):
            th=threading.Thread(target=self.action())
            th.start()
            li.append(th)
        # for i in li:
        #     i.join()
        ( i.join() for i in li)
        # connection.close()
song=send()
song.lll()