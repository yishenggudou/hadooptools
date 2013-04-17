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
import gzip
import imp
import os
from up2hadoop_with_queue import up2hadoop


def parsejob(**kwargs):
    kwargs = kwargs.get('kwargs') or kwargs
    print kwargs
    if kwargs.get('filetype') == 'gz':
        print 'gz file'
        f = gzip.open(kwargs['path'])
    else:
        f = open(kwargs['path'])
    fp, pathname, description = imp.find_module(kwargs['parsefile'],
                                                [kwargs['moduledir']])
    parse_module = imp.load_module(kwargs['parsefile'],
                                   fp,
                                   pathname,
                                   description)
    #Qparse_fun = getattr(parse_module, kwargs['parsefunction'])
    Qparse_fun = getattr(parse_module, 'Qparse1')
    line = f.readline()
    n = 0
    path = kwargs['path'].strip('.gz')
    readbuff = eval(kwargs['readbuff'])
    print Qparse_fun, readbuff
    while line:
        n += 1
        gzip_path = '.'.join([path, str(n), 'gz'])
        gzipfile = gzip.open(gzip_path, 'wb')
        gzipfile.write(Qparse_fun(line))
        for line in f.readlines(readbuff):
            t = Qparse_fun(line)
            if t:
                gzipfile.write(t+'\n')
        gzipfile.close()
        hadoop_dir = kwargs['hadoop_dir'].format(**kwargs)
        logger.warning("{0}=>{1} => {2}".format(kwargs['path'],
                                                gzip_path,
                                                hadoop_dir))
        up2hadoop(gzip_path, hadoop_dir)
        line = f.readline()
    f.close()
    os.remove(kwargs['path'])
