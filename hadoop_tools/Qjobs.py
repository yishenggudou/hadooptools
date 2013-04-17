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

from log import logger
from tasks import Q
from parsejob import parsejob

def loadjob(**kwargs):
    from urllib import urlretrieve
    import os
    kwargs = kwargs.get('kwargs') or kwargs
    tmppath = os.path.join(kwargs['tmpdir'],kwargs['uri'].strip('http://').replace('/','_'))
    urlretrieve(kwargs['uri'], tmppath)
    logger.warning('{0}=>{1}'.format(kwargs['uri'],tmppath))
    timeout = 120*3600
    kwargs.update({'path':tmppath})
    Q.enqueue(parsejob, kwargs=kwargs, timeout=timeout)
    
