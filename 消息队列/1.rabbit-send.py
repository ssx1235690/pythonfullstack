import pika,time,threading
class send():
    def __init__(self,que_nam='hello'):
        # self.credentials = pika.PlainCredentials('mytest', 'mytest')
        self.credentials = pika.PlainCredentials('guest', 'guest')
        # self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.157.132',credentials=self.credentials))
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='11.11.136.141',credentials=self.credentials))
    def action(self,thread_num,msgj='ndyd 996'):
        que_nam='hello'
        print(thread_num)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=que_nam, durable=True)  # 只是指出队列持久化
        while True:
            try:
                self.channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body=msgj,
                                   properties=pika.BasicProperties(delivery_mode=2)
                                           )
            except BaseException as e:
                print(e)
            print(" [x] Sent %s %d" %(msgj,thread_num))
            time.sleep(3)
    def lll(self):
        li=[]
        for i in range(1,2):
            th=threading.Thread(target=self.action,args=(i,))
            th.start()
            li.append(th)
        # for i in li:
        #     i.join()
        # connection.close()
song=send('sdfl')
song.lll()
# song.action(1)