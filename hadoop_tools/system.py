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

def get_ip_address(ifname=''):
    import subprocess
    import re
    get_ip_cmd = '/sbin/ifconfig %s | grep inet | cut -d":" -f 2 | cut -d" " -f1'%ifname
    result=subprocess.Popen(get_ip_cmd,stdout=subprocess.PIPE,shell=True)
    p = result.stdout.read().split('\n')[0].strip()
    if re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',p):
        return p
    else:
        return '127.0.0.1'

name = get_ip_address()
localip = name

if __name__ == "__main__":
    print get_ip_address()
