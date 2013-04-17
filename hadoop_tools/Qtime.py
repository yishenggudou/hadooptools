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


def Qtime(timestr):
    u"""
    {year:'',month:'',day:'',hour:'',min:'',ptime:'20130304'}
    """
    ptime = timestr + '0' * 10
    ptime = ptime[:12]
    rst = {'year': ptime[:4],
           'month': ptime[4:6],
           'day': ptime[6:8],
           'hour': ptime[8:10],
           'min': ptime[10:12]}
    rst['ptime'] = ptime
    return rst
