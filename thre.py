# -*- coding:utf-8 -*-

#多线程 条件同步
#GLI 全局解释器锁
#一个python进程 一次只能进行一个进程

import time

'''for i in range(10):
    time.sleep(i)
    print(i)'''

import requests

import threading

'''print(requests.get('http://www.baidu.com/pn=1').text)

start_url = 'https://www.bilibili.com'
def get_response(url):
    response = requests.get(url).content
    print(response)

#get_response(start_url.format(1))

thread_list = []

for i in range(1,10):
    url = start_url.format(i)
    t = threading.Thread(target = get_response,args=(url,))
    thread_list.append(t)

for th in thread_list:
    th.start()'''

import random

condition = threading.Condition()

#生产者 消费者
class Producer(threading.Thread):
    '''
    向一个list里面添加一个随机数
    '''
    def __init__(self,integers,condition):
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            integer = random.randint(0,256)
            self.condition.acquire() #获取锁
            print('生产者{}正在获取锁'.format(self.name))
            self.integers.append(integer)
            print('生产者{}生产了一个随机数{},加入到了队列'.format(self.name,integer))
            print('生产者{}准备唤醒消费者',format(self.name))
            self.condition.notify()
            print('生产者{}释放锁'.format(self.name))
            self.condition.release()
            time.sleep(1)

class Consumer(threading.Thread):

    def __init__(self,integers,condition):
        threading.Thread.__init__(self)
        self.integers = integers
        self.condition = condition

    def run(self):
        while True:
            self.condition.acquire()
            print('消费者{}正在获取锁'.format(self.name))

            while True:
                if self.integers:#判断list里是否有数据
                    integer = self.integers.pop()
                    print('消费者{}消费了一个随机数{}'.format(self.name,integer))
                    break
                print('消费者{}准备消费，但没有数据，在等待生成'.format(self.name))
                self.condition.wait() #等待生产者生产数据，并且释放锁

            print('消费者{}释放锁'.format(self.name))
            self.condition.release()
            time.sleep(1)

def main():
    integers = []
    condition = threading.Condition()
    p1 = Producer(integers,condition)
    c1 = Consumer(integers,condition)
    p1.start()#启动
    c1.start()

    p1.join()#等待线程执行完毕
    c1.join()

if __name__ == '__main__':
    main()
