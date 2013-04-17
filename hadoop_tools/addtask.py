#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#    Copyright 2011 timger
#    +Author timger
#    +Gtalk&Email yishenggudou@gmail.com
#    +Msn yishenggudou@msn.cn
#    +Weibo @timger http://t.sina.com/zhanghaibo
#    +twitter @yishenggudou http://twitter.com/yishenggudou
#    Licensed under the MIT License, Version 2.0 (the "License");
from conf import conf
from tasks import Q
from Qtime import Qtime
from Qjobs import loadjob
from log import logger


def addtask(**kwargs):
    u"""
    host:
    port:
    ptime:201303042100
    jobname:'diaodu'
    """
    jobname = kwargs['jobname']
    kwargs.update(Qtime(kwargs['ptime']))
    print conf['jobs']
    jobs = [i for i in conf['jobs'] if i['name'] == jobname]
    print jobs
    for job in jobs:
        job['uri'] = job['uriformat'].format(**kwargs)
        job.update(kwargs)
        timeout = 30 * 3600
        logger.warning(' '.join([str(job), str(timeout)]))
        Q.enqueue(loadjob, kwargs=job.copy(), timeout=timeout)


if __name__ == "__main__":
    addtask(host='10.11.50.160',
            port=9188,
            ptime='201304040000',
            jobname='diaodu')
