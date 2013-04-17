#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
    Copyright 2011 timger
    +Author timger
    +Gtalk&Email yishenggudou@gmail.com
    +Msn yishenggudou@msn.cn
    +Weibo @timger http://t.sina.com/zhanghaibo
    +twitter @yishenggudou http://twitter.com/yishenggudou
    Licensed under the MIT License, Version 2.0 (the "License");
'''
"""
http://www.zeuux.com/blog/content/3938/
http://xgxzj.blog.163.com/blog/static/39537205201172810564038/
http://docs.celeryproject.org/en/master/userguide/tasks.html
"""
#from conf import conf
#from celery import Celery
#celery = Celery('tasks', broker=conf.CELERY_DB_URI)

#http://python-rq.org/
from redis import Redis
from rq import Queue
from rq import use_connection
from conf import conf
from  system import name as host_name

__all__ = ["Q", "GetQueue"]


default_redis = Redis(host=conf['redis']['host'], port=conf['redis']['port'])
use_connection(default_redis)

Q = Queue(name="rq_queue_{0}".format(host_name), connection=default_redis)


def GetQueue(name, host=None, port=None):
    Q = Queue(name=name, connection=default_redis)
    return Q


def GetAllQueues(host=None, port=None):
    return Q.all()

all_queues = GetAllQueues()


def GetWorksByQueueName(name, host=None, port=None):
    from rq.worker import Worker
    Q = GetQueue(name, host, port)
    w = Worker(Q, connection=default_redis)
    return w.all(connection=default_redis)

GetAllWorkers = GetWorksByQueueName


def removeWorker(wname, host=None, port=None):
    workers = GetAllWorkers('failed', host, port)
    worker = filter(lambda x: x.name == wname, workers)
    #connection=tasks.default_redis;y.register_death()
    [w.register_death() for w in worker]
    return worker

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        str_ = sys.argv[1]
    allqueue = GetAllQueues()
    print allqueue
    for queue in allqueue:
        print '-' * 100
        print "===:", queue.name, "=" * 3
        workers = GetWorksByQueueName(queue.name)
        for w in workers:
            print ">>>:", w.name
            if len(sys.argv) == 2:
                if str_ in w.name:
                    removeWorker(w.name)
