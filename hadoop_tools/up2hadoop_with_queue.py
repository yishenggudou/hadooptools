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

from tasks import Q
from up2hadoop_ import up2hadoop as up2hadoop_


def up2hadoop(path, hadoop_dir,):
    Q.enqueue(up2hadoop_,
              args=(path, hadoop_dir,),
              )

if __name__ == "__main__":
    import sys
    path = sys.argv[1]
    ptime = sys.argv[2]
    up2hadoop(path, ptime)
